import pandas as pd
import os as os
import openpyxl

def main():
    path = 'C:/Users/user/Dropbox/LANEVI-CRG/LANEV-CRG-ResearchDataREPOSITORY/LAVEV/Escola Monsenhor/16-12-23/Final_Reversal_56/'
    dfs = []
    path_save = path + 'Merge_Date_Reversal.xlsx'
    file_name = [i for i in os.listdir(path)]
    for i in file_name:
        df = pd.read_excel(path + i)
        dfs.append(df)
    df = pd.concat(dfs, ignore_index=True)
    x = df[(df['Subject_session'] == '#01') | (df['Subject_session'] == '#00')]
    df
    df.to_excel(path_save,index=False)

if __name__ == '__main__':
    main()
