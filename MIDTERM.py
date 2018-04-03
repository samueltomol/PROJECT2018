#Samuel C. Tomol
#github.com/samueltomol
#MIDTERM
def match_a():
    print ("Function match_a() \n")

    sam1 = input("Enter 1st input:")
    sam2 = input("Enter 2nd input:")
    sam3 = input("Enter 3rd input:")

    sam22 = []
    sam33 = []
    sam11 = []

    for i in sam1:
        if len(i) != 1:
            if i == i[::-1]:
                sam11.append(i)

    for i in sam2:
        if len(i) != 1:
            if i == i[::-1]:
                sam22.append(i)

    for i in sam3:
        if len(i) != 1:
            if i == i[::-1]: 
               sam33.append(i)

    print ("1st output: ", len(sam11))
    print("2nd output: ", len(sam22))
    print ("3rd output: ", len(sam33))


match_a()
print ("\n\n")


def front_x():
    print ("Function front_x()\n")

    sam1 = input("Enter 1st input:")
    sam2 = input("Enter 2nd input:")
    sam3 = input("Enter 3rd input:")

    sam11 = []
    sam111 = []
    sam22 = []
    sam222 = []
    sam33 = []
    sam333 = []

    for i in sam1:
        if i.startswith('x'): 
            sam11.append(i)
        else:
            sam111.append(i) 

    print ("1st output: ", sorted(sam11) + sorted(sam111)) 

    for i in sam2:
        if i.startswith('x'): 
            sam22.append(i)
        else:
            sam222.append(i)  

    print ("2nd output: ", sorted(sam22) + sorted(sam222)) 

    for i in sam3:
        if i.startswith('x'): 
            sam33.append(i)
        else:
            sam333.append(i)  

    print ("3rd output: ", sorted(sam33) + sorted(sam333)) 


front_x()
