import pandas as pd
import numpy as np

def __main__():
    df = pd.read_excel('C:/Users/user/Dropbox/LANEVI-CRG/LANEV-CRG-ResearchDataREPOSITORY/LAVEV/Escola Monsenhor/16-12-23/Final/Merge_final.xlsx')
    df_test = df[(df['Subject_session'] == '#01') | (df['Subject_session'] == '#00')]
    df_retest = df[df['Subject_session'] == '#02']
    unique_ids = df['ID'].unique()
    unique_types = df['type'].unique()
    correlations = {}
    correlations_by_type = {ut: [] for ut in unique_types}
    for id in unique_ids:
        for unique_type in unique_types:
            data_test_2 = df_test[(df_test['ID'] == id) & (df_test['type'] == unique_type)]
            data_retest_2 = df_retest[(df_retest['ID'] == id) & (df_retest['type'] == unique_type)]
            data_test_2 = data_test_2.reset_index(drop=True)
            data_retest_2 = data_retest_2.reset_index(drop=True)
            if len(data_test_2) == len(data_retest_2):
                correlation = data_test_2['Reversal Intensities'].corr(data_retest_2['Reversal Intensities'])
                correlations[f'{id} {unique_type}'] = correlation
                correlations_by_type[unique_type].append(correlation)
            else:
                print(f"Tamanhos inconsistentes para ID {id} e tipo {unique_type}")
    for key, corr in correlations.items():
        print(f"{key}: Correlação = {corr}")
    for unique_type in unique_types:
        average_correlation = np.mean(correlations_by_type[unique_type])
        print(f"Média de Correlação para o tipo '{unique_type}': {average_correlation}")
    all_correlations = np.nanmean(list(correlations.values()))
    print(f"Média Global de Correlações: {all_correlations}")
    
if __name__ == '__main__':
    __main__()
