import pandas as pd

orders_df = pd.read_csv('C:\Alexey\DS30\IDE\PY_12_Продвинутые методы работы с данными в Pandas\data\orders.csv', sep=';')
product_df = pd.read_csv('C:\Alexey\DS30\IDE\PY_12_Продвинутые методы работы с данными в Pandas\data\products.csv', sep=';')


orders_products = orders_df.merge(
    product_df, 
    left_on='ID товара',
    right_on='Product_ID',
    how='left')

orders_products['Profit'] = orders_products['Price'] * orders_products['Количество'] 
print(orders_products[orders_products['Оплачен'] == 'Да'].groupby('ID Покупателя')['Profit'].sum().sort_values(ascending=False))
