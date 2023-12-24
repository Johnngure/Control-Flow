#map (function, iterable)

def make_even(num):
    if num%2==1:
        return num + 1
    else:
        return num
    
x = [ 112, 113, 114, 115, 120, 121, 130, 133]

y = list(map(make_even, x))
print(y)    
