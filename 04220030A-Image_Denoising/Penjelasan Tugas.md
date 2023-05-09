Tugas : Image Denoising

Langkah-langkah : 
1. Impor library yang diperlukan import cv2
import cv2
2. Baca gambar dengan noise:
image_with_noise = cv2.imread("image_with_noise.jpg")
3. Gunakan metode denoising berbasis filter (misalnya, Bilateral Filter) untuk menghilangkan noise:
denoised_image = cv2.bilateralFilter(image_with_noise, 9, 75, 75)
Dalam contoh di atas, kita menggunakan Bilateral Filter dengan ukuran jendela 9x9 dan parameter sigma yang diatur ke 75.
4. Tampilkan gambar asli dan gambar hasil denoising
cv2.imshow("Original Image", image_with_noise)
cv2.imshow("Denoised Image", denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

Fungsi cv2.imshow() digunakan untuk menampilkan gambar dalam jendela. Fungsi cv2.waitKey(0) menunggu pengguna menekan tombol apa pun untuk menutup jendela gambar. Fungsi cv2.destroyAllWindows() digunakan untuk menghapus semua jendela tampilan.

