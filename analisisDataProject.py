import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#How does weather affect the bike rental servicee?
#At what day of the week does the rental hit it's peak number of customers?

day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

#Data Wrangling
#Memeriksa tipe data pada dataset
day_df.info()
hour_df.info()
#Terlihat data lengkap tanpa adanya missing values
#Terlihat pada dataset dteday menggunakan tipe data object sehingga diubah dulu menjadi datetime
dteday_columns = ["dteday"]
for column in dteday_columns:
    day_df[column] = pd.to_datetime(day_df[column])
    hour_df[column] = pd.to_datetime(hour_df[column])
#Mengecek adakah duplikat data pada dataset
print("Jumlah duplikasii data pada day.csv : ", day_df.duplicated().sum())
print("Jumlah duplikasii data pada hour.csv : ", hour_df.duplicated().sum())
#Data tidak ada duplicate value
print(day_df.describe())
print(hour_df.describe())
#Wrangling done no need for more cleaning

#EDA
weatherSitch = {
    1: 'Clear',
    2: 'Misty',
    3: 'Light snow/rain',
    4: 'Heavy rain/storm'
} 
day_df['weatherSitch'] = day_df['weathersit'].map(weatherSitch)
numToDay = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}
#Pertanyaan 1
weatherRental = day_df.groupby('weatherSitch')['cnt'].mean().reset_index().sort_values("cnt")
weatherCorr = day_df['weathersit'].corr(day_df['cnt'])
plt.figure(figsize=(10,6))
sns.barplot(x='cnt', y='weatherSitch', data=weatherRental)
plt.xlabel('Average number of rentals')
plt.ylabel('Weather situation')
plt.title('Effect of weather to the number of bike rentals')
plt.show()
print("The correlation value between the weather and bike rental count is : ",weatherCorr)

#Pertanyaan 2
avgRentalByDay = day_df.groupby(day_df['dteday'].dt.day_of_week)['cnt'].mean().sort_index()
plt.bar(avgRentalByDay.index.map(numToDay), avgRentalByDay.values)
plt.xlabel('Day of the week')
plt.ylabel('Average number of rentals')
plt.title('Average number of rentals by Day of the week')
plt.show()
