import pandas as pd
import matplotlib.pyplot as plt

def __main__():
    df = pd.read_excel('C:/Users/user/Dropbox/LANEVI-CRG/LANEV-CRG-ResearchDataREPOSITORY/LAVEV/Escola Monsenhor/16-12-23/Final/Merge_final.xlsx')
    idade = df[df['Idade No Dia do Teste'] < 18]
    idade = idade.reset_index(drop=True)
    unique_ids = idade['ID'].unique()
    data = {'ID': [], 'Idade': [], 'Idade Fracionada': []}
    for id in unique_ids:
        subset = idade[idade['ID'] == id]
        data['ID'].append(id)
        data['Idade'].append(subset['Idade No Dia do Teste'].iloc[0])
        data['Idade Fracionada'].append(subset['Idade No Dia do Teste Fracionada'].iloc[0])
    novo_df = pd.DataFrame(data)
    novo_df['Idade'].describe()
    novo_df['Idade Fracionada'].describe()

if __name__ == '__main__':
    __main__()