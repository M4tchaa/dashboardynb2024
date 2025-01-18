import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as sns  
import streamlit as st  
  
sns.set_theme(style='dark')  
  
# Load Data  
dataynb = pd.read_csv("main_data.csv")  
  
# Data Preparation  
# Pastikan kolom timestamp diubah menjadi datetime jika diperlukan  
dataynb["timestamp"] = pd.to_datetime(dataynb["timestamp"])  
  
# Sidebar Date Filter (jika ada kolom tanggal)  
min_date = dataynb["timestamp"].min()  
max_date = dataynb["timestamp"].max()  
  
with st.sidebar:    
    # Menambahkan spasi di atas dan di bawah logo untuk memusatkan  
    st.write("")  # Spasi atas  
    st.image("logo.png", width=200)  
    st.write("")  # Spasi bawah  
    start_date, end_date = st.date_input(    
        label="Rentang Waktu",    
        min_value=min_date,    
        max_value=max_date,    
        value=[min_date, max_date]    
    )    
  
filtered_data = dataynb[(dataynb["timestamp"] >= str(start_date)) &     
                         (dataynb["timestamp"] <= str(end_date))]  
filtered_data = dataynb  
  
# Helper Functions  
def create_gender_data(df):  
    return df['jenis_kelamin'].value_counts()  
  
def create_city_data(df):  
    return df['kota'].value_counts()  
  
def create_status_data(df):  
    return df['status'].value_counts()  
  
def create_age_group_data(df):  
    return df['rentang_usia'].value_counts()  
  
def create_hobby_category_data(df):  
    return df['hobby_category'].value_counts()  
  
# Prepare Data Using Helper Functions  
gender_data = create_gender_data(filtered_data)  
city_data = create_city_data(filtered_data)  
status_data = create_status_data(filtered_data)  
age_group_data = create_age_group_data(filtered_data)  
hobby_category_data = create_hobby_category_data(filtered_data)  
  
# Streamlit Visualizations  
st.title("Dashboard Analisis Peserta Yukngaji Bogor")  
st.header("Analisis Peserta Yukngaji Bogor")  
  
##### Gender Distribution
st.subheader("Distribusi Jenis Kelamin")

# Data distribusi jenis kelamin
gender_data = dataynb[dataynb['jenis_kelamin'] != 'Undefined']['jenis_kelamin'].value_counts()
total = gender_data.sum()

# Membuat plot
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(gender_data.index, gender_data.values, color='skyblue')

# Menambahkan persentase di atas bilah
for bar in bars:
    yval = bar.get_height()
    percentage = f'{100 * yval / total:.1f}%'  # Menghitung persentase
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        yval + 50,  # Mengatur posisi teks
        percentage,  # Menampilkan persentase
        ha='center',
        va='bottom',
        fontsize=10
    )

# Menambahkan judul dan label
ax.set_title('Distribusi Jenis Kelamin', fontsize=14, fontweight='bold')
ax.set_xlabel('Jenis Kelamin', fontsize=12)
ax.set_ylabel('Jumlah', fontsize=12)

# Menyembunyikan garis tepi atas dan kanan
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Menampilkan plot di Streamlit
st.pyplot(fig) 

##### City Distribution  #####
st.subheader("Distribusi Kota")

# Data distribusi kota
total = city_data.sum()

# Membuat plot
fig, ax = plt.subplots(figsize=(8, 6))
bars = ax.bar(city_data.index, city_data.values, color='lightgreen')

# Menambahkan persentase di atas bilah
for bar in bars:
    yval = bar.get_height()
    percentage = f'{100 * yval / total:.1f}%'  # Menghitung persentase
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        yval + 50,  # Mengatur posisi teks
        percentage,  # Menampilkan persentase
        ha='center',
        va='bottom',
        fontsize=10
    )

# Menambahkan judul dan label
ax.set_title('Distribusi Kota', fontsize=14, fontweight='bold')
ax.set_xlabel('Kota', fontsize=12)
ax.set_ylabel('Jumlah', fontsize=12)

# Menyembunyikan garis tepi atas dan kanan
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Menampilkan plot di Streamlit
st.pyplot(fig)

##### Info Kajian  #####
st.subheader("Distribusi Info Kajian")  
  
# Data distribusi info kajian  
info_data = dataynb['info_kajian'].value_counts()  
  
# Menghapus kategori 'Other' jika ada  
if 'Other' in info_data.index:  
    info_data = info_data.drop('Other')  
  
# Total jumlah data  
total = info_data.sum()  # Total jumlah data  
  
# Membuat plot  
fig, ax = plt.subplots(figsize=(8, 6))  
bars = ax.bar(info_data.index, info_data.values, color='cornflowerblue')  
  
# Menambahkan persentase di atas bilah  
for bar in bars:  
    yval = bar.get_height()  
    percentage = f'{100 * yval / total:.1f}%'  # Menghitung persentase  
    ax.text(  
        bar.get_x() + bar.get_width() / 2,  
        yval + 5,  # Mengatur posisi teks  
        percentage,  # Menampilkan persentase  
        ha='center',  
        va='bottom',  
        fontsize=10  
    )  
  
