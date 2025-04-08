class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def is_teacher(self):
        return False

class Student(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.requests = []

class Teacher(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.student_requests = []

    def is_teacher(self):
        return True