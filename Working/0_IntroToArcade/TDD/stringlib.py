def strLength(mystring):
    total = 0
    for i in mystring:
        total += 1
    return total
print(strLength(input()))

def lettercount(mystring, letter):
    occureces = 0
    for i in mystring:
        if i in letter:
            occureces += 1
    return occureces
print(lettercount(input(), input()))

string = input()
def removeLspace():
    new_string = ""
    for i in string:
        if i is not " ":
            new_string += i
    return new_string
print(removeLspace())
