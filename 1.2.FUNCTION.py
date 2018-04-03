#Samuel C. Tomol
#github.com/samueltomol
#FUNCTION

#works on version python 3

print ("Let's count the no. of UPPPERCASE and lowercase letters")


def counter():
    a = input("\nEnter Words here: ")
    d = {"UPPER CASE" : 0, "LOWER CASE": 0,"SPACE": 0}
    for c in a:
        if c.isupper():
            d["UPPER CASE"] += 1
        elif c.islower():
            d["LOWER CASE"] += 1
        else:
            pass

    print (" NO. of UPPERCASE LETTERS is ", d["UPPER CASE"])
    print (" NO. of lowercase letters is ", d["LOWER CASE"])
    return counter()

counter()
