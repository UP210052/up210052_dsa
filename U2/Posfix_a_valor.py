#stack=pila
posfix = '5 6 2 + * 12 4 / -'
P=posfix.split()
Value=0
stack=[]
i=0
P.append(')')
while P[i]!=')':
    if P[i] in ['-','+','*','/','^']:
        B = int(stack.pop())
        A = int(stack.pop())
        if P[i] == '*':
            C = A * B
        elif P[i] == '/':
            C= A / B
        elif P[i] == '-':
            C = A - B
        elif P[i] == '+':
            C = A + B
        elif P[i] == '^':
            C = A ** B
        stack.append(C)
    else:
        stack.append(P[i])
    i+=1
Value=stack.pop()
print(Value)