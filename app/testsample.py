

def deco1(f):
    print("デコレート")

    def wrapper(f):
        print("defore exec", f)
        v = f()
        print("after exce", f)
        return v
    return wrapper


@deco1(f=3)
def func():
    print("exec")
    return 1


func()
