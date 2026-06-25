import socket
import struct
import cv2

HOST = "0.0.0.0"
PORT = 5600


def main():

    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen(1)

    print(f"Video server listening on {HOST}:{PORT}")

    conn, addr = server.accept()

    print("Video client connected:", addr)

    while True:

        ok, frame = cap.read()

        if not ok:
            continue

        success, jpeg = cv2.imencode(
            ".jpg",
            frame,
            [cv2.IMWRITE_JPEG_QUALITY, 80]
        )

        if not success:
            continue

        data = jpeg.tobytes()

        conn.sendall(struct.pack(">I", len(data)))
        conn.sendall(data)


if __name__ == "__main__":
    main()