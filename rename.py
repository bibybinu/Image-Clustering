import os
import shutil



folder_path = 'images/'

new_dest="dataset/products/"


file_list = os.listdir(folder_path)

counter=0


for file_name in file_list:

    file_path = os.path.join(folder_path, file_name)


    lst=list(file_name.split("_"))



    val=int(lst[0])
    

    ftp=lst[-1].split(".")[1]
    if val>=800 and val<=999:
      print(lst)
      new_name="products_"+str(counter)+"."+"jpg"
      new_path = os.path.join(new_dest, new_name)
      shutil.copy2(file_path, new_path)
      counter+=1



