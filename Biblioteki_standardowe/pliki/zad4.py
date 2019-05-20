import os

dir_name = 'e:'

scan = os.scandir(dir_name)
print(scan)

dir_content = [el for el in scan]
print(dir_content)

for dir_entry in dir_content:
    print(f'{dir_entry.name}: czy jestem katalogiem? {dir_entry.is_dir()}')
    if dir_entry.is_dir():
        print(list(os.scandir(dir_entry)))
