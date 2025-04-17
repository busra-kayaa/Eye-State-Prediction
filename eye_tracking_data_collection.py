# Göz takibi

import cv2
import dlib

detector = dlib.get_frontal_face_detector()
model = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)
def mid(p1, p2):
    return (int((p1[0]+p2[0])/2), int((p1[1]+p2[1])/2))

f = open("dataset.csv","a")

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(frame)
    for face in faces:
        points = model(gri, face)
        points_list = [(p.x, p.y) for p in points.parts()]
        # print(points_list)

        p1, p2 = points_list[37], points_list[38]
        p3, p4 = points_list[40], points_list[41]

        p5, p6 = points_list[43], points_list[44]
        p7, p8 = points_list[46], points_list[47]

        # cv2.circle(frame, (p1[0], p1[1]), 3, (0, 0, 255), -1)
        # cv2.circle(frame, (p2[0], p2[1]), 3, (0, 0, 255), -1)
        # cv2.circle(frame, (p3[0], p3[1]), 3, (0, 0, 255), -1)
        # cv2.circle(frame, (p4[0], p4[1]), 3, (0, 0, 255), -1)
        # cv2.circle(frame, (p5[0], p5[1]), 3, (0, 0, 255), -1)
        # cv2.circle(frame, (p6[0], p6[1]), 3, (0, 0, 255), -1)
        # cv2.circle(frame, (p7[0], p7[1]), 3, (0, 0, 255), -1)
        # cv2.circle(frame, (p8[0], p8[1]), 3, (0, 0, 255), -1)

        # sol
        po_ust_sol = mid(p1, p2)
        po_alt_sol = mid(p3, p4)
        cv2.circle(frame, (po_ust_sol[0], po_ust_sol[1]), 3, (0, 255, 0), -1)
        cv2.circle(frame, (po_alt_sol[0], po_alt_sol[1]), 3, (0, 255, 0), -1)

        sol_mesafe = po_alt_sol[1] - po_ust_sol[1]

        # sağ
        po_ust_sag = mid(p5, p6)
        po_alt_sag = mid(p7, p8)
        cv2.circle(frame, (po_ust_sag[0], po_ust_sag[1]), 3, (0, 255, 0), -1)
        cv2.circle(frame, (po_alt_sag[0], po_alt_sag[1]), 3, (0, 255, 0), -1)

        sag_mesafe = po_alt_sag[1] - po_ust_sag[1]

        # burun
        mburun = points_list[30][1]-points_list[27][1]
        print(mburun)

    cv2.imshow("sd", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        r = input("islem girin:  ")
        if r == "q":
            break
        elif r == "v":
            sol = input("sol göz icin veri gir")
            sag = input("sag göz icin veri gir")

            f.write(f"{sol_mesafe}, {sag_mesafe}, {mburun}, {sol}, {sag} \n")
            f.flush()

cap.release()
cv2.destroyAllWindows()