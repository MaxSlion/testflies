import os
import re
import xlwt
import pandas as pd

File_Name = []
Save_Xls = []
def file_name (file_dir):
    for files in os.listdir(file_dir):
        if os.path.splitext(files)[1] == '.txt':
            File_Name.append(files)
            Save_Xls.append(os.path.splitext(files)[0] + '.xls')
file_name(".")

for i in range(len(File_Name)):
    wb = open(File_Name[i],'r').read()
    s = re.split('[,\s]',wb)
    newxs = [s[pos:pos+3] for pos in range(0,len(s),3)]
    dataframe = pd.DataFrame(newxs)
    print(dataframe)
    dataframe.to_excel(Save_Xls[i])
