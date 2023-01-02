
from xml.etree.ElementInclude import include


temp = 0

def printTemp():
    print(temp)


def add(left, right):
    return left + right

def subtract(left, right):
    return left - right

def multiply(left, right):
    return left * right

def divide(left, right):
    if right == 0:
        print("Error : right value is 0.")
    else:
        return left / right


def sum(first, *values):
    val = first
    for value in values:
        val += value
    return val
    

printTemp()
a = 10
b = 20
print(add(10, 20))
print(divide(a, 0))
print(sum(1,2,3,4,5,6,7,8,9))

def increaseA(value = 1):
    global a
    a += value

def increase(target, value = 1):
    return target + value


increaseA(7)
print(a)

a = increase(a,2)
print(a)

