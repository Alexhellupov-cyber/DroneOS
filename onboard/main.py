from common.network import DroneServer
from common.protocol import decode, encode
from common.logger import log

server = DroneServer()

while True:

    conn, addr = server.accept()

    log(f"Client connected: {addr}")

    data = conn.recv(4096)

    if not data:
        conn.close()
        continue

    packet = decode(data)

    log(packet)

    if packet["type"] == "ping":

        conn.send(
            encode(
                {
                    "type": "pong"
                }
            )
        )

    conn.close()
