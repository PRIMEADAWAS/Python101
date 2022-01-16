import os
import shutil
cur_path = os.getcwd()
print(cur_path)  # get current path

print(os.listdir())  # list file

rel_path = 'FileManage/demo'
abs_path = cur_path + '/'+rel_path
print(os.listdir(rel_path))  # go to rel path
print(os.listdir(abs_path))  # go to abscls path

# os.mkdir(abs_path+'/MakeNewFolder1')
# os.mkdir(abs_path+'/MakeNewFolder2')


# shutil.move(abs_path+'/MakeNewFolder1'+'/test1.txt', abs_path+'/MakeNewFolder2')
# shutil.move(abs_path+'/MakeNewFolder2'+'/test1.txt', abs_path+'/MakeNewFolder1')


for file in os.listdir(abs_path+'/MakeNewFolder1'):
    # print(file)
    shutil.move(abs_path+'/MakeNewFolder1'+'/' +
                file, abs_path+'/MakeNewFolder2')
