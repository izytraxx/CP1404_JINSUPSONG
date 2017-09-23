import os
import shutil

print(os.getcwd())

# target_path = "/Users/izytr/PycharmProjects/"
# os.chdir(target_path)
# print(os.getcwd())
# print(os.listdir("."))

# for names, dirs, files in os.walk("."):
#     print(names)
TARGET_PATH = "/Users/izytr/PycharmProjects/test_shutil"

for each in os.listdir("."):
    print("{} is file? {} is dir? {}".format(each, os.path.isfile(each), os.path.isdir(each)))
    if os.path.isfile(each):
        split_data = each.split(".")
        if split_data[-1] == "py":
            print(split_data[0])
            source = os.path.join(os.getcwd(), each)
            target = os.path.join(TARGET_PATH, each) #join filename to path with separator
            shutil.copyfile(source, target)
