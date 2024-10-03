# !/usr/bin/python3.10
from test_gen import most_recent, update_body, compile_tex
import os

file = most_recent()[1]
directory = most_recent()[0]
os.chdir(directory)

with open(file, 'r') as rfile:
     file_body = rfile.read()

# uploading playpy_callbacks before changing directories
file_body = update_body(file_body, True, False, False)

# Indicating Number of duplicates to be made
# ------------------------------------------
# ------------------------------------------
print(f"Creating versions of {file}.")
while True:
    try:
        copies_int = int(input("State the number of versions: "))
        break
    except:
        print("Invalid entry. Try again.")

# Creating/Updating Directory
# ------------------------------------------
# ------------------------------------------
directory_copies = file.split('.tex')[0]
directory_copies = f'{directory}/{directory_copies}/'
if os.path.exists(directory_copies):  # if directory already exists erase all contents
    os.chdir(directory_copies)
    print(f'Directory {directory_copies}\n Already exist')
    os.system("rm * -f")
else:  # if directory does not exist, create a new folder and transfer
    print(f'\nCreating directory: {directory_copies}')
    os.mkdir(directory_copies)

# Generating versions and copying them to assessment directory
# ------------------------------------------
# ------------------------------------------
for i in range(1, copies_int + 1):
    new_file = file.replace('.tex', f'--V{i}.tex')

    file_new_body = update_body(file_body, False, True, True)

    with open(new_file, 'w') as wfile:
        wfile.write(file_new_body)

    compile_tex(new_file)