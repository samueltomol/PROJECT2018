#Samuel C. Tomol
#github.com/samueltomol
#STR AND CHAR MANIPULATIONS

str = "Data Structure"

print("String is %d bytes long" % len(str))

print(str.upper())

print("The index of the S is %d" % str.upper().index("S"))

print("There are %d letter T's in '%s'" % (str.upper().count("T"), str))

#slice the string
print(str[7])
print(str[0:4])
print(str[5:len(str)])

name = "SAMUEL TOMOL"
mylist = name.split(" ")
print(mylist)
print("First Name : %s , Last Name : %s" %(mylist[0],mylist[1]))
