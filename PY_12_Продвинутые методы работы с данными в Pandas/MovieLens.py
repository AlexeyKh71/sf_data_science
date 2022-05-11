import pandas as pd

#Сколько уникальных фильмов представлено в таблице movies?
def Task_12_52_53(df):
    print(df.nunique())
    
def Task_12_54(df):
    df['aYear'] = pd.to_datetime(df['date'], dayfirst=True).dt.year
    print(
        df.groupby('aYear')['aYear'].count().sort_values(ascending=False).index[0]
    )

#movies_data = pd.read_csv('C:\Alexey\DS30\IDE\PY_12_Продвинутые методы работы с данными в Pandas\data\movies.csv', sep=',')
#ratings1_data = pd.read_csv('C:\Alexey\DS30\IDE\PY_12_Продвинутые методы работы с данными в Pandas\data\m_ratings1.csv', sep=',')
dates = pd.read_csv('C:\Alexey\DS30\IDE\PY_12_Продвинутые методы работы с данными в Pandas\data\dates.csv', sep=',')

Task_12_54(dates)



