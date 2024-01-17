

def show_locals():
    val = 20
    print('Globals:', globals())
    print(120*'-')
    print('Locals:', locals())

show_locals()



num = 10

def myfunc():
    num = 20
    print('Locals:', locals())
    print('Globals:', globals())
#myfunc()

