"""
说明：将字符标签转换为字典索引标签
注意：该字典中blank字符是第0索引
"""

def find_index(char_i, char_list):
    for index, str_i in enumerate(char_list):
        if char_i == char_list[index].strip():
            return index

    print(char_i)
    print("没找到该字符！")
    return -1

dict_path = r"D:\FengZhan\ElectricityMeter\Code\ElectricityMeter\config\dictionary\char_std_433.txt"
ori_label_path = r"D:\FengZhan\ElectricityMeter\Data\virtual_make\dataset_20w_label\label_split_blank.txt"
new_label_path = r"D:\FengZhan\ElectricityMeter\Data\virtual_make\dataset_20w_label\label_index_25w.txt"

# 读取字典
with open(dict_path, 'r', encoding="UTF-8") as dict:
    char_list = dict.readlines()


# 读取数据->去除空格
str_list_save = []
with open(ori_label_path, 'r', encoding="UTF-8") as file:
    file_list = file.readlines()
    length = len(file_list)

    for i, file_i in enumerate(file_list):
        print("{:0>5d} / {:0>5d}".format(i, length))
        str_ori = file_i.strip()
        str_list = str_ori.split(' ')
        str_new = str_list[0]
        str_part = str_list[1]
        for char_i in str_part:
            index_i = find_index(char_i, char_list)
            str_new += (' ' + str(index_i))
        str_list_save.append(str_new)

# 存储
with open(new_label_path, 'w', encoding="UTF-8") as txt:
    for text in str_list_save:
        if '\n' not in text:
            text += '\n'
        txt.writelines(text)
    txt.close()

print("finished!")