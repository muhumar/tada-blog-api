class ArticleNotFound(Exception):
    def __init__(self, id: int):
        self.message = f"Article with ID {id} not found."
        super().__init__(self.message)


class ArticleAlreadyExists(Exception):
    def __init__(self, id: int):
        self.message = f"Article with ID {id} already Exists."
        super().__init__(self.message)


class ArticleValidationError(Exception):
    def __init__(self, errors, status_code=422):
        self.errors = errors
        self.status_code = status_code
        super().__init__(self.format_errors())

    def format_errors(self):
        formatted = {}
        for error in self.errors:
            key = '.'.join(str(x) for x in error['loc'])
            formatted[key] = error['msg']

        return formatted
