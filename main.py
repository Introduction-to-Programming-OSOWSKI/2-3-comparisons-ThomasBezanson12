def greaterThan(x, y):
    if x > y:
        return True
    else:
        return False
def lessThan(x, y):
    if x < y:
        return True
    else:
        return False
def equalTo(x, y):
    if x == y:
        return True
    else:
        return False
def greaterOrEqual(x, y):
    if x >= y:
        return True
    else:
        return False
def lessOrEqual(x, y):
    if x <= y:
        return True
    else:
        return False
print(greaterThan(5,4))
print(lessThan(4,5))
print(equalTo(5,5))
print(greaterOrEqual(5,3))
print(lessOrEqual(3,5))