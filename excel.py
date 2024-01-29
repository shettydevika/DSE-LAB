import pandas as pd
#Read Excel file
df=pd.read_excel('D:/data.xlsx')

#display first few rows
print("First few rows:")
print(df.head())

#get summary statistics
print("\n Summary statistics:")
print(df.describe())

#Filter data
filtered_data=df[df['Age']>30]
print("\nFiltered data (Age>30):")
print(filtered_data)

#Sort data
sorted_data = df.sort_values(by='Annual Salary',ascending=False)
print("\nSorted data(by salary):")
print(sorted_data)

#Add a new column
df['Bonus']=df['Annual Salary']*0.1
print("\nData with new column(Bonus):")
print(df)

#write to Excel file
df.to_excel('output.xlsx',index=False)
print("\n Data written to output.xlsx")