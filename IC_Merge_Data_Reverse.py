import pandas as pd
import os as os
import openpyxl

def create_df(path,line):
    df = pd.read_excel(path,sheet_name=line)
    x = path.split('/')
    z = x[10]
    t = z.split('_')
    t_new = t[3] +'_'+t[4]
    dados = {
        'Subject_name': [t[0], t[0], t[0],t[0], t[0], t[0],t[0],t[0],t[0],t[0]],
        'Subject_id': ['IDc', 'IDc', 'IDc','IDc', 'IDc', 'IDc','IDc','IDc','IDc','IDc'],
        'Subject_session': [t[2], t[2], t[2],t[2], t[2], t[2],t[2],t[2],t[2],t[2]],
        'expName': [t_new, t_new, t_new,t_new, t_new, t_new,t_new,t_new,t_new,t_new],
        'Reversal Intensities': [df['Reversal Intensities'][0], df['Reversal Intensities'][1], df['Reversal Intensities'][2],df['Reversal Intensities'][3], df['Reversal Intensities'][4], df['Reversal Intensities'][5],df['Reversal Intensities'][6],df['Reversal Intensities'][7],df['Reversal Intensities'][8],df['Reversal Intensities'][9]],
        'Reversal Indices': [df['Reversal Indices'][0], df['Reversal Indices'][1], df['Reversal Indices'][2],df['Reversal Indices'][3], df['Reversal Indices'][4], df['Reversal Indices'][5],df['Reversal Indices'][6],df['Reversal Indices'][7],df['Reversal Indices'][8],df['Reversal Indices'][9]],
        'Reversal rank': ['1','2','3','4','5','6','7','8','9','10']
            }
    dados = pd.DataFrame(dados)
    return dados

def main():
    line_l_01 = 'lowContrast_size01'
    line_l_10 = 'lowContrast_size10'
    line_h_01 = 'highContrast_size01'
    line_h_10 = 'highContrast_size10'
    path = 'C:/Users/user/Dropbox/LANEVI-CRG/LANEV-CRG-ResearchDataREPOSITORY/LAVEV/Escola Monsenhor/16-12-23/RawData_Clean_56/'
    path_save = 'C:/Users/user/Dropbox/LANEVI-CRG/LANEV-CRG-ResearchDataREPOSITORY/LAVEV/Escola Monsenhor/16-12-23/Final_Reversal_56/'
    if not os.path.exists(path_save):
        os.makedirs(path_save)
    for i in os.listdir(path):
        df1 = create_df(f'{path}{i}',line_l_01)
        df2 = create_df(f'{path}{i}',line_l_10)
        df3 = create_df(f'{path}{i}',line_h_01)
        df4 = create_df(f'{path}{i}',line_h_10)
        df1['type'] = line_l_01
        df2['type'] = line_l_10
        df3['type'] = line_h_01
        df4['type'] = line_h_10
        df5 = pd.concat([df1,df2,df3,df4])
        df5['Nome do arquivo'] = f'{i}'
        df5.to_excel(f'{path_save}{i}',index=False)

if __name__ == '__main__':
    main()