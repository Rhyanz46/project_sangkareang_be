from flask import abort
from core import result


class ValueChecker:
    def __init__(self, data_request):
        self.data_request = data_request
        self.type = type(data_request)
        self.__parsed = {}

    def parse(self, field, field_type, nullable=False, length=float("inf")):
        is_dict = self.type == dict

        data_request = self.data_request

        if is_dict:
            value = data_request.get(field)
            if not nullable and not value:
                msg = {
                    "message": 'field {} it\'s can\'t be null'.format(field)
                }
                abort(result(msg, 400))

            wrong_type = type(value) != field_type
            wrong_len = len(str(value)) > length
            if wrong_type:
                msg = {
                    "message": 'field {} it\'s must be {}'.format(field, field_type)
                }
                abort(result(msg, 400))
            if wrong_len:
                msg = {
                    "message": 'length of filed {} can\'t over {}'.format(field, length)
                }
                abort(result(msg, 400))
            self.__parsed.update({field: value})

    def get_parsed(self):
        return self.__parsed
