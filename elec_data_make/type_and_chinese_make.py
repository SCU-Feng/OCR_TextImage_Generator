"""
制作电表型号+汉语后缀的语料库
"""

txt_path_type = r"..\data\elec_corpus\type_83_TimesNewRoman.txt"
txt_path_save = r"..\data\elec_corpus\type_and_chinese_heiti.txt"
txt_save = []

with open(txt_path_type, 'r', encoding="UTF-8") as type:
    type_list = type.readlines()
    length_type = len(type_list)

    for i, type_i in enumerate(type_list):
        str_pre = type_i.strip()

        str_1 = str_pre + '  ' + "单相费控智能电能表"
        str_2 = str_pre + '  ' + "型单相费控智能电能表"
        str_3 = str_pre + '型' + ' ' + "单相费控智能电能表"
        txt_save.append(str_1)
        txt_save.append(str_2)
        txt_save.append(str_3)


with open(txt_path_save, 'w', encoding="UTF-8") as txt:
    for text in txt_save:
        if '\n' not in text:
            text += '\n'
        txt.writelines(text)
    txt.close()

print("finished!")

