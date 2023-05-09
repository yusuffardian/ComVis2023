import cv2

# Baca gambar dengan noise
image_with_noise = cv2.imread("gambar/router.jpg")

# Denoising menggunakan metode Bilateral Filter
denoised_image = cv2.bilateralFilter(image_with_noise, 9, 75, 75)

# Tampilkan gambar asli dan hasil denoising
cv2.imshow("Original Image", image_with_noise)
cv2.imshow("Denoised Image", denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
