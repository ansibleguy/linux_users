class FilterModule(object):

    def filters(self):
        return {
            "intersection": self.intersection,
            "ensure_list": self.ensure_list,
        }

    @classmethod
    def intersection(cls, search_for: (list, str), search_in: (list, str)) -> bool:
        # check if any elements of list X are in list Y
        search_for = cls.ensure_list(search_for)
        search_in = cls.ensure_list(search_in)
        matches = len(set(search_in).intersection(search_for))
        return True if matches > 0 else False

    @staticmethod
    def ensure_list(data: (str, list)) -> list:
        # if user supplied a string instead of a list => convert it to match our expectations
        if type(data) == str:
            return [data]

        else:
            return data
