import pandas as pd
import math as mt

def getdfcopy(df):
    return df.copy()

def do_drop_1(df, column_name):
    return df.drop(['index', column_name], axis=1)

def do_drop_inplace(df, column_name):
    return df.drop(['index', column_name], axis=1, inplace = True)

def delete_columns(df, col=[]):
    for cc in col:
        if cc not in df.columns:
            return None
            
    return df.drop(col, axis=1)

def countries_df_ps():
    countries_df = pd.DataFrame({
        'country': ['Англия', 'Канада', 'США', 'Россия', 'Украина', 'Беларусь', 'Казахстан'],
        'population': [56.29, 38.05, 322.28, 146.24, 45.5, 9.5, 17.04],
        'square': [133396, 9984670, 9826630, 17125191, 603628, 207600, 2724902]
    })

    countries_df['density'] = countries_df['population'] / countries_df['square'] * 1e6
    print(round(countries_df['density'].mean(), 2))

def get_weekend(weekday):
    if weekday == 5 or weekday == 6:
        return 1
    else: 
        return 0
        
def weekend_count(melb_df):
    #melb_df['WeekdaySale'] = pd.to_datetime(melb_df['Date'], format="%d/%m/%y", errors='coerce').dt.dayofweek
    #melb_df['NewDate'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
    melb_df['WeekdaySale'] = pd.to_datetime(melb_df['Date'], dayfirst=True).dt.dayofweek
    weekend_count = melb_df[(melb_df['WeekdaySale'] == 5) | (melb_df['WeekdaySale'] == 6)].shape[0]
    print(weekend_count)
    
def weekend_price_avg(melb_df):
    melb_df['WeekdaySale'] = pd.to_datetime(melb_df['Date'], dayfirst=True).dt.dayofweek
    melb_df['Weekend'] = melb_df['WeekdaySale'].apply(get_weekend)
    print(round(melb_df[melb_df['Weekend']==1]['Price'].mean(), 2))
    
def UIF_1():
    df = pd.read_csv('http://bit.ly/uforeports')
    df['Time'] = pd.to_datetime(df.Time)
    print(df['Time'].dt.year.mode()[0])
    
def UIF_2():
    df = pd.read_csv('http://bit.ly/uforeports')
    df['Date'] = pd.to_datetime(df['Time'], dayfirst=False).dt.date
    print(df[df['State']=='NV']['Date'].diff().dt.days.mean())
    

def popular_seler(melb_df):
    popular_seler = melb_df['SellerG'].value_counts().nlargest(49).index
    # заменяем значения улиц, не попавших в список популярных на строку 'other'
    melb_df['SellerG'] = melb_df['SellerG'].apply(lambda x: x if x in popular_seler else 'other') 

    a = melb_df[melb_df['SellerG'] == 'Nelson']['Price'].min() 
    b = melb_df[melb_df['SellerG'] == 'other']['Price'].min() 
    print(round(a/b, 1))

def get_experience(arg):
    month_key_words = ['месяц', 'месяцев', 'месяца']
    year_key_words = ['год', 'лет', 'года']
    args_splited = arg.split(' ')
    month = 0
    year = 0
    for i in range(len(args_splited)):
        if args_splited[i] in month_key_words:
            month = args_splited[i-1]
        if args_splited[i] in year_key_words:
            year = args_splited[i-1]
    return int(year)*12 + int(month)

def get_experience_main():
    if __name__ == '__main__':
        experience_col = pd.Series([
            'Опыт работы 8 лет 3 месяца',
            'Опыт работы 3 года 5 месяцев',
            'Опыт работы 1 год 9 месяцев',
            'Опыт работы 3 месяца',
            'Опыт работы 6 лет'
            ])
        experience_month = experience_col.apply(get_experience)
        print(experience_month)            

def to_category(melb_df):
    cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] # список столбцов, которые мы не берём во внимание
    max_unique_count = 150 # задаём максимальное число уникальных категорий
    for col in melb_df.columns: # цикл по именам столбцов
        if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude: # проверяем условие
            melb_df[col] = melb_df[col].astype('category') # преобразуем тип столбца
    print(melb_df.info())
    
def to_new_category(melb_df): 
    melb_df['Type'] = melb_df['Type'].cat.rename_categories({
    'u': 'unit',
    't': 'townhouse',
    'h': 'house'
    })   
    melb_df['Type'] = melb_df['Type'].cat.add_categories('flat')
    new_houses_types = pd.Series(['unit', 'house', 'flat', 'flat', 'house'])
    new_houses_types = new_houses_types.astype(melb_df['Type'].dtype)
    print(new_houses_types)        

def popular_Suburb_to_category(melb_df):
    print(melb_df.info())
    popular_Suburb = melb_df['Suburb'].value_counts().nlargest(199).index
    # заменяем значения улиц, не попавших в список популярных на строку 'other'
    melb_df['Suburb'] = melb_df['Suburb'].apply(lambda x: x if x in popular_Suburb else 'other') 
    melb_df['Suburb'] = melb_df['Suburb'].astype('category') # преобразуем тип столбца
    print(melb_df.info())


