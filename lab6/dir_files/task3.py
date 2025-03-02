import os
def get_path_info(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Path '{path}' exists.")
        print(f"File name: {filename}")
        print(f"The part of the path, that points to the directory: {directory}")
    else:
        print(f"Path '{path}' does not exists.")

#xmple
path1 = "./test_file.txt"  
path2 = "./non_existent_path"

#creating file
if not os.path.exists(path1):
    with open(path1, "w") as f:
        f.write("Test content")

get_path_info(path1)
get_path_info(path2)