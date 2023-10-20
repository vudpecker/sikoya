import string
import random



def gen_pass():
    passwd = "".join(
        random.choices(string.ascii_letters + string.digits  + string.punctuation, k=15,)
    )

    if (
        any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and any(c.isdigit() for c in password)
        and any(c in string.punctuation for c in password)
    ):
        print(passwd)
        return passwd


def test_generate_password():
    password = gen_pass()
    print("Executing password")
    assert len(password) >= 8
    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(c in string.punctuation for c in password)
    print("All tests executed")

def invok_pass():
    pass