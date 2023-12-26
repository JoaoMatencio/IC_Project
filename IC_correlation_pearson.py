import pandas as pd
import numpy as np

def __main__():
    df = pd.read_excel('C:/Users/user/Dropbox/LANEVI-CRG/LANEV-CRG-ResearchDataREPOSITORY/LAVEV/Escola Monsenhor/16-12-23/Final/Merge_final.xlsx')
    df_t = df[(df['Subject_session'] == '#01') | (df['Subject_session'] == '#00')]
    df_r = df[df['Subject_session'] == '#02']
    unique_ids = df['ID'].unique()
    unique_types = df['type'].unique()
    correlations = {}
    dfs_tests = []
    df_retests = []
    for unique_type in unique_types:
        for id in unique_ids:
            data_test = df_t[(df_t['ID'] == id) & (df_t['type'] == unique_type)]
            data_retest = df_r[(df_r['ID'] == id) & (df_r['type'] == unique_type)]
            data_test = data_test.reset_index(drop=True)
            data_retest = data_retest.reset_index(drop=True)
            value_test = data_test['Reversal Intensities'].values
            teste_mean = value_test[-5:].mean()
            value_retest = data_retest['Reversal Intensities'].values
            retest_mean = value_retest[-5:].mean()
            if len(value_test) == 10 and len(value_retest) == 10:
                dfs_tests.append(teste_mean)
                df_retests.append(retest_mean)
        correlation = np.corrcoef(dfs_tests, df_retests)[0, 1]
        print(f'{unique_type}: {correlation}')  
            
if __name__ == '__main__':
    __main__()
