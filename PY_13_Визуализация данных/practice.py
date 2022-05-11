import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def video_games_visual():
    vg_data = pd.read_csv('C:\Alexey\DS30\IDE\PY_13_Визуализация данных\data\Video_Games_Sales_as_at_22_Dec_2016.csv')
    dinamic_by_region = vg_data[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Year_of_Release']].groupby('Year_of_Release').sum()
    
    fig = plt.figure(figsize=(12, 6))
    lineplot = sns.lineplot(data=dinamic_by_region)
    lineplot.set_title('Динамика продаж видеоигр', fontsize=16)
    lineplot.set_xlabel('Год выпуска')
    lineplot.set_ylabel('Суммарный объём продаж')
    
    plt.show()
    
def Melb_data_visual():

    melb_data = pd.read_csv('C:\Alexey\DS30\IDE\PY_13_Визуализация данных\data\melb_data.csv')

    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))
    plt.subplots_adjust(hspace=.0)

    histplot1 = sns.histplot(
        data=melb_data, 
        x='Price', 
        bins=30,
        ax=axes[0],
    )
    histplot1.set_title('Распределение стоимости недвижимости в Мельбурне', fontsize=16)
    histplot1.set_xlabel('Цена объекта (млн. австралийских долларов)')
    histplot1.set_ylabel('Число объектов')

    histplot2 = sns.histplot(
        data=melb_data,
        x='Price',
        y='Type',
        bins=30,
        color='green',
        ax=axes[1]
    )
    histplot2.set_xlabel('Цена объекта (млн. австралийских долларов)')
    histplot2.set_ylabel('Тип объекта')
    plt.show()

def covid_data():
    covid_data = pd.read_csv('C:\Alexey\DS30\IDE\PY_13_Визуализация данных\data\covid_data.csv', sep=',')
    covid_data = covid_data.groupby(['date', 'country'], as_index=False)[['confirmed', 'deaths', 'recovered']].sum()
    covid_data['date'] = pd.to_datetime(covid_data['date']) 
    covid_data['active'] = covid_data['confirmed'] - covid_data['deaths'] - covid_data['recovered'] 
    covid_data = covid_data.sort_values(by=['country', 'date'])
    covid_data['daily_confirmed'] = covid_data.groupby('country')['confirmed'].diff()
    covid_data['daily_deaths'] = covid_data.groupby('country')['deaths'].diff()
    covid_data['daily_recovered'] = covid_data.groupby('country')['recovered'].diff()
    
    vaccinations_data = pd.read_csv('C:\Alexey\DS30\IDE\PY_13_Визуализация данных\data\country_vaccinations.csv',  sep=',')
    vaccinations_data = vaccinations_data[ 
                                            ['country', 'date', 'total_vaccinations', 'people_vaccinated', 
                                             'people_vaccinated_per_hundred', 'people_fully_vaccinated', 'people_fully_vaccinated_per_hundred',
                                            'daily_vaccinations', 'vaccines']
                                        ]
    vaccinations_data['date'] = pd.to_datetime(vaccinations_data['date'])
    
    covid_df = covid_data.merge(vaccinations_data, on=['date', 'country'], how='left')

    covid_df['death_rate'] = covid_df['deaths'] / covid_df['confirmed'] * 100
    covid_df['recover_rate'] = covid_df['recovered'] / covid_df['confirmed'] * 100
    
    
    #print('Число строк: ', covid_df.shape[0])
    #print('Число столбцов: ', covid_df.shape[1])
    #print(covid_data['date'].max(), covid_data['date'].min(), vaccinations_data['date'].min(),'-',vaccinations_data['date'].max())
    #print(round(covid_df[covid_df['country'] == 'United States']['death_rate'].max(), 2))
    #print(round(covid_df[covid_df['country'] == 'Russia']['recover_rate'].mean(), 2))
    #covid_df.groupby(['country'])['total_vaccinations'].last().nsmallest(5).plot(kind='bar')
    #plt.show()
    
    covid_df.to_clipboard() 
    return covid_df


    
    

covid_data()

#video_games_visual()
#Melb_data_visual()

