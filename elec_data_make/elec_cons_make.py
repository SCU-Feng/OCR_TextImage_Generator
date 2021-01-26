"""
制作电流规格+脉冲常数语料库
"""

elec_list = ["5(60)A",
             "10(60)A",
             "10(40)A",
             "10(100)A",
             "5(20A)",
             "20(100)A",
             "1.5(6)A",
             "20(80)A"]
cons_list = ["1200",
             "1600",
             "800",
             "3200",
             "6400"]

txt_path_save = r"D:\FengZhan\text_renderer\data\elec_corpus\elec_and_cons.txt"
txt_save = []

for elec_i in elec_list:
    for cons_i in cons_list:
        str_i = elec_i + ' ' + "220V" + ' ' + "50Hz" + ' ' + cons_i + "imp/kWh②"
        txt_save.append(str_i)

with open(txt_path_save, 'w', encoding="UTF-8") as txt:
    for text in txt_save:
        if '\n' not in text:
            text += '\n'
        txt.writelines(text)
    txt.close()

print("finished!")