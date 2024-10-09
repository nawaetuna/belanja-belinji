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


Tugas Individu 4
1. **Apa itu Django UserCreationForm?**
   **Django UserCreationForm** adalah formulir bawaan Django yang memudahkan pembuatan pengguna baru. Ini adalah bagian dari `django.contrib.auth.forms`, yang menyediakan validasi otomatis dan perlindungan terhadap input berbahaya. Formulir ini biasanya digunakan untuk pendaftaran pengguna.

   **Kelebihan:**
   - **Praktis dan cepat**: Formulir sudah disediakan oleh Django sehingga menghemat waktu pengembangan.
   - **Keamanan terjamin**: Django sudah menangani validasi password dan sanitasi input secara otomatis, membantu mencegah serangan injeksi dan keamanan lainnya.
   - **Mudah dikustomisasi**: Anda bisa menambahkan field tambahan atau mengubah validasi jika diperlukan.

   **Kekurangan:**
   - **Keterbatasan bawaan**: Hanya menangani pembuatan pengguna sederhana. Untuk fitur yang lebih kompleks (seperti email verification atau custom password policies), perlu tambahan logika.
   - **Kurang fleksibel**: Kustomisasi lebih mendalam membutuhkan modifikasi tambahan pada class atau form kustom.

2. **Perbedaan antara Autentikasi dan Otorisasi dalam Konteks Django**
   - **Autentikasi** (authentication) adalah proses memverifikasi identitas pengguna. Misalnya, ketika seorang pengguna memasukkan username dan password, sistem memastikan bahwa informasi yang diberikan cocok dengan yang tersimpan dalam database.
   - **Otorisasi** (authorization) adalah proses menentukan hak akses pengguna setelah berhasil diautentikasi. Ini memastikan bahwa pengguna hanya dapat mengakses sumber daya atau fitur yang diizinkan sesuai dengan peran mereka.

   **Pentingnya Autentikasi dan Otorisasi:**
   - **Keamanan**: Autentikasi memastikan bahwa hanya pengguna terverifikasi yang dapat masuk ke sistem. Otorisasi memastikan bahwa pengguna hanya dapat mengakses data atau fungsi yang relevan dengan peran mereka.
   - **Manajemen Hak Akses**: Dalam aplikasi yang kompleks, otorisasi membantu menjaga akses data sensitif hanya kepada pengguna yang berhak, seperti admin atau pengguna dengan peran tertentu.

3. **Apa itu Cookies dalam Konteks Aplikasi Web?**
   **Cookies** adalah data kecil yang disimpan oleh browser di perangkat pengguna untuk menyimpan informasi sementara. Dalam konteks aplikasi web, cookies sering digunakan untuk mengingat preferensi pengguna, status login, atau data sesi pengguna.

   **Bagaimana Django Menggunakan Cookies untuk Mengelola Data Sesi Pengguna:**
   Django menggunakan cookies untuk menyimpan session ID pengguna. Ketika pengguna masuk, Django menyimpan session ID dalam cookie dan menggunakan ID ini untuk mencocokkan data sesi di server. Dengan cara ini, server dapat mengenali pengguna yang sudah diautentikasi saat mereka melakukan permintaan lebih lanjut, seperti mengakses halaman dashboard setelah login.

4. **Apakah Penggunaan Cookies Aman Secara Default dalam Pengembangan Web?**
   Penggunaan cookies **tidak sepenuhnya aman secara default**, meskipun Django memberikan langkah-langkah keamanan untuk melindungi cookies.

   **Risiko Potensial:**
   - **Session Hijacking**: Jika cookie tidak dilindungi dengan baik, peretas bisa mencuri cookie pengguna dan mendapatkan akses tidak sah ke sesi pengguna.
   - **Cross-Site Scripting (XSS)**: Jika situs web rentan terhadap XSS, penyerang bisa memasukkan skrip berbahaya untuk mencuri cookies pengguna.

   **Langkah Keamanan dalam Django:**
   - **`HttpOnly`**: Menandai cookies dengan flag `HttpOnly` untuk mencegah akses melalui JavaScript.
   - **`Secure`**: Menggunakan flag `Secure` untuk memastikan cookies hanya dikirim melalui koneksi HTTPS.
   - **`CSRF` (Cross-Site Request Forgery)**: Django memiliki perlindungan CSRF untuk mencegah penggunaan cookie sesi secara tidak sah di aplikasi pihak ketiga.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
1. **Registrasi, Login, dan Logout**: Implementasikan formulir registrasi dengan menggunakan `UserCreationForm`, autentikasi pengguna saat login dengan `AuthenticationForm`, dan gunakan fungsi `logout()` untuk menghapus sesi pengguna saat logout.

