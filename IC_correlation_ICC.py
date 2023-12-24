import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols

def calcular_icc(df, target, rater, rating):
    formula = f"Q('{rating}') ~ C(Q('{target}')) * C(Q('{rater}'))"
    modelo = ols(formula, data=df).fit()
    anova_table = sm.stats.anova_lm(modelo, typ=2)
    MSB = anova_table['sum_sq'][f'C(Q(\'{target}\'))'] / anova_table['df'][f'C(Q(\'{target}\'))']
    MSW = anova_table['sum_sq']['Residual'] / anova_table['df']['Residual']
    k = df[rater].nunique()
    icc_value = (MSB - MSW) / (MSB + (k - 1) * MSW)
    return icc_value

def __main__():
    df = pd.read_excel('C:/Users/user/Dropbox/LANEVI-CRG/LANEV-CRG-ResearchDataREPOSITORY/LAVEV/Escola Monsenhor/16-12-23/Final/Merge_final.xlsx')
    df['Subject_session'] = df['Subject_session'].replace('#00', '#01')
    tipos = df['type'].unique()
    icc_global = calcular_icc(df, 'ID', 'Subject_session', 'Reversal Intensities')
    for tipo in tipos:
        df_tipo = df[df['type'] == tipo]
        icc = calcular_icc(df_tipo, 'ID', 'Subject_session', 'Reversal Intensities')
        print(f"ICC para o tipo '{tipo}': {icc}")
    print(f"ICC Global: {icc_global}")
    
if __name__ == '__main__':
    __main__()
