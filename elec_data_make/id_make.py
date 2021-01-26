"""
制作id语料库
id:
    19位：0xxx
    22位：5xxx
"""
import random

txt_path_save = r"D:\FengZhan\text_renderer\data\elec_corpus\id.txt"
txt_save = []


for i in range(25000):
    # 19
    str_pre = '0'
    for k in range(18):
        str_pre += str(random.randint(0, 9))
    txt_save.append(str_pre)
    print("{}".format(i))
for i in range(25000):
    # 22
    str_pre = '5'
    for k in range(21):
        str_pre += str(random.randint(0, 9))
    txt_save.append(str_pre)
    print("{}".format(i))


with open(txt_path_save, 'w', encoding="UTF-8") as txt:
    for text in txt_save:
        if '\n' not in text:
            text += '\n'
        txt.writelines(text)
    txt.close()

print("finished!")

