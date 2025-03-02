import os

def list_directories_files(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exists.")
        return

    directories = []
    files = []
    all_items = []

    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        all_items.append(item)
        if os.path.isdir(full_path):
            directories.append(item)
        elif os.path.isfile(full_path):
            files.append(item)

    print("Dirs:")
    for directory in directories:
        print(f"- {directory}")

    print("\nFiles:")
    for file in files:
        print(f"- {file}")

    print("\nAll elements:")
    for item in all_items:
        print(f"- {item}")

#xmpl
path = "./"  
list_directories_files(path)