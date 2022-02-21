from main import app
import sys
from fastapi.testclient import TestClient

print(f"{sys.path[:3]=}")
print(f"{__package__=}")

client = TestClient(app)


def func(a):
    return a + 5


def test_me():
    assert func(3) == 8


def test_read_main():
    main_url = "/"
    response = client.get(main_url)
    print(f"{response.json()=}")
