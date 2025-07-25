def decorator(fun):
    def wrapor():
        print('top')
        fun()
        print('Bottom')
    return wrapor
# Remember the wraper returns in the decerator ffungtion level not in wraper fugtion level

@decorator
def chocolate():
    print("Chocolate")

@decorator
def cake():
    print('Cake another fungtion')


chocolate()
print('**********************')
cake()