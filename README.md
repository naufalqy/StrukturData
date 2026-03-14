# 1. Penjelasan Konsep Array

Array adalah struktur data yang digunakan untuk menyimpan sekumpulan data dengan tipe yang sama dalam satu variabel. Data dalam array disimpan secara berurutan di dalam memori dan setiap elemen memiliki indeks yang digunakan untuk mengakses data tersebut.

Indeks pada array biasanya dimulai dari angka 0. Dengan menggunakan array, kita dapat mengelola banyak data dengan lebih efisien dibandingkan membuat variabel satu per satu.

Pada program ini array digunakan untuk menyimpan **10 nilai siswa** yang kemudian diproses untuk mencari nilai tertinggi, nilai terendah, rata-rata nilai, serta jumlah siswa yang lulus.

--

# 2. Tangkapan Layar Hasil

## Hasil Program

![Hasil Program](https://github.com/naufalqy/gambar/blob/d7f4d1c65773333a36a3e624868a51a69b0b2984/screenshot_program.png)

## Grafik Nilai

![Grafik Nilai](https://github.com/naufalqy/gambar/blob/d7f4d1c65773333a36a3e624868a51a69b0b2984/screenshot_grafik1.png)

## Grafik Kelulusan

![Grafik Kelulusan](https://github.com/naufalqy/gambar/blob/d7f4d1c65773333a36a3e624868a51a69b0b2984/screenshot_grafik2.png)

--

# 3. Analisis Kompleksitas

Berikut adalah analisis kompleksitas dari setiap operasi pada program:

### Input nilai siswa
Kompleksitas: **O(n)**  
Program melakukan perulangan untuk memasukkan nilai ke dalam array sebanyak jumlah data yang dimasukkan.

### Mencari nilai tertinggi
Kompleksitas: **O(n)**  
Program harus memeriksa setiap elemen dalam array untuk menentukan nilai terbesar.

### Mencari nilai terendah
Kompleksitas: **O(n)**  
Program memeriksa seluruh elemen array untuk menentukan nilai terkecil.

### Menghitung rata-rata
Kompleksitas: **O(n)**  
Semua nilai dalam array dijumlahkan terlebih dahulu sebelum dibagi dengan jumlah data.

### Menghitung jumlah siswa lulus
Kompleksitas: **O(n)**  
Program memeriksa setiap nilai apakah memenuhi syarat kelulusan (≥ 60).

### Akses elemen array
Kompleksitas: **O(1)**  
Akses elemen array menggunakan indeks dapat dilakukan secara langsung.

Dari analisis tersebut dapat disimpulkan bahwa sebagian besar operasi dalam program memiliki kompleksitas **O(n)** karena harus memproses seluruh data dalam array.

---

# 4. Refleksi Pembelajaran

Melalui tugas ini saya menjadi lebih memahami konsep dasar struktur data array dan bagaimana array digunakan untuk menyimpan serta mengolah banyak data secara efisien.

Saya juga belajar bagaimana melakukan beberapa operasi dasar pada array seperti mencari nilai maksimum, nilai minimum, menghitung rata-rata, serta melakukan pengecekan kondisi untuk menentukan kelulusan siswa.

Selain itu, saya juga belajar membuat grafik sederhana menggunakan Python untuk menampilkan data secara visual. Dengan adanya grafik, informasi yang diperoleh dari data dapat lebih mudah dipahami.

Tugas ini membantu saya memahami bahwa struktur data merupakan bagian penting dalam pemrograman karena dapat mempermudah pengolahan data dalam jumlah besar.
