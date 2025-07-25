def Summer_discount_Decorator(fun):
    def wraper(number):
        return fun(number)*0.15
    return wraper
@Summer_discount_Decorator
def calculate(number):
    return number

print(f'discount for the sumer is ${calculate(500)}')