# Plugin Buku Program AI

Pakej berada dalam `plugins/buku-program-ai/`. Ia membundel manifest portable, satu skill dan kedua-dua imej contoh. Tiada MCP server, API key, hook atau automasi pelayar.

## Status sebenar

Pakej telah dibina; pemasangan dan penjanaan dalam ChatGPT belum diuji. Ia belum dihantar untuk semakan atau diterbitkan dalam direktori plugin awam. Repo GitHub bukan bukti plugin sudah dipasang.

## Ujian pemasangan desktop

Mengikut dokumentasi rasmi, gunakan repo marketplace `.agents/plugins/marketplace.json`. Jika Codex CLI yang menyokong plugin tersedia:

```sh
codex plugin marketplace add firdaushadi442/buku-program-ai --ref main
```

Kemudian gunakan aplikasi desktop ChatGPT yang menyokong marketplace itu untuk mencari dan memasang Buku Program AI daripada sumber marketplace tersebut. Restart aplikasi mengikut keperluan klien dan uji dalam perbualan baharu. Jangan menganggap langkah CLI ini memasang plugin ke akaun ChatGPT web.

Alternatif: berikan folder pakej kepada Plugin Creator untuk menyediakan pemasangan ujian. Jika akaun/klien tidak menyediakan ciri ini, pakej belum boleh diuji di situ.

## Ujian penerimaan manual

- Plugin muncul dan boleh dipilih selepas pemasangan.
- Arahan skill dibaca, bukan sekadar ringkasan repo.
- Kedua-dua imej dibuka sebagai imej; jika tidak boleh, AI menyatakan hadnya.
- AI meminta tema dan maklumat yang belum lengkap.
- Maklumat cukup: terus jana helaian luar tanpa kelulusan teks tambahan.
- Selepas semakan pengguna, helaian dalam dijana.
- Tiada dakwaan fail siap jika fail tidak wujud.

Bundling tidak menjamin klien menyediakan fungsi membaca imej atau penjanaan poster. Catat keputusan sebenar sebelum menganggap plugin berfungsi hujung-ke-hujung.

## Dokumentasi rasmi

https://developers.openai.com/plugins/build/plugins

Lesen teks: MIT. Imej rujukan tertakluk pada `assets/NOTICE.md` dalam skill, bukan MIT.
