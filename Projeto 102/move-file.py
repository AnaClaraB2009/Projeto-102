import os
import shutil

from_dir = "C:\\Users\\anacl\\Downloads\\Origem"
to_dir = "C:\\Users\\anacl\\Downloads\\Destino"

list_of_files = os.listdir(from_dir)

print (list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    print(extension)

    if extension == '': 
        continue
    
    if extension in ['‘.txt’, ‘.doc’, ‘.docx’, ‘.pdf’']:
        path_1 = from_dir + "/" + file_name
        path_2 = to_dir + '/' + "Arquivos_Texto"
        path_3 = to_dir + '/' + "Arquivos_Texto" + '/'  + file_name
    
        if os.path.exists(path_2):
            print ("Movendo" + file_name + ".....")
            shutil.move(path_1,path_3)

        else :
            os.makedirs(path_2)
            print ("Movendo" + file_name + ".....")
            shutil.move(path_1,path_3)

