import os

def list_files():
    g = os.walk('./')
    for path, dir_list, file_list in g:
        for dir_name in dir_list:
            print(os.path.join(path, dir_name))
        for file_name in file_list:
            print(os.path.join(path, file_name))

def main():
   list_files()

if __name__ == '__main__':
	main()