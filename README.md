# Eye-State-Prediction

Eye-State-Prediction, gerçek zamanlı göz durumu tahminini yapabilen bir uygulamadır. Bu uygulama, kameradan alınan yüz görüntülerine göre gözlerin açık mı kapalı mı olduğunu tahmin eder. Model, kullanıcıdan alınan yüz verilerini kullanarak gözlerin durumunu (açık/kapalı) doğru şekilde sınıflandırır.

Eye-State-Prediction is an application that can predict the eye state in real-time. The application predicts whether the eyes are open or closed based on facial images taken from a camera. The model classifies the eye state (open/closed) correctly using the face data obtained from the user.

## Özellikler / Features:
- Gerçek zamanlı göz durumu tahmini / Real-time eye state prediction
- Gözlerin açık/kapalı olduğunu sınıflandıran bir model / A model that classifies whether the eyes are open or closed
- Veri toplama ve model eğitimi / Data collection and model training

## Kod Yapısı / Code Structure

Bu proje üç ana bileşenden oluşur / This project consists of three main components:

### 1. **Göz Takibi ve Veri Toplama: `eye_tracking_data_collection.py`**

Bu dosya, yüz tespiti ve gözlerin durumunu (açık/kapalı) takip etmek için kullanılan ana kodu içerir. Gerçek zamanlı bir kamera akışından alınan görüntüler üzerinde, **dlib** kütüphanesi ile yüz noktaları tespit edilir ve gözlerin açılıp kapanma durumları hesaplanır. Kullanıcıdan bu veriler alınarak, CSV dosyasına kaydedilir. Bu veriler daha sonra modelin eğitilmesi için kullanılabilir.

This file contains the main code used for face detection and tracking the state of the eyes (open/closed). Using the **dlib** library, facial landmarks are detected from images taken from a real-time camera stream, and the state of the eyes is calculated. These data are collected from the user and saved to a CSV file, which can later be used to train the model.

**Temel İşlevler / Key Functions:**
- Yüz tespiti yapmak için **dlib** kullanılır / **dlib** is used for face detection.
- Gözlerin üst ve alt noktalarından mesafe hesaplanarak gözlerin açık mı kapalı mı olduğu tahmin edilir / The distance between the upper and lower points of the eyes is calculated to predict whether the eyes are open or closed.
- Gerçek zamanlı video akışı üzerinden kullanıcıdan göz verileri toplanır / Eye data is collected from the user via a real-time video stream.
- Veriler `dataset.csv` dosyasına kaydedilir / Data is saved to the `dataset.csv` file.

**Kullanıcı Komutları / User Commands:**
- `'q'`: Uygulamayı sonlandırır / Exits the application.
- `'v'`: Göz verilerini kaydeder / Saves the eye data (collects eye data from the user).

### 2. **Model Eğitimi ve Gerçek Zamanlı Tahmin: `real_time_prediction_model.py`**

Bu dosya, göz durumu tahmininin yapılacağı modelin eğitimini içerir. Modelin eğitimi için `LogisticRegression` sınıflandırıcısı kullanılır. **MultiOutputClassifier** ile gözlerin sol ve sağ durumları tahmin edilir. Kamera akışındaki her bir yüz için, modelin tahmin ettiği göz durumu ekranda görüntülenir.

This file contains the training of the model that will predict the eye state. The model is trained using a `LogisticRegression` classifier, and the left and right eye states are predicted using **MultiOutputClassifier**. For each face in the camera stream, the predicted eye state is displayed on the screen.

**Temel İşlevler / Key Functions:**
- Model, `dataset.csv` dosyasındaki veriler ile eğitilir / The model is trained with the data from the `dataset.csv` file.
- Gözlerin sol ve sağ durumları tahmin edilir ve bu tahminler gerçek zamanlı olarak ekranda gösterilir / The left and right eye states are predicted and shown in real-time on the screen.
- Kullanıcı `'t'` tuşuna basarak gerçek zamanlı tahmin yapabilir / The user can press `'t'` to make real-time predictions.

### 3. **Model Doğruluğu ve Test Seti Tahminleri: `model_accuracy_and_predictions.py`**

Bu dosya, modelin doğruluğunu test etmek için kullanılır. `dataset.csv` dosyasındaki verilerle eğitilen modelin başarımı hesaplanır ve test seti üzerindeki tahminler doğruluk oranı ile birlikte görüntülenir. Sol ve sağ gözlerin tahmin sonuçları ayrı ayrı değerlendirilir.

This file is used to test the accuracy of the model. The performance of the trained model is calculated with the data from the `dataset.csv` file, and predictions on the test set are displayed along with the accuracy rate. The prediction results for the left and right eyes are evaluated separately.

**Temel İşlevler / Key Functions:**
- Model eğitildikten sonra, test seti üzerinde doğruluk hesaplanır / After the model is trained, accuracy is calculated on the test set.
- Doğruluk oranları (sol ve sağ gözler için) hesaplanır ve ekrana yazdırılır / Accuracy rates (for left and right eyes) are calculated and displayed on the screen.
- Test seti üzerinde modelin tahmin ettiği değerler ve gerçek değerler karşılaştırılır / The predicted values and real values on the test set are compared.

## Gereksinimler / Requirements:
- Python 3.x
- OpenCV
- dlib
- scikit-learn
