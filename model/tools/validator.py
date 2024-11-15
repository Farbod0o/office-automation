import re
from datetime import datetime


def pattern_validator(pattern, message):
    def inner1(function_name):
        def inner2(self, text):
            if isinstance(text, str) and re.match(pattern, text):
                result = function_name(self, text)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


def date_validator(message):
    def inner1(function_name):
        def inner2(self, date_param):
            if isinstance(date_param, datetime):
                result = function_name(self, date_param)
            elif isinstance(date_param, str):
                date_param = date_param.replace('/', '-')
                try:
                    date_param = datetime.strptime(date_param, '%Y-%m-%d').date()
                    result = function_name(self, date_param)
                except:
                    raise ValueError(message)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


def time_validator(message):
    def inner1(function_name):
        def inner2(self, date_time_param):
            if isinstance(date_time_param, datetime):
                result = function_name(self, date_time_param)
            elif isinstance(date_time_param, str):
                date_time_param = date_time_param.replace('/', '-')
                try:
                    date_time_param = datetime.strptime(date_time_param, '%Y-%m-%d %H:%M:%S')
                    result = function_name(self, date_time_param)
                except:
                    raise ValueError(message)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


def date_time_validator(message):
    def inner1(function_name):
        def inner2(self, date_time_param):
            if isinstance(date_time_param, datetime):
                result = function_name(self, date_time_param)
            elif isinstance(date_time_param, str):
                date_time_param = date_time_param.replace('/', '-')
                try:
                    date_time_param = datetime.strptime(date_time_param, '%Y-%m-%d %H:%M:%S').date()
                    result = function_name(self, date_time_param)
                except:
                    raise ValueError(message)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


def boolean_validator(message):
    def inner1(function_name):
        def inner2(self, bool_param):
            if isinstance(bool_param, bool):
                result = function_name(self, bool_param)
            else:
                raise ValueError(message)
            return result

        return inner2

    return inner1


class Validator:

    @classmethod
    def positive_int_validator(cls, int_value, message):
        if isinstance(int_value, int) and int_value >= 0:
            return int_value
        else:
            raise ValueError(message)

