#Samuel C. Tomol
#github.com/samueltomol
#PALINDROME

pal = input ("Enter a palindrome:")
fram = 1
red = 0
blue = 1
while True:
    if (red > int (len(pal))):
        break
    if (blue > int (len(pal))):
        break

    c = pal[red]
    red += 1
    d = pal[-blue]
    blue += 1

    if (c != d):
        fram = 0

if (fram == 0):
    print (pal, "NOT PALINDROME")
     
elif (fram == 1):
    print (pal, "PALINDROME")
