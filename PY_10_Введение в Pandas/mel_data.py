import pandas as pd

students_performance = pd.read_csv('C:\Alexey\DS30\IDE\PY_10_Введение в Pandas\data\students_performance.csv', sep=',')

#print(students_performance['race/ethnicity'].value_counts())
print(students_performance[students_performance['race/ethnicity']=='group A']['writing score'].median() - students_performance[students_performance['race/ethnicity']=='group C']['writing score'].mean())
