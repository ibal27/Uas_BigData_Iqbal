import mysql.connector

import pandas as pd

 

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="uas_big_data"

)

# Buat objek cursor

db_cursor = db_connection.cursor()

# Contoh pernyataan SQL SELECT

select_query = "SELECT * FROM pende_tens"

# Eksekusi pernyataan SELECT

db_cursor.execute(select_query)

# Ambil hasil SELECT

results = db_cursor.fetchall()

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()

# Konversi hasil SELECT menjadi dataframe pandas

df = pd.DataFrame(results, columns=["id", "kod_prov", "nm_prov", "bps_kod_kab", "bps_nm_kab", "bps_kod_kec", "bps_nm_kec", "keme_kode_kec", "keme_nm_kec", "upt_pusk", "jml_pende_tens", "satuan", "tahun"])


# Simpan dataframe sebagai file Excel

df.to_excel("penderita hipertensi di kota bandung.xlsx", index=False, engine="openpyxl")

print("Data telah disimpan dalam file Excel 'penderita hipertensi di kota bandung'") #csv / xlsx