2. **Dummy Data**: Buat dua akun pengguna di lokal dengan menambahkan tiga data dummy untuk setiap akun, misalnya melalui admin panel atau menggunakan ORM di Django.

3. **Menghubungkan Model Product dengan User**: Tambahkan relasi `ForeignKey` pada model `Product` untuk menghubungkannya dengan model `User`, sehingga setiap produk terkait dengan pemiliknya.

4. **Menampilkan Detail Pengguna Logged In**: Tampilkan detail pengguna yang sedang login, seperti username, di halaman utama menggunakan `request.user`, dan simpan informasi `last_login` di cookies untuk ditampilkan di halaman utama.


### 1. Urutan Prioritas CSS Selector
Urutan prioritas CSS selector, yang dikenal sebagai "specificity," ditentukan berdasarkan beberapa kriteria. Pertama, inline styles memiliki prioritas tertinggi karena diterapkan langsung ke elemen HTML. Selanjutnya, selector ID (dengan tanda `#`) memiliki prioritas lebih tinggi daripada class selectors (dengan tanda `.`) dan pseudo-classes. Setelah itu, class selectors memiliki prioritas lebih tinggi daripada tag selectors, yang merupakan selector dengan nama tag HTML. Terakhir, universal selector (`*`) memiliki prioritas terendah dan akan ditimpa oleh semua jenis selector di atas.

### 2. Pentingnya Responsive Design
Responsive design adalah konsep penting dalam pengembangan aplikasi web karena memastikan tampilan dan fungsionalitas situs web yang optimal di berbagai perangkat dan ukuran layar, mulai dari desktop hingga ponsel pintar. Dengan menggunakan teknik seperti media queries, fleksibel grid layouts, dan gambar responsif, pengguna mendapatkan pengalaman yang lebih baik tanpa perlu menggulir secara horizontal atau memperbesar tampilan. Contoh aplikasi yang sudah menerapkan responsive design adalah Facebook, yang menyesuaikan tampilan antarmukanya sesuai perangkat yang digunakan, sedangkan aplikasi seperti situs web berita tertentu mungkin masih memiliki desain yang tidak responsif dan memerlukan pengguliran horizontal pada perangkat mobile.

### 3. Perbedaan Margin, Border, dan Padding
Margin, border, dan padding adalah tiga konsep dasar dalam CSS yang mempengaruhi ruang dan penempatan elemen. Margin adalah ruang di luar batas elemen yang memisahkannya dari elemen lain, border adalah garis yang mengelilingi elemen dan dapat memiliki warna dan gaya, sedangkan padding adalah ruang di dalam elemen, antara konten dan border. Untuk mengimplementasikannya, Anda dapat menggunakan properti CSS `margin`, `border`, dan `padding` dengan nilai yang sesuai untuk setiap elemen, misalnya `margin: 10px;`, `border: 1px solid black;`, dan `padding: 5px;`.

### 4. Konsep Flexbox dan Grid Layout
Flexbox dan Grid Layout adalah dua metode yang digunakan dalam CSS untuk mendesain layout web. Flexbox dirancang untuk menata elemen dalam satu dimensi, baik secara horizontal maupun vertikal, dengan memberikan kontrol yang lebih besar terhadap ruang dan penempatan elemen dalam kontainer flex. Di sisi lain, Grid Layout memungkinkan pengaturan elemen dalam dua dimensi (baris dan kolom), memberikan fleksibilitas yang lebih besar untuk menciptakan tata letak kompleks. Keduanya berguna untuk membangun antarmuka pengguna yang responsif dan terstruktur dengan baik, dengan memudahkan penyelarasan, distribusi ruang, dan pengaturan elemen.

### 5. Implementasi Checklist
Untuk mengimplementasikan checklist di atas secara step-by-step, pertama, saya akan mempelajari setiap konsep dengan membaca dokumentasi resmi CSS dan tutorial online. Setelah memahami dasar-dasar, saya akan membuat proyek sederhana untuk menerapkan urutan prioritas CSS dengan menulis beberapa contoh selector dan menguji bagaimana mereka berinteraksi di browser. Selanjutnya, saya akan merancang layout responsif dengan menggunakan media queries, flexbox, dan grid layout pada proyek tersebut. Saya juga akan bereksperimen dengan margin, border, dan padding pada elemen-elemen dalam proyek untuk melihat dampaknya terhadap layout. Terakhir, saya akan mereview dan menguji proyek di berbagai perangkat dan ukuran layar untuk memastikan responsivitasnya.


