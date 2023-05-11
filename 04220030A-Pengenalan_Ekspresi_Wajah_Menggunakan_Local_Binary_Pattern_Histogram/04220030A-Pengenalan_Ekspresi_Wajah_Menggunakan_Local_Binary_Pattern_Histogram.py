import cv2
import numpy as np
import os

# Fungsi untuk mengekstraksi fitur LBP Histogram
def lbp_histogram(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    lbp = cv2.textureLBP(gray)
    hist, _ = np.histogram(lbp.ravel(), bins=np.arange(0, 256), range=(0, 256))
    hist = hist.astype("float")
    hist /= (hist.sum() + 1e-7)
    return hist

# Mendefinisikan array untuk menyimpan fitur dan label
features = []
labels = []

# Mendapatkan daftar folder yang berisi dataset ekspresi wajah
expression_folders = os.listdir('dataset')

# Iterasi melalui setiap folder
for folder in expression_folders:
    # Mendapatkan path folder
    folder_path = os.path.join('dataset', folder)
    
    # Mendapatkan daftar file gambar di dalam folder
    image_files = os.listdir(folder_path)
    
    # Iterasi melalui setiap file gambar
    for image_file in image_files:
        # Mendapatkan path file gambar
        image_path = os.path.join(folder_path, image_file)
        
        # Membaca gambar
        image = cv2.imread(image_path)
        
        # Ekstraksi fitur LBP
        hist = lbp_histogram(image)
        
        # Menambahkan fitur dan label ke dalam array
        features.append(hist)
        labels.append(folder)  # Menggunakan nama folder sebagai label

# Mengubah array fitur dan label ke dalam format NumPy
features = np.array(features)
labels = np.array(labels)

# Melatih model KNN
knn = cv2.ml.KNearest_create()
knn.train(features, cv2.ml.ROW_SAMPLE, labels)

# Mendefinisikan daftar label ekspresi wajah
expression_labels = ['senang', 'sedih', 'marah']

# Fungsi untuk memprediksi ekspresi wajah dari gambar
def predict_expression(image):
    hist = lbp_histogram(image)
    hist = np.array([hist])
    _, result, _, _ = knn.findNearest(hist, k=3)
    predicted_label = expression_labels[int(result[0][0])]
    return predicted_label

# Contoh penggunaan
test_image_path = 'test_image.jpg'
test_image = cv2.imread(test_image_path)
predicted_expression = predict_expression(test_image)
print("Ekspresi Wajah:", predicted_expression)
