# Import library
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv('data.csv')

# Header
st.markdown("<h2 style='text-align: center;'>DASHBOARD BIKE SHARING 2011-2012</h2>", unsafe_allow_html=True)
st.write('')

# jumlah rental 
jumlah_2011 = df[df['yr'] == 2011]['cnt'].sum()
jumlah_2012 = df[df['yr'] == 2012]['cnt'].sum()

# hitung persentase
persentase = round((jumlah_2012 - jumlah_2011) / jumlah_2011 * 100)
persentase = str(persentase) + "%"

# hitung total rental sepeda
total = jumlah_2011 + jumlah_2012

# visualisasi
col1, col2,col3 = st.columns(3)

with col1:
    st.metric(label='Total Rental Sepeda', value=total)

with col2:
    st.metric(label='Jumlah Rental Tahun 2011', value=jumlah_2011)

with col3:
    st.metric(label='Jumlah Rental Tahun 2012', value=jumlah_2012, delta=persentase
        , delta_color='normal')

# =====================================================================================
# 1. Hari Paling Sedikit Perental
st.subheader('Hari Paling Sedikit Perental')

# hitung perental bedasarkan hari
weekday = df.groupby('weekday').sum()['cnt']

# visualisasi
min_index = weekday.idxmin()
color1 = ['#ceffbc' if day != min_index else '#162a10' for day in weekday.index]

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=weekday.index, y=weekday.values, palette=color1, ax=ax)
ax.set_title('Hari Paling Sedikit Perental', fontsize=15)
ax.set_xlabel('Hari', fontsize=15)
ax.set_ylabel('Jumlah Sewa', fontsize=15)
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center',
                va = 'center',
                xytext = (0, 10),
                textcoords = 'offset points')
ax.set_yticks([0, 100000,200000,300000,400000,500000,600000])
ax.set_yticklabels(['0', '100 Ribu', '200 Ribu', '300 Ribu', '400 Ribu', '500 Ribu', '600 Ribu'])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
st.pyplot(fig)

# =====================================================================================
# 2. Jumlah Rental Berdasarkan Tipe Perental
st.subheader('Jumlah Rental Berdasarkan Tipe Perental')

casual = df.groupby('yr').sum()['casual']
registered = df.groupby('yr').sum()['registered']

# visualisasi
data = pd.DataFrame({'type': ['Casual', 'Registered'],
                    'count': [casual.sum(), registered.sum()]})
fig, ax = plt.subplots()
ax.pie(data['count'], labels=data['type'], autopct='%.2f%%', startangle=90, colors=['#ff9999', '#66b3ff'])
ax.axis('equal')  
st.pyplot(fig)

# =====================================================================================
# 3. Jumlah Rental Berdasarkan Musim
st.subheader('Jumlah Rental Berdasarkan Musim')

# hitung perental berdasarkan season
season = df.groupby('season').sum()['cnt']

# visualisasi
max_index = season.idxmax()
color2 = ['#ceffbc' if day != max_index else '#162a10' for day in season.index]

fig, ax = plt.subplots(figsize=(10,5))
sns.barplot(x=season.index, y=season.values, palette=color2, ax=ax)
ax.set_title('Jumlah Rental Berdasarkan Musim', fontsize=15)
ax.set_xlabel('Musim', fontsize=15)
ax.set_ylabel('Jumlah Sewa', fontsize=15)
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.0f'),
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha = 'center',
                va = 'center',
                xytext = (0, 10),
                textcoords = 'offset points')
ax.set_yticks([0, 100000,200000,300000,400000,500000,600000,700000,800000,900000,1000000])
ax.set_yticklabels(['0', '100 Ribu', '200 Ribu', '300 Ribu', '400 Ribu', '500 Ribu', '600 Ribu', '700 Ribu', '800 Ribu', '900 Ribu', '1 Juta'])
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
st.pyplot(fig)




