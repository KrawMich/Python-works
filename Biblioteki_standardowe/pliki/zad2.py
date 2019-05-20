import sys
from collections import defaultdict

# OUTPUT_FILE_NAME = 'wynik.txt'

try:
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
except IndexError:
    print('podaj nazwę pliku')
    exit(0)

total_time = defaultdict(int)

with open(input_file_name, 'r') as f:
    for line in f.readlines():
        user, op, time = line.split(';')
        time = int(time)
        if op == 'LOGIN':
            total_time[user] -= time
        elif op == 'LOGOUT':
            total_time[user] += time
        else:
            print('nieznana operacja')


sorted_keys = list(total_time)
sorted_keys.sort(key=lambda el: int(el.split('-')[1]))
print(sorted_keys)

sorted_values = sorted(total_time, key=lambda el:total_time[el], reverse=True)
print(sorted_values)

with open(output_file_name,'w') as f:
    f.write('posortowane po userach:\n')
    for user in sorted_keys:
        f.write(f'- {user}: {total_time[user]} s\n')

    f.write('\nposortowane po czasach:\n')
    for user in sorted_values:
        f.write(f'- {user}: {total_time[user]} s\n')
