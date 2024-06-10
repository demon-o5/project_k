import os
import datetime
def create_file(filename):
    try:
        with open(filename,'w') as f:
            f.write("#new file created")
        print(f'{filename} \t new file is created')
    except Exception as e:
        print("unable to create the file")

def check_file(filename):
    '''this is  used to chec the file is empty or not'''
    if os.path.getsize(filename) ==0:
        raise Exception ("file is empty")

def remove_file_name(filename):
    '''this function is used to check and remove the file '''
    if os.path.exists(filename):
        if os.path.getsize(filename) !=0:
            #raise ValueError(f"file is not empty {filename}")
            f=open(filename,'r')
            print(f.read())
        else:
            os.remove(filename)
    else:
        print(f"file not exist {filename}")

def rename_file(filename,new_name=None):
    '''rename the file'''
    base, ext = os.path.splitext(filename) # split file and extension and adding date to file name
    new_name = f"{base}_{datetime.date.today()}{ext}"
    os.rename(filename,new_name)
    print(f"File renamed to {new_name}")

#m=create_file('file_2.txt') this is used to create
#rename_file('file_1.txt') this is used to rename the file
    
