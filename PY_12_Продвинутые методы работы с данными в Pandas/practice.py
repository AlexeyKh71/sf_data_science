import pandas as pd
import math as mt

#Преобразуйте столбец Date в формат datetime и выделите квартал (quarter) продажи объектов недвижимости. 
# Найдите второй по популярности квартал продажи. 
# В качестве ответа запишите число объектов, проданных в этом квартале.
def Task_12_11(melb_df):
    melb_df['Date'] = pd.to_datetime(melb_df['Date'])
    quarters = melb_df['Date'].dt.quarter
    print(quarters.value_counts().iloc[1])
    
#Преобразуйте все столбцы, в которых меньше 150 уникальных значений, в тип данных category, исключив из преобразования столбцы Date, Rooms, Bedroom, Bathroom, Car.
#В качестве ответа запишите результирующее количество столбцов, которые имеют тип данных category.    
def Task_12_12(melb_df):
    cols_to_exclude = ['Date', 'Rooms', 'Bedroom', 'Bathroom', 'Car'] 
    max_unique_count = 150 
    
    for col in melb_df.columns: 
        if melb_df[col].nunique() < max_unique_count and col not in cols_to_exclude: 
            melb_df[col] = melb_df[col].astype('category')
            
    print(melb_df.info())

#Произведите сортировку столбца AreaRatio по убыванию. При этом индексы полученной таблицы замените на новые. 
#Какое значение площади здания находится в строке 1558? Ответ округлите до целого числа.
def Task_12_22(melb_df):
    print(
            int(melb_df.sort_values(
            by='AreaRatio', 
            ignore_index=True,
            ascending=False
            ).loc[1558, 'BuildingArea'])
    )
#Найдите таунхаусы (Type) с количеством жилых комнат (Rooms) больше 2. 
# Отсортируйте полученную таблицу сначала по возрастанию числа комнат, а затем по убыванию средней площади комнат (MeanRoomsSquare). 
# Индексы таблицы замените на новые. Какая цена будет у объекта в строке 18? Ответ запишите в виде целого числа.
def Task_12_23(melb_df):
    mask1 = melb_df['Type'] == 'townhouse'
    mask2 = melb_df['Rooms'] > 2
    print(
            int(melb_df[mask1&mask2].sort_values(
            by=['Rooms', 'MeanRoomsSquare'],
            ascending=[True, False],
            ignore_index=True
            ).loc[18, 'Price'])
    )


#Сгруппируйте данные по признаку количества комнат и найдите среднюю цену объектов недвижимости в каждой группе.
#В качестве ответа запишите количество комнат, для которых средняя цена наибольшая.
def Task_12_31(melb_df):
    print(
        melb_df.groupby('Rooms')['Price'].mean().sort_values(ascending=False)
    )
    
#Какой регион имеет наименьшую протяжённость по географической широте (Lattitude)?
#Для ответа на этот вопрос рассчитайте стандартное отклонение широты для каждого региона.
#В качестве ответа запишите название этого региона.
def Task_12_32(melb_df):
    print(
        melb_df.groupby('Regionname')['Lattitude'].std().sort_values()
    )
#Какая риелторская компания (SellerG) имеет наименьшую общую выручку за период с 1 мая по 1 сентября (включительно) 2017 года?
#Для ответа на этот вопрос рассчитайте сумму продаж (Price) каждой компании в заданный период.
#Не забудьте перевести даты в формат datetime.
def Task_12_33(melb_df):
    date1 = pd.to_datetime('2017-05-01')
    date2 = pd.to_datetime('2017-09-01')
    melb_df['NewDate'] = pd.to_datetime(melb_df['Date'], dayfirst=True)
    mask = (date1 <= melb_df['NewDate']) & (melb_df['NewDate']<= date2)
    print(
        melb_df[mask].groupby('SellerG')['Price'].sum().sort_values(ascending=True)
    )
