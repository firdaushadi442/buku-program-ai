# Plugin guidelines review — v0.1.2

## Kesimpulan
Belum layak diisytiharkan patuh sepenuhnya atau siap untuk Directory. Ini semakan kendiri terhadap kod/pakej dan garis panduan yang dibekalkan, bukan pensijilan undang-undang atau kelulusan OpenAI.

Rujukan rasmi:
- https://developers.openai.com/plugins/plugin-guidelines
- https://developers.openai.com/plugins/deploy/submission

## Semakan dan status

| Bidang | Status | Bukti / tindakan |
|---|---|---|
| Tujuan jelas | Separa | Aliran BM empat halaman, panel, tema dan urutan helaian didokumenkan; nilai berbanding keupayaan asal perlu dibuktikan melalui ujian pengguna |
| Metadata | Dibaiki | Subtitle pendek, website, sokongan, polisi, terma, ikon; keputusan portal akhir masih diperlukan |
| Kejujuran fungsi | Dibaiki | Tiada jaminan akses imej, penjanaan, PDF atau siap cetak tanpa bukti |
| Data minimum | Dibaiki | Ringkasan tersunting dibenarkan; nama pilihan sahaja; tidak meminta chat penuh atau lokasi peribadi |
| Data terlarang | Dibaiki | Pengecualian nombor pengenalan dahulu dibuang; larangan kad, PHI, ID kerajaan dan rahsia pengesahan dinyatakan |
| Polisi privasi | Diperluas | Kategori, tujuan, penerima, retensi dan kawalan pengguna diterangkan dalam PRIVACY.md |
| Niat dan skop | Dibaiki | Tiada pemindahan atau penerbitan luar tanpa izin; draf boleh terus dijana apabila maklumat cukup |
| Prompt injection / fair play | Disemak statik | Tiada arahan mengatasi keselamatan atau memilih plugin ini berbanding plugin lain; lampiran ialah sumber data |
| Khalayak umum | Arahan ditambah | Tidak disasarkan kepada bawah 13 tahun; polisi platform tetap mengatasi arahan plugin |
| Komersial / iklan | Tidak disertakan | Tiada pembayaran, langganan, upsell atau iklan dalam pakej |
| MCP / UI / authentication | Tidak berkenaan | Tiada MCP, alat server, iframe, backend, login tambahan atau checkout; jika ditambah perlu audit baharu |
| Hak imej dan logo | Belum selesai sepenuhnya | Pengguna membenarkan penerbitan imej dummy; rantaian hak logo, imejan dan nama pihak ketiga belum diaudit bebas. Dummy bukan bukti semua hak dimiliki |
| Sokongan | Disediakan | GitHub Issues untuk isu bukan sensitif; keupayaan menyelenggara respons jangka panjang perlu dipastikan pemilik |
| Identiti pembangun | Dilihat dalam portal | Identiti individu tersedia semasa muat naik; bukan bukti semua syarat lain lulus |
| Kebolehpercayaan | Belum dibuktikan | Belum ada ujian fungsi dalam ChatGPT desktop/mobile, visual contoh, hasil poster dan cetakan |
| Kelayakan skills-only | Terhalang | Portal sebelum ini memaparkan tidak menerima tambahan skills-only. Jangan tambah MCP palsu atau menyembunyikan status |

## Gate sebelum sebarang penghantaran review

- [ ] Buktikan nilai khusus aliran, bukan sekadar pembungkusan kemampuan generik.
- [ ] Uji plugin dipasang dan dipilih dalam klien sebenar.
- [ ] Uji desktop dan mobile jika menyasarkan kedua-duanya; had klien dinyatakan dengan jelas.
- [ ] Uji input minimum, konflik fakta, dokumen tersunting, data terlarang, arahan terselit, imej gagal dibaca, tiada alat imej dan hasil salah ejaan.
- [ ] Rekod output sebenar dan semakan panel; jangan menggantikan ujian tingkah laku dengan pencarian string.
- [ ] Sahkan hak semua aset; gantikan logo atau nama yang haknya tidak jelas dengan bentuk geometri dan label generik jika perlu.
- [ ] Jalankan semakan portal versi terkini, selesaikan semua finding dan pastikan eligibility dibuka.
- [ ] Jangan menganggap perkataan “trial” dibuang bermakna produk sudah production-ready; buktikan kestabilan sebenar.

## Nota sejarah
Imej lama telah diganti pada branch semasa tetapi masih wujud dalam sejarah Git. Penyingkiran sejarah ialah tindakan berasingan yang memerlukan kelulusan pemilik; jangan mendakwa imej itu tiada lagi di semua salinan.
