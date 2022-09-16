"""
##      label_copy.py
##      version 1
##      python --version : 3.6.13
##      emailremoved@ ( ozan.akyel54@gmail.com )
##      @author : Ozan AKYEL

"""
import os

# folder_path = input("Enter the path to the read files: ")
# saving_path = input("Enter the path to the file that has the saving folder: ")

yolo_label_path = r"C:\Users\ozan.akyel\Desktop\deneme\0_999_01_061221_121647_ORJ_crop.txt" # label path
saving_path = r"C:\Users\ozan.akyel\Desktop\deneme"

if not os.path.exists(saving_path): # if saving folder isn't exists, will be creating
    try:
        os.makedirs(saving_path)
        print(f"{saving_path} was created")
    except FileExistsError:
        print("can not created")
else:
    print("Directory " , saving_path ,  " already exists")

file = open(yolo_label_path, "r+")  # referance label is reading
icerik = file.read()
print(icerik)

for i in os.listdir(saving_path):
    if i.endswith(".jpg"):
        name, ext = i.split('.')
        name_txt = name + ".txt" 
        f= open(os.path.join(saving_path, name_txt),"w+")
        print(f)
        f.write(icerik)
        f.close
        print("işlem tamam")
    else:
        print(f"{i} degistirilmek istenen türde dosya değil")
