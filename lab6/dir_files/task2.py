import os

def check_access(path):
    print(f"Checking path access: {path}")
    exists = os.path.exists(path)
    print(f"Exists: {exists}")

    if exists:
        readable = os.access(path, os.R_OK)
        print(f"Readable: {readable}")

        writable = os.access(path, os.W_OK)
        print(f"Ready to write: {writable}")

        executable = os.access(path, os.X_OK)
        print(f"Ready for execute: {executable}")
    else:
        print("Cannot verify access rights because the path does not exist.")

#xpmle
path1 = "./test_file.txt"  
path2 = "./non_existent_path"

if not os.path.exists(path1):
    with open(path1, "w") as f:
        f.write("Test content")

check_access(path1)
check_access(path2)