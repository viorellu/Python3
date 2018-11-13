r = []
for i in range(2600, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        r.append(str(i))

print(','.join(r))

#####################
i=int(input("input number here:"))
r=1
for x in range(1, i+1):
    r=r*x
    print(x,r)

print(r)

####################

n=int(input("input number here:"))
d=dict()
for i in range(1, n+1):
    d[i]=i*i

print(d)

###############################

print([x for x in range(2, 100) if all(x % y != 0 for y in range(2, x))])

###############################

values=input("your nuumbers here: ")
l=values.split(",")
t=tuple(l)
print(l)
print(t)

################################

s = 'Academie'
print(len(s))
print(s[0])
print(s[1])
print("Ultimul element din string: " ​+ str(s[-1]))
print("Penultimul element din satring: " ​+ str(s[-2]))
print("​\n​"​)
print("Captam anumite secvente din string")
print(s[1:3])
print(s[1:])
print(s[0:3])
print(s[:3])
print(s[:-1])
print(s[:])
print(s * 3)
print(s.upper())

######################################

s = input("input text: ")
words = [word for word in s.split(" ")]
print(" ".join(sorted(list(set(words)))))

#######################################

n=[]
for i in range(1000, 3001):
    s=str(i)
    if(int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        n.append(s)
print(",".join(n))

######################################

new_list = [a for a in range(1,3001) if all(int(b) % 2 == 0 for b in str(a))]
for x in new_list:
    print(x)

#######################################

new_list =[]
for a in range(1,10000):
    for b in str(a):
        if int(b) % 2 != 0:
            break
    else:
        new_list.append(a)
for x in new_list:
    print(x)

#######################################
n="9"
print(int(n)+int(n*2)+int(n*3)+int(n*4))

########################################

l=[]
r=input("numerele acilea ")
for c in r.split(","):
    if int(c)%2 != 0:
        l.append(c)
print(",".join(l))
with open("test.txt", mode='wt', encoding='utf-8') as f:
    f.writelines(",".join(l))

########################################

l=[1,2,3,4,5]
print(l)
l.pop(3)
print(l)
s=[]
for i in l:
    s.append(str(i))
print(",".join(s))

#########################################

