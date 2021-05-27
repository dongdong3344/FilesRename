import pandas as pd
import os

class HandleData():

    def __init__(self):
        self.file_path = 'Data.xlsx'

    def combine_col(self,includeType=False):

        df = pd.read_excel(self.file_path,engine= 'openpyxl')
        df = df.fillna('')
        df['Keyword'] = df['Keyword'].apply(lambda i: str(i).lower())
        cols = df.columns.tolist()[1:]
        if includeType:  # True, 直接拼接
            df['Combined'] = df[cols].apply(lambda x: '-'.join(x), axis=1)
        else:
            for i,val in enumerate(df['Standard'].eq('').tolist()):
                if val:  # Standard不存在，报告类型存在
                    df.loc[i, 'Combined'] = df.loc[i, 'Region'] + '-' + df.loc[i, 'Type'] + '-' + df.loc[i, 'Version'] + '-' + df.loc[i, 'Suffix']
                else:
                    df.loc[i, 'Combined'] = df.loc[i, 'Region'] + '-' + df.loc[i, 'Standard'] + '-' + df.loc[i, 'Version'] + '-' + df.loc[i, 'Suffix']
        df['Combined'] = df['Combined'].apply(lambda x: '-'.join(i for i in x.split('-') if i))  # 去掉多余‘-’,只保留一个
        return df


if __name__ == '__main__':

    h = HandleData()
    df = h.combine_col(includeType=False)
    print(df)
    print(df[df.duplicated('Combined',keep=False)])