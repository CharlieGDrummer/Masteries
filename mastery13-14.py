import fibdist


choice = input("Type '1' for fibonacci, Type '2'. for distance between points :")

if (choice == "1"):
    n = int(input("Type a number for fibonacci: "))
    r = fibdist.fib(n)
    print ("The fibonacci number is: ",r)
    
    
elif (choice == "2"):
    x1 = int(input("Type the x component in the first point: "))
    y1 = int(input("Type the y component in the first point: "))
    
    x2 = int(input("Type the x component in the second point: "))
    y2 = int(input("Type the y component in the second point: "))
    r = fibdist.dist(x1,x2,y1,y2)
    print ("The distance between the points is: ",r)
