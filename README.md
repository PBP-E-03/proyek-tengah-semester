## Nama-nama Anggota Kelompok
- Adjie Djaka Permana
- Muhammad Reyvan Natechnoury
- Dhafiano Fadeyka Ghani Wiweko
- Muhammad Nabil Mahardika
- Trias Ahmad Fairuz

## Tautan aplikasi Heroku
https://pbp-e-03.herokuapp.com/

## Cerita aplikasi yang diajukan serta manfaatnya
Dalam usaha melawan emisi karbon yang terus meningkat, kami menyediakan sebuah website yang memungkinkan semua orang untuk melakukan donasi pohon pada lokasi tertentu di Indonesia. Selain memungkinkan donasi pohon, kami menyediakan insentif kepada orang-orang yang melakukan donasi berupa koin yang dapat ditukarkan dengan berbagai macam barang yang bermanfaat. Barang-barang yang kami sediakan di marketplace juga selaras dengan tujuan utama kami, yaitu melawan emisi karbon, beberapa contohnya adalah: tumblr, shopping bag, dan tempat makan. Insentif lain untuk mendorong para pengguna melakukan donasi adalah adanya leaderboard yang mengurutkan pengguna berdasarkan jumlah lokasi pada lokasi tertentu. Dengan insentif-insentif tersebut, ditambah dengan tampilan aplikasi yang menarik, kami harap website ini dapat berkontribusi terhadap jumlah donasi pohon yang dilakukan di Indonesia.



## Daftar modul yang akan diimplementasikan
- Implementasi User dan Profile -> Adjie  
Modul ini meliputi semua keperluan implementasi user, diantaranya:
    - Login, untuk memberikan autorisasi terhadap user yang sudah terdaftar.
    - Registrasi, untuk mendaftarkan akun user yang baru
    - Logout, untuk keluar dari suatu sesi 

    Selain implementasi user, terdapat juga implementasi profil yang berkaitan tentang website ini, hal-hal tersebut dalam bentuk:  
    - Tampilan data sebuah user, seperti user name, password, koin, dan field-field lain yang dimiliki sebuah user.
    - Pengaturan untuk mengubah username dan password, serta field lain yang diperlukan.  
    - Riwayat transaksi donasi pohon, sekaligus menunjukkan laporan bulanan berupa jumlah donasi pohon yang telah dilakukan.


- Donasi Pohon -> Trias  
Modul ini meliputi semua yang berkaitan dengan donasi pohon. Hal tersebut meliputi:
    - Form untuk jumlah donasi pohon yang diinginkan.
    - Pemilihan metode pembayaran yang diinginkan, serta pengunggahan bukti (tidak diimplementasikan secara nyata, dalam artian hanya berdasarkan jumlah input pada form)
    - Pemilihan lokasi donasi pohon dari sejumlah lokasi yang sudah ditentukan.
    - Setelah sebuah user melakukan donasi pohon, user tersebut akan mendapatkan poin yang proporsional dengan jumlah donasi pohon.

- Marketplace -> Reyvan  
Modul ini meliputi semua keperluan sebuah marketplace, yang berfungsi seperti sebuah e-commerce, hal-hal tersebut diantaranya:
    - Tampilan barang-barang yang tersedia
    - Fitur keranjang belanja untuk menyimpan sejumlah barang-barang pada marketplace.
    - Fitur untuk membeli barang tersebut, yang mencakup form untuk menentukan kuantitas serta bukti transaksi.

- Leaderboard -> Dhafiano  
Modul ini mencakup hal-hal yang berkaitan dengan leaderboard, antara lain:
    - Tampilan leaderboard berupa user-user dengan jumlah donasi terbanyak pada lokasi tertentu
    - Form yang bisa digunakan untuk menentukan lokasi mana yang ingin dilihat leaderboardnya.

- Pusat Bantuan -> Nabil  
Modul ini berisi semua hal tentang pusat bantuan
    - Form yang berlaku seperti search bar untuk mencari bantuan mengenai hal spesifik.
    - Tampilan dan sejumlah Frequently Asked Questions


## Role atau peran pengguna beserta deskripsinya (karena bisa saja lebih dari satu jenis pengguna yang mengakses aplikasi)
- super admin
super admin dapat mengakses semua fitur aplikasi dalam segi administrasi tanpa memandang hak akses.

- admin
admin dapat mengakses fitur aplikasi dalam segi administrasi sesuai dengan hak akses yang diberikan.

- end user
pengguna aplikasi dapat menggunakan semua fitur yang tersedia dalam aplikasi apabila telah terdaftar
