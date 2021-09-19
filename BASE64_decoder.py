b = int(input())
if b == 0:
    i1 = "0"
    i2 = "1"
else:
    i1 = "1"
    i2 = "0"
a = input()
c = ""
arr = []
arra = []
h = 0
i = 0
while i < len(a):
    if (a[i] == "0"):
        h+=1
        i+=1
    else:
        arr.append(a[0:h*2+1])
        a = a[h*2+1:len(a)]
        h = 0
        i = 0
for i in range(0, len(arr)):
    arra.append(int('0b' +arr[i], 2))
for i in range(0, len(arra)):
    if (i%2==0):
        c+=i1*arra[i]
    else:
        c+=i2*arra[i]
arra = []
while c!="":
    arra.append(c[0:8])
    c = c[8:len(c)]
print(arra)

