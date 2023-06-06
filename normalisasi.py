import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# URL file CSV di GitHub
url = 'https://raw.githubusercontent.com/alammahdum8/dbscan_new/main/new.csv'

# Membaca file CSV
dataframe = pd.read_csv(url)

# Memisahkan kolom target (label) dari fitur
X = dataframe.iloc[:, :-1].values  # Mengambil semua kolom kecuali kolom terakhir
y = dataframe.iloc[:, -1].values   # Mengambil kolom terakhir sebagai target

# Normalisasi data menggunakan MinMaxScaler
scaler = MinMaxScaler()
X_normalized = scaler.fit_transform(X)

# Tampilkan data yang sudah dinormalisasi
normalized_dataframe = pd.DataFrame(X_normalized, columns=dataframe.columns[:-1])
normalized_dataframe['target'] = y
print(normalized_dataframe.head())
