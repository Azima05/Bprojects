import pandas as pd
import numpy as np
#2
months_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
months_index = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
month_series = pd.Series(months_data, index=months_index)
print("Months Series:")
print(month_series)
print()
#3
batch_data = {'MatMIE': 45, 'Mat DAIS': 30, 'COMIE': 50, 'COMEC': 40}
batch_series = pd.Series(batch_data)
print("Batch Groups Series:")
print(batch_series)
print()

#4
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print("Exam DataFrame:")
print(df)
print()

#5
attempts_greater_than_2 = df[df['attempts'] > 2]
print("Number of attempts in the examination is greater than 2:")
print(attempts_greater_than_2)
