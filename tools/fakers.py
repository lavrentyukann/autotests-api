import time

# функция будет генерировать уникальный email в формате test.1740687022.054204@example.com
def get_random_email() -> str:
    return f"test.{time.time()}@example.com"