from app import add


def test_add():
   assert add(10, 20) == 30

if __name__ == "__main__":
    test_add()
    print("All tests passed!")