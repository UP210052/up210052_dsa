A=5
B=8
C=9
if A>B and A>C:
    print(A)
elif B>A and B>C:
    print(B)
elif C>A and C>B:
    print(C)

if A>=B:
    if A>=C:
        print(A)
    elif C>A:
        print(C)
elif B>=A:
    if C>B:
        print(C)
    elif B>=C:
        print(B)
