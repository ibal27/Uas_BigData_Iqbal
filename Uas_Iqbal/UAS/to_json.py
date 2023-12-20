import requests #library yang kita gunakan untuk mengakses API/json
import pandas as pd
import json
 
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
        data_ = response.json()['data']
        data_ += response2.json()['data']
        data_ += response3.json()['data']
        data_ += response4.json()['data']

        print(data_)
        with open("data.json", "w") as json_file:
            json.dump(data_, json_file)
 
        # Baca data JSON dari file
        with open('data.json', 'r') as json_file:
            data = json_file.read()

        # Ubah JSON menjadi DataFrame pandas
        df = pd.read_json(data)
 
        # Simpan DataFrame ke dalam file Excel
        excel_file = 'jumlah kepala keluarga miskin.xlsx'
        df.to_excel(excel_file, index=False)
 
        print(f"Data telah disimpan dalam file Excel: {excel_file}")
 
        # True jika ingin menampilkan hasil
        # False jika tidak ingin menampilkan hasil

        INGIN_DI_PRINT = False

        if INGIN_DI_PRINT:
            # Menampilkan hasil
            for jml_kpl in data_:
                print(f"id: {jml_kpl['id']}")
                print(f"kod_prov: {jml_kpl['kode_provinsi']}")
                print(f"nm_prov: {jml_kpl['nama_provinsi']}")
                print(f"bps_kod_kab: {jml_kpl['bps_kode_kabupaten_kota']}")
                print(f"bps_nm_kab: {jml_kpl['bps_nama_kabupaten_kota']}")
                print(f"bps_kod_kec: {jml_kpl['bps_kode_kecamatan']}")
                print(f"bps_nm_kec: {jml_kpl['bps_nama_kecamatan']}")
                print(f"bps_kod_desa_kel: {jml_kpl['bps_kode_desa_keluarahan']}")
                print(f"bps_desa_kel: {jml_kpl['bps_desa_kelurahan']}")
                print(f"keme_kode_kec: {jml_kpl['kemendagri_kode_kecamatan']}")
                print(f"keme_nm_kec: {jml_kpl['kemendagri_nama_kecamatan']}")
                print(f"keme_kode_desa_kel: {jml_kpl['kemendagri_kode_desa_kelurahan']}")
                print(f"keme_nm_desa_kel: {jml_kpl['kemendagri_nama_desa_kelurahan']}")
                print(f"lokasi: {jml_kpl['lokasi']}")
                print(f"kategori: {jml_kpl['kategori']}")
                print(f"jumlah: {jml_kpl['jumlah']}")
                print(f"satuan: {jml_kpl['satuan']}")
                print(f"tahun: {jml_kpl['tahun']}")
                print("-" * 30)
    else:
        print(f"Gagal mengambil data. Kode status: {response.status_code}")
 
except requests.exceptions.RequestException as e:
    print(f"Terjadi kesalahan saat menghubungi API: {str(e)}")
 
 

