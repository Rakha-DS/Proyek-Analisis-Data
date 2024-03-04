import pandas as pd
import streamlit as st

dtLink = lambda x : f"https://raw.githubusercontent.com/Rakha-DS/Proyek-Analisis-Data/main/{x}.csv"

day_df = pd.read_csv(dtLink("day"))
hour_df = pd.read_csv(dtLink("hour"))

#Data Wrangling
dteday_columns = ["dteday"]
for column in dteday_columns:
    day_df[column] = pd.to_datetime(day_df[column])
    hour_df[column] = pd.to_datetime(hour_df[column])

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

#Dashboard
st.title('Bike Rental Service Analysis')

#Sidebar
st.sidebar.subheader('Choose an option')
option = st.sidebar.selectbox('Select an option', ['Weather Effects', 'Peak Rental Day'])

#Graph Options
if option == 'Weather Effects':
    st.subheader('Effect of Weather on Bike Rentals')

    weatherCorr = day_df['weathersit'].corr(day_df['cnt'])
    st.write("The correlation value between the weather and bike rental count is {:.3f}: ".format(weatherCorr))

    weatherRental = day_df.groupby('weatherSitch')['cnt'].mean().reset_index().sort_values('cnt',ascending=True)
    st.bar_chart(weatherRental.set_index('weatherSitch'))

elif option == 'Peak Rental Day':
    st.subheader('Peak Rental Day')

    avgRentalByDay = day_df.groupby(day_df['dteday'].dt.day_of_week)['cnt'].mean()
    st.bar_chart(avgRentalByDay.rename(index=numToDay))