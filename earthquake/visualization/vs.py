import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel('earthquake/data/earthquake.xlsx')

df['TarihSaat'] = pd.to_datetime(df['Tarih'].astype(str) + ' ' + df['Saat'], format='%Y.%m.%d %H:%M:%S')

df_clean = df.dropna(subset=['ML'])
print('Temizlenmiş veri seti boyutu: ', df_clean.shape)



# Görselleştirme
# Tarihe göre deprem sayısı
plt.figure(figsize=(12,6))
sns.countplot(data=df_clean, x=df_clean['TarihSaat'].dt.date, palette='viridis')
plt.xticks(rotation=45)
plt.title('Günlere Göre Deprem Sayısı')
plt.xlabel('Tarih')
plt.ylabel('Deprem Sayısı')
plt.tight_layout()
plt.show()


# Depremin büyüklük dağılımı
# plt.figure(figsize=(8,6))
# sns.histplot(df_clean['ML'], bins=50, kde=True, color='skyblue')
# plt.title('Deprem Büyüklük Dağılımı')
# plt.xlabel('Büyüklük (ML)')
# plt.ylabel('Frekans')
# plt.show()



# # Derinliğine Göre Deprem Büyüklükleri
# plt.figure(figsize=(8,6))
# sns.scatterplot(data=df_clean, x = 'Derinlik(km)', y = 'ML', hue='Yer', palette='deep')
# plt.title('Derinliğine Göre Deprem Büyüklükleri')
# plt.xlabel('Derinlik (km)')
# plt.ylabel('Büyüklük (ML)')
# plt.legend(bbox_to_anchor = (1.01,1), loc="center")   # hue nın nerede olacağını ayarla
# plt.tight_layout()
# plt.show()
