import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data.head())





data1 = pd.get_dummies(data, columns = ['whoAmI'])
data1.head()
print(data1.head())




list2 = list[data['whoAmI'].unique()]
for i in list2:
    data.loc[data['whoAmI'] == 'human', 'human'] = '1'
    data.loc[data['whoAmI'] != 'human', 'human'] = '0'
    
    data.loc[data['whoAmI'] == 'robot', 'robot'] = '1'
    data.loc[data['whoAmI'] != 'robot', 'robot'] = '0'
data.head()
print(data.head())
   








import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получаем уникальные значения из столбца 'whoAmI'
unique_values = data['whoAmI'].unique()

# Создаем новые столбцы для каждого уникального значения
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаляем исходный столбец 'whoAmI'
data.drop(columns=['whoAmI'], inplace=True)

# Выводим первые строки преобразованного DataFrame
print(data.head())



