import cv2

backends = [
    cv2.CAP_ANY,
    cv2.CAP_DSHOW,
    cv2.CAP_MSMF,
]

backend_names = {
    cv2.CAP_ANY: "ANY",
    cv2.CAP_DSHOW: "DSHOW",
    cv2.CAP_MSMF: "MSMF",
}

for backend in backends:
    print(f"\n===== {backend_names[backend]} =====")

    for i in range(10):
        cap = cv2.VideoCapture(i, backend)

        if cap.isOpened():
            ret, frame = cap.read()
            print(f"{i}: opened={ret} size={frame.shape if ret else None}")

        cap.release()