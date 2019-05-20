import sys

try:
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
except IndexError:
    print('podaj nazwę pliku')
    exit(0)

cleaned = set()

with open(input_file_name, 'r') as f:
    for line in f.readlines():
        if line.count('@') != 1:
            continue
        cleaned.add( line.lower().strip())

to_file = sorted(cleaned)

with open(output_file_name,'w') as f:
    f.write('\n'.join(to_file))

