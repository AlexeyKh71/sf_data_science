from asyncio.windows_events import NULL
import pandas as pd

def create_companyDF(income, expenses, years):
    df = pd.DataFrame({
    'income':income,
    'expenses': expenses
})
    df.index = years
    return df

def get_profit(df, year):
    profit = None
    if year in df.index:
        profit = df.loc[year, 'income'] - df.loc[year, 'expenses']
        
    return profit

if __name__ == '__main__':
    expenses = [156, 130, 270]
    income = [478, 512, 196]
    years = [2018, 2019, 2020]
    
    scienceyou = create_companyDF(income, expenses, years)
    print(scienceyou)
    print(get_profit(scienceyou, 2020)) #-74
    print(get_profit(scienceyou, 0)) #-74
