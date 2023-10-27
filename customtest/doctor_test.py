from test import Test, TestCase

# Path: doctor/tests.py
login = TestCase(
    url="http://127.0.0.1:8000/doctor/login/",
    headers={
        "Content-Type": "application/json",
        "accept": "application/json",
        "X-CSRFToken": "tSOWvjB7Ln14dkmxh3uRWn71D6hMN3t2uZm5Lx23QeUYsevFpGRP7cKhGhudNZXf",
    },
    data={"username": "09353941017", "password": "123456"},
)
print(Test([login]))
