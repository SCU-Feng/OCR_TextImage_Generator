"""
制作id+生产年份的语料库
id:
    19位：0xxx
    22位：5xxx

年份：
    2009-2020年
"""
import random


txt_path_year = r"D:\FengZhan\text_renderer\data\elec_corpus\year_2009_2020_TimesNewRoman.txt"
txt_path_save = r"D:\FengZhan\text_renderer\data\elec_corpus\id_and_year_TimesNewRoman.txt"
txt_save = []


with open(txt_path_year, 'r', encoding="UTF-8") as year:
    year_list = year.readlines()
    length_year = len(year_list)

    for j, year_j in enumerate(year_list):
        str_last = year_j.strip()
        for i in range(2100):
            # 19
            str_pre = '0'
            for k in range(18):
                str_pre += str(random.randint(0, 9))

            str_ij = str_pre + '  ' + str_last
            txt_save.append(str_ij)
            print("{} / {} ：{} / {}".format(j, length_year, i, 2100))

    for j, year_j in enumerate(year_list):
        str_last = year_j.strip()
        for i in range(2100):
            # 22位随机数
            str_pre = '5'
            for k in range(21):
                str_pre += str(random.randint(0, 9))

            str_ij = str_pre + ' ' + str_last
            txt_save.append(str_ij)
            print("{} / {} ：{} / {}".format(j, length_year, i, 2100))

with open(txt_path_save, 'w', encoding="UTF-8") as txt:
    for text in txt_save:
        if '\n' not in text:
            text += '\n'
        txt.writelines(text)
    txt.close()

print("finished!")

