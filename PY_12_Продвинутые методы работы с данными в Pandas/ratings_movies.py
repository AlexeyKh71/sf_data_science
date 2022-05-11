import pandas as pd
import re 

def get_year_release(arg):
    #находим все слова по шаблону "(DDDD)"
    candidates = re.findall(r'\(\d{4}\)', arg) 
    # проверяем число вхождений
    if len(candidates) > 0:
        #если число вхождений больше 0,
	#очищаем строку от знаков "(" и ")"
        year = candidates[0].replace('(', '')
        year = year.replace(')', '')
        return int(year)
    else:
        #если год не указан, возвращаем None
        return None
    
    
#def add_ratings_movies(df):
 #   joined['year_release'] = df.joined['title'].apply(get_year_release)
 #   print(df.joined.info())



ratings_movies = pd.read_csv('C:\Alexey\DS30\IDE\PY_12_Продвинутые методы работы с данными в Pandas\data\m_ratings_movies.csv', sep=',')
ratings_movies['year_release'] = ratings_movies['title'].apply(get_year_release)

#ratings_movies.info()
#print(100818 - 100836)

#mask = ratings_movies['year_release'] == 1999
#print(ratings_movies[mask].groupby('title')['rating'].mean().sort_values())

#mask = ratings_movies['year_release'] == 2010
#print(ratings_movies[mask].groupby('genres')['rating'].mean().sort_values())

#print(ratings_movies.groupby('userId')['genres'].nunique().sort_values(ascending=False))

#print(ratings_movies.groupby('userId')['rating'].agg(['count', 'mean']).sort_values(['count', 'mean'], ascending=[True, False])

#mask = ratings_movies['year_release'] == 2018


#grouped = ratings_movies[mask].groupby('genres')['rating'].agg(['mean', 'count'])
#print(grouped[grouped['count']>10].sort_values(    by='mean',    ascending=False))

ratings_movies['date'] = pd.to_datetime(ratings_movies['date'])
ratings_movies['year_rating'] = ratings_movies['date'].dt.year
pivot = ratings_movies.pivot_table(
    index='year_rating',
    columns='genres',
    values='rating',
    aggfunc='mean'
)
print(pivot[ 'Comedy' ])




