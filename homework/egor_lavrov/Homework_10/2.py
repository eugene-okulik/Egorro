'''Создайте универсальный декоратор, который будет управлять тем,
сколько раз запускается декорируемая функция'''


def repeat_me(count):
    def inner(func):
        def wrapper(*args):
            for x in range(count):
                func(*args)
        return wrapper
    return inner


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
