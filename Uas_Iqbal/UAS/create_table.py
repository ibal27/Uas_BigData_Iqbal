# Buat koneksi ke server MySQL
import mysql.connector
db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="uas_bigdata_iqbal"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan struktur tabel 'mahasiswa'

create_table_query = """

CREATE TABLE jml_kpl (

   id INT AUTO_INCREMENT PRIMARY KEY,
    kod_prov varchar(255),
    nm_prov varchar(255),
    bps_kod_kab int,
    bps_nm_kab varchar(255),
    bps_kod_kec int,
    bps_nm_kec varchar(255),
    bps_kod_desa_kel int,
    bps_desa_kel varchar(255),
    keme_kode_kec varchar(255),
    keme_nm_kec varchar(255),
    keme_kode_desa_kel varchar(255),
    keme_nm_desa_kel varchar(255),
    lokasi varchar(255),
    kategori varchar (255),
    jumlah int,
    satuan varchar(11),
    tahun varchar(255)
)

"""

 

# Eksekusi perintah SQL untuk membuat tabel

db_cursor.execute(create_table_query)

 

# Komit perubahan ke database

db_connection.commit()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()