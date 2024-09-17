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


Tugas Individu 3
1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan untuk memastikan data yang dikirimkan dan diterima antara berbagai komponen dalam platform dapat diakses dengan cepat dan akurat. Ini penting untuk menjaga integritas data, efisiensi dalam komunikasi antar sistem, dan mendukung pengalaman pengguna yang lancar.

2. Mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih baik daripada XML dalam hal kesederhanaan dan efisiensi. JSON menggunakan format yang lebih ringkas, lebih mudah dibaca manusia, dan lebih cepat diproses oleh mesin. JSON populer karena strukturnya lebih sederhana, cocok untuk pertukaran data yang ringan seperti API modern, sementara XML lebih berat dan sering digunakan untuk kasus yang lebih kompleks atau memerlukan validasi skema yang ketat.

3. Fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkannya?
Method is_valid() pada form Django digunakan untuk memeriksa apakah data yang diinputkan ke dalam form memenuhi syarat validasi yang telah ditentukan. Method ini penting karena memastikan bahwa data yang diterima aplikasi adalah benar dan aman sebelum diproses lebih lanjut, seperti menyimpannya ke dalam database.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django?
csrf_token dibutuhkan untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery), di mana penyerang dapat membuat permintaan berbahaya yang tampak sah dari pengguna yang sudah login. Jika kita tidak menambahkan csrf_token, penyerang dapat memanfaatkan celah ini untuk mengirim permintaan palsu atas nama pengguna tanpa izin mereka, seperti mengubah data atau melakukan tindakan sensitif lainnya di platform.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Membuat Input Form untuk Menambahkan Objek Model
Pertama, buat form menggunakan ModelForm yang berdasarkan model yang ingin ditambahkan. Setelah form dibuat, tambahkan view untuk menampilkan form ini dan meng-handle input dari user. Buat template HTML sederhana untuk menampilkan form di frontend. Di view, pastikan form dapat menambahkan objek baru ke database saat data valid dikirimkan oleh user.

Menambahkan 4 Fungsi Views untuk Format XML dan JSON
Buat empat views baru di mana dua view untuk menampilkan semua objek dalam format XML dan JSON, dan dua view lainnya untuk menampilkan objek berdasarkan ID-nya. Gunakan serialisasi data di Django untuk mengubah objek ke dalam format XML dan JSON. Untuk menampilkan objek berdasarkan ID, tambahkan logika query yang memfilter objek sesuai ID yang diberikan.

Membuat Routing URL untuk Setiap Views
Tambahkan URL routing untuk masing-masing view di file urls.py. Buat empat endpoint terpisah, misalnya /products/xml/, /products/json/, /products/xml/<id>/, dan /products/json/<id>/, sehingga setiap view bisa diakses melalui URL yang sesuai.

Jangan lupa untuk selalu migrate, setiap melakukan perubahan di models.py karena kmrn pas saya mengganti nama kelas dari Product menjadi productEntry dan lupa migrate saat mau runserver, keluarnya Operational Error !!

![Screenshot 2024-09-16 204822](https://github.com/user-attachments/assets/02cdc4ac-95ed-47b4-a553-16666c0e926d)
![Screenshot 2024-09-16 201941](https://github.com/user-attachments/assets/503d245e-2ceb-46ec-b746-896709705e9e)
![Screenshot 2024-09-16 201958](https://github.com/user-attachments/assets/9dc33236-2583-436a-9186-0843172b8427)
![Screenshot 2024-09-16 204656](https://github.com/user-attachments/assets/68c9d9af-f431-45fe-a3e7-9f2b9c4a54d1)
