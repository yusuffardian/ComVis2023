Langkah 1: Persiapan Dataset
- Kumpulkan dataset ekspresi wajah yang berisi gambar-gambar dengan label ekspresi yang sesuai (misalnya, senang, sedih, marah, dll.).
- Pisahkan gambar-gambar tersebut ke dalam folder-folder yang sesuai dengan label ekspresinya.

Langkah 2: Ekstraksi Fitur LBP Histogram
- Impor library OpenCV dan NumPy.
- Buat sebuah fungsi `lbp_histogram(image)` yang mengambil gambar sebagai input dan mengembalikan histogram LBP dari gambar tersebut.
- Di dalam fungsi `lbp_histogram`, ubah gambar ke dalam skala keabuan menggunakan `cv2.cvtColor()` dengan parameter `cv2.COLOR_BGR2GRAY`.
- Terapkan operator LBP pada gambar menggunakan `cv2.textureLBP()`.
- Hitung histogram LBP menggunakan `np.histogram()`. Pastikan untuk mengubah tipe data histogram menjadi float dan melakukan normalisasi dengan membaginya dengan jumlah total elemen histogram.
- Kembalikan histogram yang dihitung.

Langkah 3: Melatih Model Pengenalan Ekspresi Wajah
- Mendefinisikan array untuk menyimpan fitur dan label.
- Gunakan `os.listdir()` untuk mendapatkan daftar folder yang berisi dataset ekspresi wajah.
- Lakukan iterasi melalui setiap folder untuk mendapatkan path folder dan daftar file gambar di dalamnya.
- Lakukan iterasi melalui setiap file gambar dan baca gambar menggunakan `cv2.imread()`.
- Gunakan fungsi `lbp_histogram()` untuk menghitung fitur LBP histogram dari gambar.
- Tambahkan fitur dan label ke dalam array yang telah didefinisikan sebelumnya.
- Ubah array fitur dan label ke dalam format NumPy menggunakan `np.array()`.
- Inisialisasi model pengenalan ekspresi wajah, seperti K-Nearest Neighbors (KNN), dengan menggunakan `cv2.ml.KNearest_create()`.
- Latih model menggunakan `knn.train()` dengan fitur-fitur yang diekstraksi dan label-labelnya.

Langkah 4: Menguji Model Pengenalan Ekspresi Wajah
- Definisikan daftar label ekspresi wajah yang sesuai dengan dataset Anda.
- Buat sebuah fungsi `predict_expression(image)` yang mengambil gambar sebagai input dan mengembalikan prediksi ekspresi wajah dari gambar tersebut.
- Di dalam fungsi `predict_expression`, ekstraksi fitur LBP histogram dari gambar menggunakan fungsi `lbp_histogram()`.
- Ubah fitur menjadi array NumPy dengan dimensi 2D menggunakan `np.array([hist])`.
- Gunakan `knn.findNearest()` untuk memprediksi label ekspresi dengan mengambil nilai k terdekat dari hasil prediksi.
- Konversi nilai hasil prediksi ke dalam tipe data integer dan gunakan sebagai indeks dalam daftar label ekspresi untuk mendapatkan prediksi akhir.
- Kembalikan prediksi ekspresi.

Langkah 5: Pengujian
- Tentukan path ke gambar yang ingin Anda gunakan untuk pengujian.
- Baca gambar menggunakan `cv2.imread()