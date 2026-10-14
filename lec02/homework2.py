
def arithmetic(x,y):
    if isinstance(x, str) and isinstance(y, str):
        return x+y
    elif isinstance(x, float) and isinstance(y, str):
        return str(x)+y
    elif isinstance(x, str) and isinstance(y, float):
        return x*int(y)
    elif isinstance(x, float) and isinstance(y, float):
        return x*y
print(arithmetic("Hello ", "World!!"))
print(arithmetic(2.5,"Grade"))
print(arithmetic("Mahesh",4.0))
print(arithmetic(2.0,3.2))