def bikes_usertype_max(data):
    mode_usertype = data['usertype'].mode()[0]
    count_mode_user = data[data['usertype'] == mode_usertype].shape[0]
    print(round(count_mode_user / data.shape[0], 2))

def bikes_male_or_female(data):
    male_count = data[data['gender'] == 1].shape[0]
    female_count = data[data['gender'] == 0].shape[0]
    print(max([male_count, female_count]))

def get_time_of_day(time):
    if 0 <= time <= 6:
        return 'night'
    elif 6 < time <= 12:
        return 'morning'
    elif 12 < time <= 18:
        return 'day'
    elif 18 < time <= 23:
        return 'evening'
    else:
        return 'else'


#melb_data = pd.read_csv('C:\Alexey\DS30\IDE\PY_11_Базовые приемы работы с данными в Pandas\data\melb_data_ps.csv', sep=',')

citibike_data = pd.read_csv('C:\Alexey\DS30\IDE\PY_11_Базовые приемы работы с данными в Pandas\data\citibike-tripdata.csv', sep=',')

#Найдите идентификатор самой популярной стартовой стоянки. Запишите идентификатор в виде целого числа.
#print(citibike_data['start station id'].mode()[0])


#Велосипед с каким идентификатором является самым популярным?
#print(citibike_data['bikeid'].mode()[0])

#Какой тип клиентов (столбец usertype) является преобладающим — Subscriber или Customer? В качестве ответа запишите долю клиентов преобладающего типа среди общего количества клиентов.
#bikes_usertype_max(citibike_data)

#Кто больше занимается велоспортом — мужчины или женщины? В ответ запишите число поездок для той группы, у которой их больше.
#bikes_male_or_female(citibike_data)

#В наших данных присутствуют столбцы, которые дублируют информацию друг о друге: это столбцы с идентификатором и названием стартовой и конечной стоянки. Удалите признаки идентификаторов стоянок. Сколько столбцов осталось?
#citibike_data.drop(['start station id', 'end station id'], axis=1, inplace=True)
#print(citibike_data.shape[1])

#Замените признак birth year на более понятный признак возраста клиента age. Годом отсчёта возраста выберите 2018 год. Столбец birth year удалите из таблицы. Сколько поездок совершено клиентами старше 60 лет?
#citibike_data['age'] = 2018 - citibike_data['birth year']
#citibike_data.drop(['birth year'], axis=1, inplace=True)
#print(citibike_data[citibike_data['age'] > 60].shape[0])

#Создайте признак длительности поездки trip duration. Для этого вычислите интервал времени между временем окончания поездки (stoptime) и временем её начала (starttime) в секундах. Рассчитайте среднее значение по новому столбцу — среднюю длительность поездки, а затем переведите её в секунды. Ответ округлите до целого.
#Для того чтобы преобразовать временной интервал timedelta в секунды, используется атрибут seconds (в datetime атрибут был second — в единственном числе).
citibike_data['starttime'] = pd.to_datetime(citibike_data['starttime'], dayfirst=True)
citibike_data['stoptime'] = pd.to_datetime(citibike_data['stoptime'], dayfirst=True)
citibike_data['trip duration'] = (citibike_data['stoptime'] - citibike_data['starttime']).dt.seconds
print(citibike_data['trip duration'].mean())

#Создайте «признак-мигалку» weekend, который равен 1, если поездка начиналась в выходной день (суббота или воскресенье), и 0 — в противном случае. Выясните, сколько поездок начиналось в выходные.
#weekday = pd.to_datetime(citibike_data['starttime'], dayfirst=True).dt.dayofweek
#citibike_data['weekend'] = weekday.apply(lambda x: 1 if x ==5 or x == 6 else 0)
#print(citibike_data['weekend'].sum())

#Создайте признак времени суток поездки time_of_day. Время суток будем определять из часа начала поездки. Условимся, что:
#поездка совершается ночью (night), если её час приходится на интервал от 0 (включительно) до 6 (включительно) часов;
#поездка совершается утром (morning), если её час приходится на интервал от 6 (не включительно) до 12 (включительно) часов;
#поездка совершается днём (day), если её час приходится на интервал от 12 (не включительно) до 18 (включительно) часов;
#поездка совершается вечером (evening), если её час приходится на интервал от 18 (не включительно) до 23 часов (включительно).
#Во сколько раз количество поездок, совершённых днём, больше, чем количество поездок, совёршенных ночью, за представленный в данных период времени? Ответ округлите до целых.    
#citibike_data['time_of_day'] = pd.to_datetime(citibike_data['starttime'], dayfirst=True).dt.hour.apply(get_time_of_day)
#a = citibike_data[citibike_data['time_of_day'] == 'day'].shape[0]
#b = citibike_data[citibike_data['time_of_day'] == 'night'].shape[0]
#print(round(a / b))

