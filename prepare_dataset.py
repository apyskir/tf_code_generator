import os
from paths import TENSORFLOW_DIR, dataset_path

def read_files_from_directory(directory):
    inside = os.listdir(directory)
    for element in inside:
        if os.path.isdir(os.path.join(directory, element)):
            read_files_from_directory(os.path.join(directory, element))
        elif element[-3:] == '.py':
            with open(os.path.join(directory, element), 'r') as source_file:
                with open(dataset_path, 'a') as target_file:
                    content = source_file.read()
                    target_file.write(content)

def main():
    read_files_from_directory(TENSORFLOW_DIR)

if __name__ == '__main__':
    main()
    print('dupa')
