import os
#creation of folder
def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
# whrite the file and the data
def write_file(path,data):
    f=open(path,'w')
    f.write(data)
    f.close
