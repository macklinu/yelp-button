__author__ = 'macklinu'


class JsonResponse:
    def __init__(self, **entries):
        self.__dict__.update(entries)