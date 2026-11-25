import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(r"C:\Users\Srikant Nair\Downloads\Un fresh.csv")
print(df)
print(df.head())
print(df.shape)
print(df.info())
print("Missing values null",df.isnull().sum())
missing_percentage = (df.isnull().sum() / len(df)) * 100

print(missing_percentage)
print(df.duplicated().sum())
#These 27 duplicate detections are caused by completely blank rows. Pandas considers repeated completely empty rows duplicates after the first one.
#Step 6: Remove completely empty rows
#We can remove rows where every column is empty.
df = df.dropna(how='all') #dropna() removes rows containing missing values according to the specified condition.
#how='all' means remove a row only when all its columns are missing.
print(df.shape)
print(df.duplicated().sum())
duplicates = df[df.duplicated()]

print("Number of duplicates:", len(duplicates))
df = df.drop_duplicates()
#Clean column names
#Your Date column contains an unnecessary leading space.
#We can remove unnecessary spaces from all column names:
print(df.columns) #in this there are extra space in region ,all columns so 
df.columns = df.columns.str.strip()

print(df.columns)
#print("Final Dataset Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())
print(df.shape) #after cleaning and using dropna missing values have been removed now
#it has 740 rows nd 7 columns from 768 that means 28 missing values have been removed
print(df.dtypes)
df.to_csv("un_Fresh-Cleaned.csv",index=False) #you can skip this is just to have cleaned
#EDA reduce spacing inside values of columns convert data types in right format
#so it can read code correctly like date into date format numeric in numeric

df['Region']=df['Region'].str.strip()
df['Frequency']=df['Frequency'].str.strip() 
df['Area']=df['Area'].str.strip()
df['Date']=pd.to_datetime(df['Date'],dayfirst=True,errors='coerce')
numericcols=[
    'Estimated Unemployment Rate (%)',
     'Estimated Employed','Estimated Labour Participation Rate (%)']
for col in numericcols:
    df[col]=pd.to_numeric(df[col],errors='coerce')
print(df.dtypes)
print(df.describe())#numerical info of our dataset
#check outliers:from numerical columns
for col in numericcols:
    q1=df[col].quantile(0.25)
    q3=df[col].quantile(0.75)
    IQR=q3-q1
    lowerlimit=q1-1.5*IQR
    upperlimit=q3+1.5*IQR
    outliers=df[(df[col]<lowerlimit)|(df[col]>upperlimit)]
    print("\nColumn:",col)
    print("Q1:",q1)
    print("Q3:",q3)
    print("IQR",IQR)
    print("lower limit:",lowerlimit)
    print("Upperlimit:",upperlimit)
    print("Number of outliers:",len(outliers))
#analyze unemployement trends across indian states(region wise unemployment)
stateunemployment=df.groupby("Region")["Estimated Unemployment Rate (%)"].mean().sort_values(ascending=False)
print(stateunemployment)
#create graph of this
plt.figure(figsize=(12,8))
stateunemployment.plot(kind="bar")
plt.title("Average unemployment rate across indian states")
plt.xlabel("Region")
plt.ylabel("Average unemployment rate")
plt.tight_layout()
plt.show()  #we notice tripura region has highest unemployment
#analyze unemployment trends over time monthly using date column
monthlyunemployment=df.groupby(df['Date'].dt.to_period('M'))["Estimated Unemployment Rate (%)"].mean()
print(monthlyunemployment)
#create graph for this
plt.figure(figsize=(12,7))
monthlyunemployment.plot(kind="line",marker="o")
plt.title("Monthly unemployment Trend")
plt.xlabel("Month")
plt.ylabel("Average Unemployment rate monthly(%)")
plt.grid()
plt.tight_layout
plt.show() #we notice rise of unemployment in april,may 2020 during covid period
#compare rural,urban unemployment rate by calculating avg
areaunemployment=df.groupby("Area")["Estimated Unemployment Rate (%)"].mean()
print(areaunemployment)
#create graph
plt.figure(figsize=(12,7))
areaunemployment.plot(kind="bar")
plt.title("Area wise Unemployment trend")
plt.xlabel("Area")
plt.ylabel("Average unemployment Rate (%)")
plt.tight_layout()
plt.show()
df.to_excel("un-freshfullcleaned.xlsx",index=False)
print("Excel file Downloaded Succesfully!")
import os
print(os.getcwd())
print(os.path.exists("un-freshfullcleaned.xlsx"))
print(os.path.abspath("un-freshfullcleaned.xlsx"))