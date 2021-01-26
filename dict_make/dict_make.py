import pandas as pd

excel_path = r"D:\backup\Github\OCR_ElectricityMeter\dataset\dictionary\coltd_total.xlsx"
txt_path = r"D:\backup\Github\OCR_ElectricityMeter\dataset\dictionary\char_std_253.txt"
new_txt_path = r"D:\backup\Github\OCR_ElectricityMeter\dataset\dictionary\char_new2.txt"

coltd_ori = pd.read_excel(excel_path, header=None)
coltd_list = coltd_ori.loc[:, 0].values.tolist()
length = len(coltd_list)

label = open(txt_path, encoding="UTF-8")
label_list = label.readlines()

for i, coltd_i in enumerate(coltd_list):
    print("*"*30)
    print("{:0>5d} / {:0>5d}".format(i, length))
    print("now coltd is : ", coltd_i)
    for coltd_ij in coltd_i:
        if '\n' not in coltd_ij:
            str_temp = coltd_ij + '\n'
        else:
            str_temp = coltd_ij

        if str_temp not in label_list:
            label_list.append(str_temp)

print("compare done!")
print("*"*50)

print("write start!")
with open(new_txt_path, "w+", encoding="UTF-8") as fo:
    for str_i in label_list:
        if '\n' not in str_i:
            str_i = str_i + '\n'

        fo.writelines(str_i)


print("finished")