def decorator(fun):
    def wrapor():
        print('top')
        fun()
        print('Bottom')
    return wrapor

@decorator
def chocolate():
    print("Chocolate")

@decorator
def cake():
    print('Cake another fungtion')


chocolate()
print('**********************')
cake()