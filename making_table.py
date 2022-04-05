import pandas as pd
data = {'Name': ['Imran','Shimanto','Prince','Niloy','Ganster'], 'Salary': [55000,45000,36000,29057,35675], 'Occupation': ['Data Scientist','Banker','finance','Bekar','bou']}
df=pd.DataFrame(data=data)
print(df)
num_col=df.shape[1]
num_row=df.shape[0]
print("Number of column: ",num_col)
print("Number of rows: ",num_row)
