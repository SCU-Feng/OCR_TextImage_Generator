"""
说明：将标签文件划分为训练标签文件和测试标签文件
"""

import random

label_path = r"D:\FengZhan\ElectricityMeter\Data\virtual_make\dataset_20w_label\label_index_25w.txt"
save_test_path = r"D:\FengZhan\ElectricityMeter\Data\virtual_make\dataset_20w_label\label_index_25w_test_5w.txt"
save_train_path = r"D:\FengZhan\ElectricityMeter\Data\virtual_make\dataset_20w_label\label_index_25w_train_20w.txt"
rate = 0.8

# 读取数据->打乱
with open(label_path, 'r', encoding="UTF-8") as label:
    str_list = label.readlines()
    length = len(str_list)
    threshold = int(length * rate)
    random.shuffle(str_list)                                    # 源列表随机打乱
    test_save_list = str_list[threshold:]
    train_save_list = str_list[:threshold]

# 存储
with open(save_test_path, 'w', encoding="UTF-8") as txt:
    for text in test_save_list:
        if '\n' not in text:
            text += '\n'
        txt.writelines(text)
    txt.close()

with open(save_train_path, 'w', encoding="UTF-8") as txt:
    for text in train_save_list:
        if '\n' not in text:
            text += '\n'
        txt.writelines(text)
    txt.close()
print("finished!")