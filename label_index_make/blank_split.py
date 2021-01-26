"""
说明：去除字符标签中的多余空格
例子："123.jpg 123 456"转换为"123.jpg 123456"
"""

def str_split_blank(ori_str):
    str_list = ori_str.split(' ')
    str_new = str_list[0] + ' '
    for i in range(1, len(str_list)):
        if str_list[i] != ' ':
            str_new += str_list[i]

    return str_new

ori_label_path = r"D:\FengZhan\ElectricityMeter\Data\virtual_make\dataset_20w_label\labels.txt"
new_label_path = r"D:\FengZhan\ElectricityMeter\Data\virtual_make\dataset_20w_label\label_split_blank.txt"

# 读取数据->去除空格
str_list_save = []
with open(ori_label_path, 'r', encoding="UTF-8") as file:
    file_list = file.readlines()
    length = len(file_list)

    for i, file_i in enumerate(file_list):
        print("{:0>5d} / {:0>5d}".format(i, length))
        str_ori = file_i.strip()
        str_new = str_split_blank(str_ori)
        str_list_save.append(str_new)

# 存储
with open(new_label_path, 'w', encoding="UTF-8") as txt:
    for text in str_list_save:
        if '\n' not in text:
            text += '\n'
        txt.writelines(text)
    txt.close()

print("finished!")



