# MyError.py

class invalid(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"Invalid Error: {self.message}"

    
