import cv2

for i in range(10):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print(f"{i}: not opened")
        continue

    ret, frame = cap.read()
    print(f"{i}: opened={ret}")

    cap.release()