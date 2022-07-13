def voyToLetter(src):
    ret = [src]
    for letter in changes:
        buf = ''
        checkDouble = 1
        for c in src:
            if (c in voy):
                c = letter
            buf += c
        for r in ret:
            if r == buf:
                checkDouble = 0
        if checkDouble:
            ret.append(buf)
    return (ret)

word = 'tartuf'
changes = ['i', 'a', 'u', 'y']
voy = ['i', 'a', 'u', 'y', 'e', 'o']
rez = []

rez += voyToLetter(word)
for result in rez:
    print(result)

