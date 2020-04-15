from typing import Union

def divide(dividend:[int,float],divisor:[int,float]):
    if divisor==0:
        raise ValueError("Divisor cannot be zero.....")
    return dividend/divisor

def multiply(*args:Union[int,float]):
    if len(args)==0:
        raise ValueError("At least one value should be passed")

    total=1
    for arg in args:
        total*=arg

    return total