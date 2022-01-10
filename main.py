l1 = []
l2 = []

def anagrama(string1, string2):
    i = 0
    j = 0

    if len(string1) != len(string2):
        return False
    else:
        while i != len(string1):
            l1.append(ord(string1[i]))
            i += 1
        while j != len(string1):
            l2.append(ord(string2[j]))
            j += 1
        return l1, l2

def compareList(l1, l2):
    if l1 != []:
        l1.sort()
        l2.sort()
        if (l1 == l2):
            return "Equal"
        else:
            return "Non equal"
    else:
        return "Non equal"

anagrama("amor", "roma")
print(l1, l2)
if anagrama != 0:
    print(compareList(l1, l2))

