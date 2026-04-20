class ErrorHandler:
    def __init__(self):
        self.error_codes = {
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            500: "Internal Server Error"
        }

    def handle_error(self, error_code):
        if error_code in self.error_codes:
            return self.error_codes[error_code]
        else:
            return "Unknown Error"

    def handle_exception(self, exception):
        if isinstance(exception, ValueError):
            return "Invalid input"
        elif isinstance(exception, TypeError):
            return "Invalid data type"
        else:
            return "Unknown Error"

def main():
    error_handler = ErrorHandler()

    try:
        # Simulate an error
        raise ValueError("Invalid input")
    except Exception as e:
        print(error_handler.handle_exception(e))

    try:
        # Simulate an error
        raise TypeError("Invalid data type")
    except Exception as e:
        print(error_handler.handle_exception(e))

    print(error_handler.handle_error(404))

if __name__ == "__main__":
    main()
