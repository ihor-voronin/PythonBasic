class CustomException(Exception):
    err_code = -1


class IncorrectInput(CustomException):
    err_code = 104


if __name__ == "__main__":
    raise IncorrectInput
