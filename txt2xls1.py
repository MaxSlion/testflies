import re
import pandas as pd
wb = open('flie2.txt','r').read()
s = re.split('[,\s]',wb)
newxs = [s[pos:pos+3] for pos in range(0,len(s),3)]
dataframe = pd.DataFrame(newxs)
print(dataframe)
dataframe.to_excel('list.xls')


