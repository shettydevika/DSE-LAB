#Python program to perform File Operation on Excel Data Set.
import pandas as pd
data = {
    'Name': ['John', 'Emma', 'Sam', 'Lisa', 'Tom'],
    'Age': [25,30,28,32,27],
    'Country': ['USA', 'Denmark', 'Mexico', 'Germany', 'Russia'],
    'Salary': [50000,60000,78000,52000,27000]
}

df=pd.DataFrame(data)
print("Original Data Frame: \n")
print(df)

name_age=df[['Name','Age']]
print("\n Name and Age column:\n")
print(name_age)

#Filter data
filtered_data=df[df['Country']=='USA']
print("Filtered data ('Country'=='USA'):\n")
print(filtered_data)

#Sort data
sorted_data = df.sort_values('Salary',ascending=False)
print("\nSorted data(by salary in descending order):")
print(sorted_data)

average_salary=df['Salary'].mean()
print("\n Average Salary: ", average_salary)

#Adding new column
df['Experience']=[3,6,4,8,5]
print("\n Data Frame with added experience column:")
print(df)

#updating values
df.loc[df['Name']=='Emma', 'Salary']=65000
print("\nData Frame after updating Emma's Salary:")
print(df)

'''
OUTPUT:

Original Data Frame: 

   Name  Age  Country  Salary
0  John   25      USA   50000
1  Emma   30  Denmark   60000
2   Sam   28   Mexico   78000
3  Lisa   32  Germany   52000
4   Tom   27   Russia   27000

 Name and Age column:

   Name  Age
0  John   25
1  Emma   30
2   Sam   28
3  Lisa   32
4   Tom   27
Filtered data ('Country'=='USA'):

   Name  Age Country  Salary
0  John   25     USA   50000

Sorted data(by salary in descending order):
   Name  Age  Country  Salary
2   Sam   28   Mexico   78000
1  Emma   30  Denmark   60000
3  Lisa   32  Germany   52000
0  John   25      USA   50000
4   Tom   27   Russia   27000

 Average Salary:  53400.0

 Data Frame with added experience column:
   Name  Age  Country  Salary  Experience
0  John   25      USA   50000           3
1  Emma   30  Denmark   60000           6
2   Sam   28   Mexico   78000           4
3  Lisa   32  Germany   52000           8
4   Tom   27   Russia   27000           5

Data Frame after updating Emma's Salary:
   Name  Age  Country  Salary  Experience
0  John   25      USA   50000           3
1  Emma   30  Denmark   65000           6
2   Sam   28   Mexico   78000           4
3  Lisa   32  Germany   52000           8
4   Tom   27   Russia   27000           5
​'''
