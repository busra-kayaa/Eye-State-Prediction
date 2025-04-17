import cv2
import dlib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.multioutput import MultiOutputClassifier

data = pd.read_csv("dataset.csv")
x = data.iloc[:, :3].values
y = data.iloc[:, 3:].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
model = MultiOutputClassifier(LogisticRegression())
model.fit(x_train, y_train)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

def mid(p1, p2):
    return (int((p1[0] + p2[0]) / 2), int((p1[1] + p2[1]) / 2))

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(frame)
    for face in faces:
        points = predictor(gri, face)
        points_list = [(p.x, p.y) for p in points.parts()]

        # Göz noktaları
        p1, p2 = points_list[37], points_list[38]
        p3, p4 = points_list[40], points_list[41]
        p5, p6 = points_list[43], points_list[44]
        p7, p8 = points_list[46], points_list[47]

        po_ust_sol = mid(p1, p2)
        po_alt_sol = mid(p3, p4)
        sol_mesafe = po_alt_sol[1] - po_ust_sol[1]

        po_ust_sag = mid(p5, p6)
        po_alt_sag = mid(p7, p8)
        sag_mesafe = po_alt_sag[1] - po_ust_sag[1]

        mburun = points_list[30][1] - points_list[27][1]

        cv2.putText(frame, f'Sol Mesafe: {sol_mesafe}', (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(frame, f'Sag Mesafe: {sag_mesafe}', (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(frame, f'Burun Mesafe: {mburun}', (20, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('t'):
            p = [sol_mesafe, sag_mesafe, mburun]
            y_pred = model.predict([p])
            print("Tahmin Edilen Değerler: ", y_pred)

        if key == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()

    cv2.imshow("Goz Takibi", frame)
