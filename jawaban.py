import pandas as pd

data = {'Nama': ['John', 'Jane', 'Bob', 'Alice'],
        'Usia': [25, 35, 30, 28],
        'Gaji': [50000, 60000, 70000, 55000]}

df = pd.DataFrame(data)

# Pertanyaan 1:
print (df)

dflimapersen = df
for i in range(len(dflimapersen)):
    dflimapersen.loc[i, 'Gaji'] = (lambda x: x * 1.05)(dflimapersen.loc[i, 'Gaji'])


# Gunakan loop for dan fungsi lambda untuk menghitung gaji setiap karyawan setelah diberikan peningkatan sebesar 5% dari gaji saat ini.

# Pertanyaan 2:
print("DataFrame setelah peningkatan gaji 5%:")
print(dflimapersen)

# Setelah perubahan dilakukan, tampilkan DataFrame yang sudah diperbarui dan berikan ringkasan perubahan yang telah terjadi.

# Pertanyaan 3:
df30tahun = dflimapersen

for i in range(len(df30tahun)):
    if df30tahun.loc[i, 'Usia'] > 30:
        df30tahun.loc[i, 'Gaji'] = (lambda x: x * 1.02)(df30tahun.loc[i, 'Gaji'])
# Gunakan loop for lagi untuk mengevaluasi karyawan yang usianya di atas 30 tahun. Jika usia karyawan di atas 30, berikan peningkatan tambahan sebesar 2% dari gaji saat ini menggunakan fungsi lambda.

# Pertanyaan 4:
print("\nDataFrame setelah peningkatan gaji tambahan yang 30 tahun:")
print(df30tahun)
# Tampilkan DataFrame yang sudah diperbarui setelah peningkatan gaji tambahan dan berikan ringkasan hasilnya.

# ---------------------------- #
# Buat Branch Baru pada repository github berikut dengan format KELAS_NRP_NAMA
# https://github.com/diashfirdaus-cyber/Pemdas_Itenas.git
# ---------------------------- #

# Catatan:

# Gunakan loop for dan fungsi lambda untuk mengimplementasikan operasi yang diminta.
# Pastikan untuk menyimpan hasil perubahan pada DataFrame.
# Tampilkan hasil dan ringkasan dengan jelas.
# Jangan lupa untuk menyesuaikan persentase peningkatan gaji sesuai dengan cerita.