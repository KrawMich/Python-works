word = input('Podajwyrza do sprawdzenia ')
is_palindrome = word.find(word[::-1])
if is_palindrome == 0:
    print('To jest palindrom ')
else:
    print('To nie jest plindrom')