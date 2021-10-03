class FilterModule(object):

    def filters(self):
        return {
            "parse_nested_members": self.parse_nested_members,
        }

    @staticmethod
    def parse_nested_members(groups: dict, max_nesting_depth: int = 10) -> dict:
        for i in range(max_nesting_depth):
            # recursion the extension of the members to process nested groups

            for name, g in groups.items():
                member_nesting = False
                parent_nesting = False

                if 'member_of' in g:
                    member_nesting = True
                    member_key = 'member_of'

                elif 'parents' in g:
                    member_nesting = True
                    member_key = 'parents'

                if 'children' in g:
                    parent_nesting = True
                    parent_key = 'children'

                elif 'nested_groups' in g:
                    parent_nesting = True
                    parent_key = 'nested_groups'

                if member_nesting:
                    for p in g[member_key]:
                        groups[p]['members'].extend(g['members'])

                if parent_nesting:
                    for c in g[parent_key]:
                        g['members'].extend(groups[c]['members'])

        # removing duplicate members
        for g in groups.values():
            g['members'] = list(set(g['members']))

        return groups
