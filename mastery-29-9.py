nick = input("Type your nickname, no longer than 10 characters: ")
while (len(nick) > 10):
    nick = input("Hey, type a nickname no longer than 10 characters: ")

intnum = input("Type an integer number: ")
while ("." in intnum):
    intnum = input("Hey, type just integers please: ")
while True:
    try:
        intnum = int(intnum)
        break
    except ValueError:
        intnum = input("Hey, please just integers: ")
        
while True:
    try:
        floatnum = float(input("Type a float please: "))
        break
    except ValueError:
        print( "That's not a float!")
