import requests
import mysql.connector
 
# Konfigurasi database
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'uas_bigdata_iqbal'
}
 
# Alamat URL API
api_url = "https://opendata.bandung.go.id/api/bigdata/kecamatan_cibeunying_kidul/jmlh_kpl_klrg_nggt_klrg_mskn_d_kcmtn_cbnyng_kdl_kt_bndng"
 
try:
    # Mengirim permintaan GET ke API
    response = requests.get(api_url)
    response2 = requests.get(api_url + "?page=2")
    response3 = requests.get(api_url + "?page=3")
    response4 = requests.get(api_url + "?page=4")
 
    # Memeriksa status kode respons
    if response.status_code == 200:
        # Parse data JSON yang diterima
        user_data = response.json()['data']
        user_data += response2.json()['data']
        user_data += response3.json()['data']
        user_data += response4.json()['data']
 
        # Membuka koneksi ke database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
 
        # Menambahkan data pengguna ke dalam tabel
        for jml_kpl in user_data:
            cursor.execute('''
                INSERT INTO jml_kpl (id, kod_prov, nm_prov, bps_kod_kab, bps_nm_kab, bps_kod_kec, bps_nm_kec,bps_kod_desa_kel, 
                           bps_desa_kel, keme_kode_kec, keme_nm_kec, keme_kode_desa_kel,keme_nm_desa_kel, lokasi, kategori, jumlah, satuan, tahun)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (jml_kpl['id'], jml_kpl['kode_provinsi'], jml_kpl['nama_provinsi'], 
                    jml_kpl['bps_kode_kabupaten_kota'], jml_kpl['bps_nama_kabupaten_kota'], jml_kpl['bps_kode_kecamatan'], 
                    jml_kpl['bps_nama_kecamatan'],jml_kpl['bps_kode_desa_kelurahan'], jml_kpl['bps_desa_kelurahan'],jml_kpl['kemendagri_kode_kecamatan'], 
                    jml_kpl['kemendagri_nama_kecamatan'], jml_kpl['kemendagri_kode_desa_kelurahan'],jml_kpl['kemendagri_nama_desa_kelurahan'],
                    jml_kpl['lokasi'],jml_kpl['kategori'],jml_kpl['jumlah'], jml_kpl['satuan'],  
                    jml_kpl['tahun']))
 
        # Menyimpan perubahan dan menutup koneksi
        conn.commit()
        conn.close()
 
        print("Data pengguna telah disimpan ke database MySQL.")
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
 
except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat menghubungi API: {str(e)}")
 