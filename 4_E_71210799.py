print ('masukkan 3 bilangan yang diinginkan!')
a1=int(input('masukkan bilangan 1 = '))
b2=int(input('masukkan bilangan 2 = '))
c3=int(input('masukkan bilangan 3 = '))

if a1>b2 and a1>c3:
    if b2>c3:
        print(c3, b2, a1)
    else:
        print(b2, c3, a1)
elif b2>a1 and b2>c3:
    if a1>c3:
        print(c3, a1, b2)
    else:
        print(a1, c3, b2)
else:
    if a1>b2:
        print(b2, a1, c3)
    else:
        print(a1, b2, c3)
