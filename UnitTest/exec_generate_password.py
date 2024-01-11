
import string
import random

def generate_password():
 
    # length = random.randint(8,16)
    # letters = string
    # result_str = ''.join(random.choice(letters) for _ in range(length))
    # print(result_str)
    # return result_str


    while True:
        password = "".join(
            random.choices(
                string.ascii_letters
                + string.digits
                + string.punctuation,
                k=12,
            )
        )
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and any(c.isdigit() for c in password)
            and any(c in string.punctuation for c in password)
        ):
            print(password)
            return password
 


def test_generate_password():
    password = generate_password()
    assert len(password) >= 8
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in string.punctuation for c in password)

if __name__ == "__main__":
    test_generate_password()

