def getCount(word,letter):
    count=0
    for c in word:
        if c==letter:
            count+=1

    return count

# print(getCount("hello",'l'))

def letter_count(word):
    d={}
    for letter in word:
        d[letter]=getCount(word,letter)

    return d

print(letter_count("renuka"))


def palindromable(s):
    odds=[]
    count=letter_count(s)
    odds=[k for k in count if count[k]%2]
    return len(odds)<=1

print("palindromable" if palindromable("malayala") else "not palindromable")