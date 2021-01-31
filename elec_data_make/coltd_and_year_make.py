"""
制作公司名称+生产年份的语料库
"""

txt_path_coltd = r"..\data\elec_corpus\coltd_106_heiti.txt"
txt_path_year = r"..\data\elec_corpus\year_2009_2020_heiti.txt"
txt_path_save = r"..\data\elec_corpus\coltd_and_year.txt"
txt_save = []

with open(txt_path_coltd, 'r', encoding="UTF-8") as coltd:
    coltd_list = coltd.readlines()
    length_coltd = len(coltd_list)

    with open(txt_path_year, 'r', encoding="UTF-8") as year:
        year_list = year.readlines()
        length_year = len(year_list)

        for i, coltd_i in enumerate(coltd_list):
            str_pre = coltd_i.strip()
            print("*"*30)
            print("{} / {}".format(i, length_coltd))
            print("now coltd is {}".format(coltd_i))

            for j, year_j in enumerate(year_list):
                str_last = year_j.strip()
                str_ij = str_pre + '  ' + str_last
                txt_save.append(str_ij)
                print("{} / {}".format(j, length_year))



with open(txt_path_save, 'w', encoding="UTF-8") as txt:
    for text in txt_save:
        if '\n' not in text:
            text += '\n'
        txt.writelines(text)
    txt.close()

print("finished!")

