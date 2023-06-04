from functools import wraps

def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Код для выполнения перед вызовом декорруемой функции

        # 2. Вызов декорируемой функции и возврат
        #    полученных от неё результатов
            return func(*args, **kwargs)

        # 3. Код для выполнения ВМЕСТО вызова декорируемой функции.
    return wrapper