import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

import folium


df = pd.read_excel('earthquake/data/earthquake.xlsx')
print('\n İlk 5 satırı göster:')
print(df.head())

print('\n Genel bilgi göster:')
print(df.info())


print('\n Temel İstatistiksel Özet:')
print(df.describe())

# Boş değer var mı kontrol et
print('\n Boş değer kontrölü: ')
print(df.isnull().sum)


# tarih ve saat sütununu birleştirme
df['TarihSaat'] = pd.to_datetime(df['Tarih'].astype(str) + ' ' + df['Saat'], format='%Y.%m.%d %H:%M:%S')


# sütünları çıkarttık
df.drop(['Tarih', 'Saat'], axis=1, inplace=True)
print("\nGüncellenmiş veri tipleri: ")

# kontrol et
print(df.dtypes)


# ML İLE ANALİZ ETME
# düzenleme yapma
df['ML'] = pd.to_numeric(df['ML'], errors='coerce')      # sayısal hataları görmezden gel
print("\n'ML' Sütünundaki eksik değerler: ")
print(df['ML'].isnull().sum())


# eğer varsa kaldır -  ML' de boş, tre veya herhangi bir sayısal olmayan veri varsa temizle
df_clean = df.dropna(subset=['ML'])
# print('Temizlenmiş veri seti boyutu: ', df_clean.shape)
# print(df_clean)




# Harita merkezi oluşturma
map_center = [37.0, 35.0]
m = folium.Map(location = map_center, zoom_start=5)


# her bir depremi haritaya ekle
for idx, row in df_clean.iterrows():
    folium.CircleMarker(
        location= [row['Enlem(N)'], row['Boylam(E)']], 
        radius = row['ML']*2,
        popup = f"Yer: {row['Yer']} <br> Büyüklük: {row['ML']} <br> Derinlik:{row['Derinlik(km)']} km ",
        color = 'crimson', 
        fill = True,
        fill_color = 'crimson'
    ).add_to(m)


# html olarak dosyayı kaydet
m.save('depremler_haritası.html')
print("İşlem gerçekleşti")
