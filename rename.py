import os

x = os.listdir(os.getcwd())
for file_name in x:
    print(file_name)
    if file_name.endswith(".log"):
        os.rename(file_name, file_name.replace(".log","_151220.txt"))
