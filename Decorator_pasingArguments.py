def decorator(fun):
    def wrapor(*args, **kwargs):
        print('top')
        fun(*args,**kwargs)
        print('Bottom')
    return wrapor
# Remember the wraper returns in the decerator ffungtion level not in wraper fugtion level

@decorator
def chocolate():
    print("Chocolate ")

@decorator
def cake(name):
    print('Cake another fungtion '+name)


chocolate()
print('**********************')
cake('Shankar')