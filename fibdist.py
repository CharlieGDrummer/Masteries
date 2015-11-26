def fib(n):
    if (n!=1 and n!=0):
        x =0
        y =1
        for e in range (0,n-1):
            e=x+y
            x = y
            y = e
    elif (n==1):
        e = 1
    elif (n==0):
        e = 0
    return(e)

def dist(x1, y1, x2, y2):
    if (x1 > x2):
        x = x1-x2

    elif (x1<x2):
        x = x2-x1

    if (y1>y2):
        y = y1-y2

    elif (y1<y2):
        y = y2-y1

    h = (y**2 + x**2)**(1/2)

    return (h)
