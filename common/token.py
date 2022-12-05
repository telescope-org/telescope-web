import jwt



def gen_token(phone: str):
    return jwt.encode({"phone": phone}, "secret", algorithm="HS256")


def check_token(token: str, phone: str):
    payload = jwt.decode(token, "secret", algorithms=["HS256"])
    if payload["phone"] == phone:
        return True
    return False