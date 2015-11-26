f = open("93cars.dat.txt","r")

text = f.readlines()

f.close()

f = open("93cars.dat.txt","w")


x = 1
for line in text:
    x = x+1
    if (x % 2 == 0):
        f.write(line)
        
f.close()

#Start over

f = open("93cars.dat.txt","r")

text = f.readlines()

f.close()

f = open("93cars.dat.txt","w")


for line in text:
    f.write(line[0:29])

f.close