# Menambahkan judul dan label  
ax.set_title('Distribusi Info Kajian', fontsize=14, fontweight='bold')  
ax.set_xlabel('Info Kajian', fontsize=12)  
ax.set_ylabel('Jumlah', fontsize=12)  
  
# Menyembunyikan garis tepi atas dan kanan  
ax.spines['top'].set_visible(False)  
ax.spines['right'].set_visible(False)  
  
# Menampilkan plot di Streamlit  
st.pyplot(fig)  

##### Status Distribution #####  
st.subheader("Distribusi Status")  
  
# Menghapus kategori 'Undefined' jika ada  
if 'Undefined' in status_data.index:  
    status_data = status_data.drop('Undefined')  
  
total_status = status_data.sum()  # Total jumlah data untuk status  
  
fig, ax = plt.subplots(figsize=(8, 6))  
bars = ax.bar(status_data.index, status_data.values, color='salmon')  
  
# Menambahkan jumlah dan persentase di atas bilah  
for bar in bars:  
    yval = bar.get_height()  
    percentage = f'{100 * yval / total_status:.1f}%'  # Menghitung persentase  
    ax.text(  
        bar.get_x() + bar.get_width() / 2,  
        yval + 5,  
        f'{yval:,.0f} ({percentage})',  # Menampilkan jumlah dan persentase  
        ha='center',  
        va='bottom',  
        fontsize=10  
    )  
  
ax.set_title('Distribusi Status', fontsize=14, fontweight='bold')  
ax.set_xlabel('Status', fontsize=12)  
ax.set_ylabel('Jumlah', fontsize=12)  
ax.spines['top'].set_visible(False)  
ax.spines['right'].set_visible(False)  
st.pyplot(fig)  
  
# Age Group Distribution  
st.subheader("Distribusi Rentang Usia")  
  
# Menghapus kategori 'Undefined' jika ada  
if 'Undefined' in age_group_data.index:  
    age_group_data = age_group_data.drop('Undefined')  
  
total_age = age_group_data.sum()  # Total jumlah data untuk rentang usia  
  
fig, ax = plt.subplots(figsize=(8, 6))  
bars = ax.bar(age_group_data.index, age_group_data.values, color='orange')  
  
# Menambahkan jumlah dan persentase di atas bilah  
for bar in bars:  
    yval = bar.get_height()  
    percentage = f'{100 * yval / total_age:.1f}%'  # Menghitung persentase  
    ax.text(  
        bar.get_x() + bar.get_width() / 2,  
        yval + 5,  
        f'{yval:,.0f} ({percentage})',  # Menampilkan jumlah dan persentase  
        ha='center',  
        va='bottom',  
        fontsize=10  
    )  
  
ax.set_title('Distribusi Rentang Usia', fontsize=14, fontweight='bold')  
ax.set_xlabel('Rentang Usia', fontsize=12)  
ax.set_ylabel('Jumlah', fontsize=12)  
ax.spines['top'].set_visible(False)  
ax.spines['right'].set_visible(False)  
st.pyplot(fig)
  
##### Hobby Category Distribution  #####
st.subheader("Distribusi Kategori Hobi")  
  
# Memfilter data untuk menghapus kategori 'Other'  
hobby_data = hobby_category_data[hobby_category_data.index.isin(['Membaca', 'Travelling', 'Hangout', 'Olahraga', 'Traveling', 'Masak'])]  
  
# Menghitung total jumlah data  
total_hobby = hobby_data.sum()  
  
fig, ax = plt.subplots(figsize=(8, 6))  
bars = ax.bar(hobby_data.index, hobby_data.values, color='purple')  
  
# Menambahkan jumlah dan persentase di atas bilah  
for bar in bars:  
    yval = bar.get_height()  
    percentage = f'{100 * yval / total_hobby:.1f}%'  # Menghitung persentase  
    ax.text(  
        bar.get_x() + bar.get_width() / 2,  
        yval + 5,  
        f'{yval:,.0f} ({percentage})',  # Menampilkan jumlah dan persentase  
        ha='center',  
        va='bottom',  
        fontsize=10  
    )  
  
ax.set_title('Distribusi Kategori Hobi', fontsize=14, fontweight='bold')  
ax.set_xlabel('Kategori Hobi', fontsize=12)  
ax.set_ylabel('Jumlah', fontsize=12)  
ax.spines['top'].set_visible(False)  
ax.spines['right'].set_visible(False)  
st.pyplot(fig)  

import matplotlib.pyplot as plt  
  
# Menghitung distribusi pendidikan terakhir, pastikan untuk menghapus 'Undefined'  
education_data = dataynb['pendidikan_terakhir'].value_counts()  
education_data = education_data[education_data.index != 'Other']  
  
# Menghitung total jumlah data  
total_education = education_data.sum()  
  
# Membuat plot  
fig, ax = plt.subplots(figsize=(8, 6))  
bars = ax.bar(education_data.index, education_data.values, color='lightblue')  
  
