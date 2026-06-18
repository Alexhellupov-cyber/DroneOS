import socket

from common.protocol import encode, decode

HOST = "0.0.0.0"
PORT = 5000


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"DroneOS listening on {HOST}:{PORT}")

while True:

    conn, addr = server.accept()

    print(f"Client: {addr}")

    packet = conn.recv(4096)

    if not packet:
        conn.close()
        continue

    message = decode(packet)

    print(message)

    if message["type"] == "ping":

        conn.send(
            encode(
                {
                    "type": "pong"
                }
            )
        )

    conn.close()
