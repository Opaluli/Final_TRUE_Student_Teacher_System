
# This file holds mock data for student requests

requests_data = [
    {
        "student": "David Levi",
        "topics": {
            "Math": "red",
            "History": "green",
            "Science": "yellow"
        },
        "message": "I'm really struggling with algebra."
    },
    {
        "student": "Noa Cohen",
        "topics": {
            "English": "yellow",
            "Biology": "red"
        },
        "message": "Please help with cell structure."
    },
    {
        "student": "Amit Azulay",
        "topics": {
            "Computer Science": "green",
            "Physics": "yellow"
        },
        "message": "Need more examples on Newton's laws."
    }
]


users = [
    {"username": "teacher1", "password": "1234", "role": "teacher"},
    {"username": "student1", "password": "abcd", "role": "student"},
    {"username": "teacher2", "password": "5678", "role": "teacher"},
    {"username": "student2", "password": "efgh", "role": "student"}
]

def get_user_by_credentials(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return user
    return None
