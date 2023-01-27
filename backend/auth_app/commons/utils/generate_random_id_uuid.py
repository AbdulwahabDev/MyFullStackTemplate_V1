import random
import string
import uuid


def generate_random_id(keys_size=10):
    random_id = "".join(random.choices(string.ascii_letters + string.digits, k=keys_size))
    return random_id


def generate_random_uuid():
    return str(uuid.uuid4())
