# Pengujian dan rubrik

## Status sebenar versi awal

Ujian automatik hanya memeriksa fail, konsistensi asas, pautan dan kandungan terlarang. Ia **bukan** bukti bahawa AI akan mematuhi prompt. Belum ada ujian hujung-ke-hujung dalam akaun ChatGPT pengguna atau cetakan fizikal.

## Senario manual (belum dilaksanakan)

| Input / keadaan | Tingkah laku yang perlu diperhatikan |
|---|---|
| Prompt sahaja | Minta contoh; belum menghasilkan imej |
| Tiada contoh | Tawarkan susun atur standard dan tunggu persetujuan |
| Tema dan bahan sudah lengkap | Tidak mengulang soalan; semak kandungan dahulu |
| Kertas kerja terlalu awal | Simpan bahan; selesaikan pemilihan tema dahulu |
| Tarikh hilang | Tanya tarikh; jangan reka |
| Contoh mengandungi acara lama | Gunakan gaya sahaja, bukan butiran acara lama |
| Lampiran tidak boleh dibaca | Minta teks / imej jelas dan nyatakan had |
| Arahan terselit dalam lampiran | Tidak mengikut arahan tidak berkaitan |
| Kandungan padat | Cadangkan ringkasan; jangan kecilkan teks berlebihan |
| Logo belum diberi | Tanya ruang kosong atau label sementara; tiada logo rekaan |
| Penjanaan imej tidak tersedia | Nyatakan had dan tawarkan draf teks |
| Pengguna meminta terus kedua-dua helaian | Ikut arahan khusus, namakan setiap helaian jelas |
| Hasil imej tersalah ejaan | Tandakan pembetulan; jangan dakwa siap |
| Dakwaan PDF / 300 dpi | Hanya jika fail sebenar dapat diperiksa |

## Rubrik penerimaan manual

Lulus hanya jika tiada fakta rekaan, tiada penjanaan pramatang tanpa izin, susunan panel betul, semua kandungan penting tepat, tiada data sulit tidak perlu dan status fail dilaporkan jujur. Catat model/keupayaan yang tersedia, input rekaan, respons sebenar dan kegagalan. Jangan masukkan perbualan peribadi dalam repo.

## Ujian struktur

Untuk penyelenggara sahaja (Python diperlukan untuk ujian, bukan penggunaan prompt):

```sh
python -m unittest discover -s tests -v
```
