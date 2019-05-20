print('Ciąg fibonacziego')
ile = int(input('Ile liczb ciągu fibonacziego chcesz wypisać ?'))

a = 0
b = 1
x = 0

if ile == 0:
    print(' NIC !!!!!')

else:
    print(1)
    while x != ile:
        x += 1
        fibonaczi = a + b
        print(fibonaczi)
        a = b
        b = fibonaczi

        

