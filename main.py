
l1 = [3, 6, 5, 2, 9, 8, 7]


def fact(n):
    if n == 0:  
        return 1  
    else:
        return n * fact(n - 1) 

factorial_list = [fact(x) for x in l1]


print(factorial_list)
