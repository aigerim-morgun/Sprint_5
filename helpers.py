import random 


def generate_email():
    number = random.randint(100, 999)
    return f"aigerimmorgun36{number}@yandex.ru"


def generate_password():
    return str(random.randint(100000, 999999))


def generate_short_password():
    return str(random.randint(1000, 9999))