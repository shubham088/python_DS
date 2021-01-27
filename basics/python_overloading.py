
# def sum(a,b):
#     return a+b


# def sum(a):     #this function is overriding the above method.
#     return a+10

#therefore to achieve overloading in python we can use default arguments or args, kwargs concept

# def sum(a, b=None):
#     if b is not None:
#         return a+b
#     else:
#         return a+10
#or 
def sum(*a):
    sum = 0
    if len(a) == 1:
        return a[0]+10
    for x in a:
        sum+=x
    return sum 

print(sum(5,5))

print(sum(10))