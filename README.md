LINK PwS : http://nawaetuna-belanjabelinji.pbp.cs.ui.ac.id/

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

Mengaktifkan Virtual Environment dan Menyiapkan Dependencies
Aktifkan virtual environment dan install dependencies dari requirements.txt.

Menyiapkan .gitignore
Tambahkan file .gitignore untuk mengabaikan file yang tidak perlu di-upload ke GitHub.

Membuat Proyek Django
Buat proyek Django dengan nama belanja_belinji.

Membuat Aplikasi main
Tambahkan aplikasi baru bernama main di dalam proyek.

Menghubungkan Aplikasi main dengan Proyek
Tambahkan aplikasi main ke dalam pengaturan proyek di settings.py.

Membuat Model Product

Buat model Product dengan atribut name, price, description dan quantity.

Melakukan Migrasi Database
Jalankan perintah untuk membuat tabel Product di database.

Membuat View untuk Menampilkan Template
Buat fungsi home di views.py untuk menampilkan halaman dengan informasi aplikasi dan data pribadi.

Membuat Template HTML
Buat file main.html untuk menampilkan informasi dari view.

Menambahkan Routing di urls.py
Atur routing di urls.py agar URL mengarah ke fungsi home.

Melakukan Commit dan Push ke Repository GitHub
Simpan perubahan, commit, dan push ke repository GitHub.

Deployment ke PWS
Deploy aplikasi ke platform hosting seperti Heroku atau Railway.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
  +------------------+        +---------------------+       +----------------+       +------------------+        +------------------+
  |  Client (Browser) | -----> |      urls.py        | ----> |    views.py    | ----> |     models.py     | ----> |    Template (HTML)|
  +------------------+        +---------------------+       +----------------+       +------------------+        +------------------+
          |                           |                           |                      |                              |
          |                           |                           |                      |                              |
      Request URL                 Mapping URL                 Business Logic        Database Queries               Render HTML
Client (Browser): Pengguna mengirimkan permintaan HTTP (GET, POST, dll.) melalui URL yang spesifik.

urls.py: Django memetakan URL yang diminta oleh pengguna ke view yang sesuai. Setiap URL yang dikirim client dicek apakah ada pola yang sesuai dalam urls.py.

views.py: Setelah URL ditemukan, Django mengirimkan request ke views.py. Di sini, logika aplikasi dan pemrosesan data dilakukan, termasuk mengambil atau memodifikasi data dari database dengan bantuan models.py.

models.py: Jika views.py memerlukan data dari database, ia akan mengakses model yang sudah dibuat di models.py. Django ORM (Object-Relational Mapping) berperan untuk memetakan objek Python ke tabel-tabel di database.

Template (HTML): Setelah data diproses di views.py, hasilnya dikirimkan ke template (file HTML) untuk dirender dan dikirim kembali sebagai respons ke browser pengguna.

Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git adalah sistem kontrol versi yang memungkinkan developer melacak perubahan pada file, memfasilitasi kerja tim, dan menjaga riwayat proyek. Dengan Git, berbagai versi file disimpan, memungkinkan pengembang mengembalikan versi sebelumnya jika terjadi kesalahan. Git juga mendukung kolaborasi dengan fitur branching dan merging, memungkinkan beberapa developer bekerja secara paralel tanpa bentrok. Setiap perubahan dapat dilacak berdasarkan siapa yang membuatnya dan kapan, serta repositori proyek dapat disimpan di server untuk backup. Branching memungkinkan pengembangan fitur atau perbaikan bug terpisah yang dapat digabungkan kembali ke versi utama.

Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dipilih sebagai framework awal untuk belajar pengembangan perangkat lunak karena sudah menyediakan banyak fitur bawaan, seperti autentikasi, manajemen sesi, ORM, dan routing URL, yang memudahkan pemula. Sebagai full-stack framework, Django memungkinkan developer belajar front-end dan back-end sekaligus. Django juga menggunakan banyak standar yang jelas, sehingga pemula bisa fokus mengembangkan tanpa perlu banyak konfigurasi. Ditambah lagi, Django punya komunitas yang besar dan dokumentasi lengkap, jadi memudahkan siapa saja yang baru belajar untuk menemukan bantuan atau tutorial.

Mengapa model pada Django disebut sebagai ORM?
Model pada Django disebut ORM (Object-Relational Mapping) karena berfungsi sebagai penghubung antara objek Python dan tabel dalam database. Dengan ORM, developer bisa berinteraksi dengan database hanya menggunakan kode Python, tanpa harus menulis query SQL. Django otomatis mengubah objek Python menjadi query SQL dan sebaliknya. Keuntungan ORM adalah pengembang tidak perlu mempelajari SQL secara mendalam, dapat menggunakan berbagai jenis database dengan mudah, serta lebih aman karena ORM membantu mencegah serangan seperti SQL Injection.