README TUGAS INDIVIDU 6

### 1. **Manfaat Penggunaan JavaScript dalam Pengembangan Aplikasi Web**
   JavaScript memberikan kemampuan untuk membuat halaman web yang interaktif dan dinamis. Manfaat utamanya antara lain:
   - **Asynchronous Operations**: Dengan JavaScript, kita bisa menggunakan AJAX untuk melakukan permintaan ke server tanpa perlu me-reload halaman, sehingga meningkatkan pengalaman pengguna.
   - **Client-Side Validation**: JavaScript dapat digunakan untuk memvalidasi input pengguna sebelum data dikirim ke server, mengurangi beban pada server.
   - **Interactivity**: JavaScript memungkinkan manipulasi elemen DOM untuk membuat UI yang responsif dan interaktif, seperti dropdown menus, modal windows, sliders, dan lain-lain.
   - **Improved User Experience**: Dengan interaksi instan, seperti auto-suggestions dan form validation, JavaScript dapat membuat aplikasi web terasa lebih responsif dan cepat.

### 2. **Fungsi `await` pada `fetch()`**
   Fungsi `await` digunakan untuk menunggu hasil dari sebuah Promise, termasuk `fetch()`, yang mengembalikan Promise saat melakukan request HTTP. `await` membuat JavaScript "menunggu" hingga fetch selesai dan memberikan respon sebelum melanjutkan eksekusi kode berikutnya.
   
   **Tanpa `await`,** kode akan langsung melanjutkan eksekusi tanpa menunggu hasil dari `fetch()`, sehingga kita tidak akan bisa bekerja dengan data yang diterima dari server jika proses asynchronous belum selesai. Ini bisa menyebabkan error karena data yang diharapkan mungkin belum tersedia.

### 3. **Mengapa Perlu `csrf_exempt` untuk AJAX POST**
   Decorator `csrf_exempt` digunakan untuk menonaktifkan mekanisme Cross-Site Request Forgery (CSRF) protection di Django pada view tertentu, khususnya untuk request AJAX POST. AJAX POST request mungkin tidak membawa token CSRF secara default, sehingga Django akan memblokirnya tanpa `csrf_exempt`. Namun, untuk menjaga keamanan, pastikan hanya menonaktifkan CSRF untuk endpoint yang aman atau pastikan token CSRF dikirim dalam header AJAX.

### 4. **Mengapa Pembersihan Data Input Pengguna Dilakukan di Backend**
   Pembersihan data di backend sangat penting karena:
   - **Keamanan**: Data yang masuk ke server bisa saja dimanipulasi oleh pengguna yang tidak bertanggung jawab. Pembersihan data di backend memastikan bahwa input yang masuk ke server benar-benar sesuai dan aman, menghindari potensi serangan seperti SQL injection atau XSS (Cross-site Scripting).
   - **Integritas Data**: Validasi di backend menjaga bahwa data yang disimpan dalam basis data memiliki format yang benar dan sesuai aturan, meskipun validasi front-end diabaikan atau diubah oleh pengguna.
   - **Redundansi**: Meskipun validasi frontend bisa dilakukan untuk meningkatkan pengalaman pengguna, validasi backend tetap wajib karena frontend validation dapat di-bypass oleh pengguna berpengalaman.

### 5. **Implementasi Checklist Step-by-Step**
   - **AJAX GET**: Saya menambahkan view baru yang menggunakan Django's `JsonResponse` untuk mengirim data mood pengguna yang sedang login. JavaScript di frontend kemudian melakukan request GET menggunakan `fetch()` untuk mengambil data ini dan memperbarui tampilan halaman tanpa reload.
   
   - **AJAX POST**: Saya membuat modal dengan form untuk menambahkan mood, yang terhubung dengan endpoint POST di server. Tombol untuk membuka modal diatur di halaman utama, dan saat submit berhasil, saya menggunakan `JavaScript` untuk menutup modal dan membersihkan input form. Jika terjadi error, error message akan ditampilkan pada modal tanpa perlu reload halaman.

   - **Path & View**: Saya membuat URL `/create-ajax/` di `urls.py` yang terhubung dengan fungsi view baru di `views.py` untuk menangani POST request mood baru. Form di modal mengirimkan data ke path tersebut secara asynchronous menggunakan `fetch()` POST request.

   - **Refresh Asynchronous**: Setelah mood berhasil ditambahkan, saya menggunakan JavaScript untuk memuat ulang daftar mood secara asynchronous, sehingga mood terbaru ditampilkan tanpa reload seluruh halaman.