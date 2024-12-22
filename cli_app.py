import os
import shutil
import sys

# Zadanie 3
def copy_file(src, dst):
    shutil.copy(src, dst)

def delete_file(src, dst):
    shutil.remove(src, dst)

def main():
    if len(sys.argv) < 3:
        print("usage: cli_all.py <command> <file_path> [destination_path]")
        sys.exit(1)

    command = sys.argv[1]
    file_path = sys.argv[2]

    if command == "copy" and len(sys.argv) == 4:
        destination_path = sys.argv[3]
        copy_file(file_path, destination_path)
    elif command == "delete":
        delete_file(file_path)
    else:
        print("nieprawidłowe command albo argument")
        sys.exit(1)

if __name__ ==  "__main__":
    main()