#Составьте сводную таблицу, которая показывает зависимость медианной площади (BuildingArea) здания 
# от типа объекта недвижимости (Type) и количества жилых комнат в доме (Rooms). 
# Для какой комбинации признаков площадь здания наибольшая?
#В качестве ответа запишите эту комбинацию (тип здания, число комнат) через запятую, без пробелов. house,7
def Task_12_42(melb_df):
    pivot = melb_df.pivot_table(
        values='BuildingArea',
        index='Type',
        columns='Rooms',
        aggfunc='median',
        fill_value=0
    )
    print(pivot)        

#Составьте сводную таблицу, которая показывает зависимость средней цены объекта недвижимости (Price) от риелторского агентства (SellerG) и типа здания (Type).
#Во вновь созданной таблице найдите агентство, у которого средняя цена для зданий типа unit максимальна. В качестве ответа запишите название этого агентства.    
def Task_12_43(melb_df):
    pivot = melb_df.pivot_table(
        values='Price',
        index='SellerG',
        columns='Type',
        aggfunc='mean',
    )
    max_unit_price = pivot['unit'].max()
    print(pivot[pivot['unit'] == max_unit_price].index[0]) 
    
def concat_users_files(path):
    """
    Вам необходимо написать функцию concat_user_files(path), параметром которой является path - путь до директории. 
    Функция должна объединить информацию из предоставленных вам файлов в один DataFrame и вернуть его. 
    Не забудьте обновить индексы результирующей таблицы после объединения.
    Учтите тот момент, что в результате объединения могут возникнуть дубликаты, от которых необходимо будет избавиться. 
    """
    data = pd.DataFrame()
    file_names = os.listdir(path)
    file_names.sort()
    for file in file_names:
        tmp_data = pd.read_csv(path + '/' + file)
        data = pd.concat([data, tmp_data], axis=0, ignore_index=True)
    data = data.drop_duplicates()
    return data

def task_12_63():
    if __name__ == '__main__':
        data = concat_users_files('./Root/users/')
        print(data)


def task_12_74():
    a = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [103, 214, 124], 'C': [1, 4, 2]})
    b = pd.DataFrame({'V': ['d', 'b', 'c'], 'U': [1393.7, 9382.2, 1904.5], 'C': [1, 3, 2]})      
    
    #print(a.join(b, how='inner', r_suffix='_r'))
    #print(a.merge(b, how='left', on='C'))
    #print(a.merge(b, how='inner', right_on='A', left_on='V'))
    #print(b.join(a.set_index('C'), how='right', on='C'))
    print(a.merge(b, how='right', on='C'))
    #print(a.merge(b, how='inner', on='C'))
    

#Сформируйте DataFrame merged, в котором в результате объединения
#purchase_df и items_df останутся модели, которые учтены на складе и имели продажи. 
#Найдите из таблицы merged суммарную выручку, которую можно было бы получить 
#от продажи всех товаров, которые есть на складе. 
#Результат занесите в переменную income.

def task_12_75():
    items_df = pd.DataFrame({
    'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 100132, 312394], 
    'vendor': ['Samsung', 'LG', 'Apple', 'Apple', 'LG', 'Apple', 'Samsung', 'Samsung', 'LG', 'ZTE'],
    'stock_count': [54, 33, 122, 18, 102, 43, 77, 143, 60, 19]
    })

    purchase_df = pd.DataFrame({
        'purchase_id': [101, 101, 101, 112, 121, 145, 145, 145, 145, 221],
        'item_id': [417283, 849734, 132223, 573943, 19475, 3294095, 382043, 302948, 103845, 100132], 
        'price': [13900, 5330, 38200, 49990, 9890, 33000, 67500, 34500, 89900, 11400]
    })

    merged = items_df.merge(purchase_df, how='inner', on='item_id')
    income = (merged['price'] * merged['stock_count']).sum()
    



melb_data = pd.read_csv('C:\Alexey\DS30\IDE\PY_12_Продвинутые методы работы с данными в Pandas\data\melb_data_fe.csv', sep=',')
task_12_74()