# Menambahkan jumlah dan persentase di atas bilah  
for bar in bars:  
    yval = bar.get_height()  
    percentage = f'{100 * yval / total_education:.1f}%'  # Menghitung persentase  
    ax.text(  
        bar.get_x() + bar.get_width() / 2,  
        yval + 5,  
        f'{yval:,.0f} ({percentage})',  # Menampilkan jumlah dan persentase  
        ha='center',  
        va='bottom',  
        fontsize=10  
    )  
  
# Menambahkan judul dan label  
ax.set_title('Distribusi Pendidikan Terakhir', fontsize=14, fontweight='bold')  
ax.set_xlabel('Pendidikan Terakhir', fontsize=12)  
ax.set_ylabel('Jumlah', fontsize=12)  
  
# Menyembunyikan garis tepi atas dan kanan  
ax.spines['top'].set_visible(False)  
ax.spines['right'].set_visible(False)  
  
# Menampilkan plot di Streamlit  
st.pyplot(fig)  


##### Distribusi Berdasarkan Timestamp   #####
st.subheader("Timestamp") 
plt.figure(figsize=(10, 6))  
  
# Menggunakan countplot untuk menghitung dan menampilkan distribusi  
ax = sns.countplot(data=dataynb[dataynb['timestamp_interval'] != 'undefined'],   
                   x='timestamp_interval',   
                   palette='pastel')  
  
# Menambahkan judul dan label  
plt.title('Distribusi Timestamp Interval', fontsize=16, fontweight='bold')  
plt.xlabel('Timestamp Interval', fontsize=14)  
plt.ylabel('Jumlah', fontsize=14)  
  
# Menghitung total untuk persentase  
total = len(dataynb[dataynb['timestamp_interval'] != 'undefined'])  
  
# Menambahkan persentase di atas setiap bilah  
for p in ax.patches:  
    percentage = f'{100 * p.get_height() / total:.1f}%'  
    ax.annotate(percentage,   
                (p.get_x() + p.get_width() / 2., p.get_height()),   
                ha='center',   
                va='bottom',   
                fontsize=10,   
                color='black')  
  
# Memutar label sumbu x agar lebih mudah dibaca  
plt.xticks(rotation=45)  
  
# Menyembunyikan garis tepi atas dan kanan  
ax.spines['top'].set_visible(False)  
ax.spines['right'].set_visible(False)  
  
# Menampilkan plot  
plt.tight_layout()  # Mengatur layout agar tidak ada yang terpotong  
st.pyplot(plt)  





##### Korelasi Data Peserta Yukngaji Bogor   #####
st.header("Analisis Korelasi Data Peserta Yukngaji Bogor")
  
# a. Hubungan antara Jenis Kelamin dan Status  
plt.figure(figsize=(10, 6))  
ax = sns.countplot(data=dataynb[~dataynb['status'].isin(['Undefined', 'Other'])],   
                   x='status',   
                   hue='jenis_kelamin',   
                   palette='Set2')  # Menggunakan palet warna yang lebih tegas  
  
plt.title('Hubungan antara Jenis Kelamin dan Status', fontsize=16, fontweight='bold')  
plt.xlabel('Status', fontsize=12)  
plt.ylabel('Jumlah', fontsize=12)  
  
# Menghitung total untuk persentase  
total = len(dataynb[~dataynb['status'].isin(['Undefined', 'Other'])])  
for p in ax.patches:  
    percentage = f'{100 * p.get_height() / total:.1f}%'    
    ax.annotate(percentage,   
                (p.get_x() + p.get_width() / 2., p.get_height()),   
                ha='center',   
                va='bottom',   
                fontsize=10)  
  
plt.legend(title='Jenis Kelamin')  
plt.xticks(rotation=45)  # Memutar label sumbu x jika diperlukan  
plt.tight_layout()  # Mengatur layout agar tidak terpotong  
st.pyplot(plt)  # Menampilkan plot di Streamlit  

# b. Hubungan antara Hobby Category dan Rentang Usia  
plt.figure(figsize=(10, 6))  
ax = sns.countplot(data=dataynb[~dataynb['hobby_category'].isin(['Undefined', 'Other'])],   
                   x='rentang_usia',   
                   hue='hobby_category',   
                   palette='Set2')  # Menggunakan palet warna yang lebih tegas  
  
plt.title('Hubungan antara Hobby Category dan Rentang Usia', fontsize=16, fontweight='bold')  
plt.xlabel('Rentang Usia', fontsize=12)  
plt.ylabel('Jumlah', fontsize=12)  
  
# Menghitung total untuk persentase  
total = len(dataynb[~dataynb['hobby_category'].isin(['Undefined', 'Other'])])  
# for p in ax.patches:  
#     percentage = f'{100 * p.get_height() / total:.1f}%'    
#     ax.annotate(percentage,   
#                 (p.get_x() + p.get_width() / 2., p.get_height()),   
#                 ha='center',   
#                 va='bottom',   
#                 fontsize=10)  
  
plt.legend(title='Hobby Category')  
plt.xticks(rotation=45)  # Memutar label sumbu x jika diperlukan  
plt.tight_layout()  # Mengatur layout agar tidak terpotong  
st.pyplot(plt)  # Menampilkan plot di Streamlit  


st.caption('Copyright © itsMatcha Development 2025')
