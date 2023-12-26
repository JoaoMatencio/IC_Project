import pandas as pd
import pingouin as pg

def __main__():
    df = pd.read_excel('C:/Users/user/Dropbox/LANEVI-CRG/LANEV-CRG-ResearchDataREPOSITORY/LAVEV/Escola Monsenhor/16-12-23/Final/Merge_final.xlsx')
    df['Subject_session'] = df['Subject_session'].replace('#00', '1')
    df['Subject_session'] = df['Subject_session'].replace('#01', '1')
    df['Subject_session'] = df['Subject_session'].replace('#02', '2')
    df = df[df['Reversal rank'] > 5]
    ids_validos = df[df['Subject_session'].isin(['1', '2'])].groupby('ID').filter(lambda x: len(x['Subject_session'].unique()) == 2)['ID'].unique()
    df = df[df['ID'].isin(ids_validos)].reset_index(drop=True)
    grouped = df.groupby(['ID', 'type', 'Subject_session'])['Reversal Intensities'].mean().reset_index()
    grouped = grouped.reset_index(drop=True)
    tipos = grouped['type'].unique()
    for tipo in tipos:
        df_tipo = grouped[grouped['type'] == tipo]
        df_tipo = df_tipo.reset_index(drop=True)
        icc = pg.intraclass_corr(data=df_tipo, targets='ID', raters='Subject_session', ratings='Reversal Intensities')
        print(f"ICC para o tipo '{tipo}':\n{icc}\n")
    
if __name__ == '__main__':
    __main__()
