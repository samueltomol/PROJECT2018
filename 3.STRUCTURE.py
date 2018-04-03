#Samuel C. Tomol
#github.com/samueltomol
#STRUCTURE


letters = ['s','s','a','a','m','m','u','u',
                'e','e','l','l','t','t','t','o',
                'o','m','m','o','l','l','l',
                's','s','s','a','l','o','o','s',
                'l','l','s','o','s','s','w']


from collections import Counter
letters_counts = Counter(letters)
repeat = letters_counts.most_common(3)
print ("letters repeated")
print(repeat)
