import pandas as pd
df=pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

#How many rows and columns are there in it?
row_count=len(df.index)
print('The no. of rows = ',row_count)
col_count=len(df.columns)
print("The no. of column is = ",col_count)

#In which class category more number of women’s died in terms of percentage of from that class?
survived_female = df.query('Sex == "female" and Survived == 0')
perc = (survived_female.groupby('Pclass').agg(['count']) / df.groupby('Pclass').agg(['count']) * 100).reset_index()
print("Class category= ",perc['Pclass'].max())


#The oldest passenger was a male or a female?
old_passenger= df["Age"].max(numeric_only=True)
fdata=df.query("Age==@old_passenger")
print( 'The oldest passenger was =' ,fdata['Sex'].values[0])

#Find the name of the oldest survived female.
survive_female=df.query('Survived==1 and Sex=="female"')
oldest=survive_female["Age"].max(numeric_only=True)
fdata=df.query("Age==@oldest")
print("The oldest survived female was = ",fdata['Name'].values[0])

#Find the details of the youngest passenger who could not survived.
non_survive=df.query('Survived==0')
young_passenger= non_survive["Age"].min(numeric_only=True)
ydata=non_survive.query("Age==@young_passenger")
print(ydata)

#Overall, what percentage of passengers survived the disaster?
survived= df.query("Survived==1")
percentage= len(survived)/len(df)*100
print('Percentage of passenger survived = ',percentage)


#Which sex of passengers were more on the board?
passenger= df.groupby("Sex").count().idxmax()
print("The passengers which are more on board is = ",passenger['PassengerId'])

#Which passenger has less average age ticket class wise?
avg=df.groupby('Pclass')['Age'].mean().idxmin()
print('The passenger class has less avg age=',avg)

#The highest fare belonged to which class?
max_fare= df["Fare"].max(numeric_only=True)
c= df.query("Fare==@max_fare")
print('The highest fare belongs to class = ',c["Pclass"].iloc[0])

#Which class has more number of passengers?
num_pass= df.groupby("Pclass").count().idxmax()
print("Class with more no.of passengers= ",num_pass['PassengerId'])