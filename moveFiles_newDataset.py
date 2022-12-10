#created by Amrit for the Manipal MedTech Hackathon '22 (Second phase) on 10-12-2022

import os
import shutil

parent_folder = r'...' + '\\'
#parent target folder

if not os.path.exists(parent_folder):
    os.mkdir(parent_folder)


target_folder1 = os.path.join(parent_folder, "adc")
if not os.path.exists(target_folder1):
    os.mkdir(target_folder1)

target_folder2 = os.path.join(parent_folder, "dwi")
if not os.path.exists(target_folder2):
    os.mkdir(target_folder2)

target_folder3 = os.path.join(parent_folder, "flair")
if not os.path.exists(target_folder3):
    os.mkdir(target_folder3)

for n in range(251):
    if n==0:
        continue
    ns = str(n)
    src = ns.zfill(4)
    source_folder = r'D:\dataset_ISLES22\_rawdata\sub-strokecase' + src + '\ses-0001' + '\\'
    os.chdir(source_folder)

    print("CASE", src)
    for file in os.listdir():
        name, ext = os.path.splitext(file)
        if ext == '.json' or file == target_folder1:
            continue
        nameList = name.split("_")
        type = nameList[2]

        if type == "adc.nii":
            shutil.copy(file, target_folder1)
            print(file,"--FILE COPIED TO-->>",target_folder1)

        if type == "dwi.nii":
            shutil.copy(file, target_folder2)
            print(file,"--FILE COPIED TO-->>",target_folder2)

        if type == "flair.nii":
            shutil.copy(file, target_folder3)
            print(file,"--FILE COPIED TO-->>",target_folder3)
    print()

