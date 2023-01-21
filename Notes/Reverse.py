a=[10,20,30,40,50]
for i in range(len(a)):
    for n in range(len(a)-1):
        if a[n] < a[n+1]:
            a[n], a[n+1]= a[n+1], a[n]
print(a) 