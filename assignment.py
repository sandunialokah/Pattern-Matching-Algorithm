NO_OF_CHARS = 256
pat = input("Enter a search string: ")

f = open("modules.txt", mode='r', encoding='utf-8')

count = 0
def boyerMoore(txt, pat, string):
    txt = txt[8:]
    n = len(txt)
    m = len(pat)
    
    badchar = preprocessing(pat, m)

    s = 0
    while(s <= n-m):
        j = m-1
        while(j>=0 and pat[j] == txt[s+j]):
            j -=  1
        if(j<0):
            global count
            count += 1
            #print("pattern occur shift ", s)
            print(string)
            s += (m-badchar[ord(txt[s+m])] if s+m<n else 1)
        else:
            s += max(1, j-badchar[ord(txt[s+j])])


def preprocessing(pat, size):
    badchar = [-1] * NO_OF_CHARS
    for i in range(size):
        badchar[ord(pat[i])] = i
    return badchar

with open('modules.txt') as openfileobject:
    for line in openfileobject:
        boyerMoore(line.lower(), pat.lower(), line)


print("Number of matches: ", count)
f.close()
