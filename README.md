# Eye-State-Prediction

### Türkçe: 
Eye-State-Prediction, gerçek zamanlı olarak gözlerin açık mı kapalı mı olduğunu tahmin eden bir uygulamadır. Uygulama, kameradan alınan görüntülerde yüz ve göz tespiti yaparak, her iki gözün durumunu ayrı ayrı sınıflandırır.

## 🚀 Özellikler
- Gerçek zamanlı göz durumu tahmini  
- Gözlerin açık/kapalı olduğunu sınıflandıran model  
- Veri toplama ve model eğitimi  
- Kamera ile canlı izleme ve tahmin

## 📁 Kod Yapısı

### 1. `eye_tracking_data_collection.py`
Kullanıcıdan kamera aracılığıyla yüz verisi alır, gözlerin açık/kapalı olduğunu tespit ederek `dataset.csv` dosyasına veri olarak kaydeder. Bu veriler model eğitimi için kullanılır.

### 2. `real_time_prediction_model.py`
Toplanan verilerle bir makine öğrenmesi modeli (Logistic Regression) eğitilir. Daha sonra bu model ile gerçek zamanlı tahmin yapılır ve tahminler ekranda görüntülenir.

### 3. `model_accuracy_and_predictions.py`
Modelin doğruluğunu ölçmek için test verileriyle tahminler yapılır. Sol ve sağ göz için doğruluk oranları ayrı ayrı hesaplanır ve raporlanır.

## 🧠 Kullanılan Teknolojiler
- Python 3.x  
- OpenCV  
- dlib  
- scikit-learn  

## ⚠️ Notlar
- `shape_predictor_68_face_landmarks.dat` dosyası 95 MB büyüklüğündedir. Bu dosyayı yüklemek için Git LFS (Large File Storage) kullanmanız önerilir.

## 📸 Tahmin Formatı
- `1 1` → Sol ve sağ göz açık  
- `0 0` → Sol ve sağ göz kapalı  
- `1 0` → Sol göz açık, sağ göz kapalı  
- `0 1` → Sol göz kapalı, sağ göz açık


### English: 
Eye-State-Prediction is a real-time application that predicts whether the eyes are open or closed. The app detects faces and eyes from a camera feed and classifies the state of both eyes individually.

## 🚀 Features
- Real-time eye state prediction  
- A model that classifies eyes as open or closed  
- Data collection and model training  
- Live video tracking and prediction

## 📁 Code Structure

### 1. `eye_tracking_data_collection.py`
Captures facial data via the camera and determines whether the eyes are open or closed. The data is saved in `dataset.csv` and later used to train a model.

### 2. `real_time_prediction_model.py`
Trains a machine learning model (Logistic Regression) using the collected data. Then, it performs real-time predictions and displays the results on screen.

### 3. `model_accuracy_and_predictions.py`
Evaluates the model's performance on test data. Accuracy rates are calculated separately for the left and right eyes and reported.

## 🧠 Technologies Used
- Python 3.x  
- OpenCV  
- dlib  
- scikit-learn  

## ⚠️ Notes
- The `shape_predictor_68_face_landmarks.dat` file is 95 MB. It is recommended to use Git LFS (Large File Storage) to upload this file.

## 📸 Prediction Format
- `1 1` → Both eyes open  
- `0 0` → Both eyes closed  
- `1 0` → Left eye open, right eye closed  
- `0 1` → Left eye closed, right eye open
