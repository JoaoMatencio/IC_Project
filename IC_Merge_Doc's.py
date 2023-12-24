import pandas as pd
import os as os
import openpyxl

def main():
    path = 'C:/Users/user/Dropbox/LANEVI-CRG/LANEV-CRG-ResearchDataREPOSITORY/LAVEV/Escola Monsenhor/16-12-23/Doc_17_12_23/'
    df = pd.read_excel(f'{path}Subject_Questionaire_Download_17_12_23.xlsx',sheet_name='Respostas ao formulário 1')
    df2 = pd.read_excel(f'{path}Experimental_Record_Download_17_12_23.xlsx',sheet_name="Crianças")
    df2 = df2.dropna(subset=['Nome do arquivo'])
    df2 = df2.dropna(subset=['ID'])
    df3 = pd.merge(df, df2, on='ID')
    df3.to_excel(f'{path}Subject_Questionaire_Experimental_Record_Merge.xlsx')

if __name__ == '__main__':
    main()