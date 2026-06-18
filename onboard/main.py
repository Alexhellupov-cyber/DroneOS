from common.network import DroneServer
from common.protocol import decode, encode
from common.messages import MessageType

server = DroneServer()

while True:

    conn, addr = server.wait_connection()

    while True:

        try:

            data = conn.recv(4096)

            if not data:
                break

            packet = decode(data)

            print(packet)

            if packet["type"] == MessageType.PING.value:

                conn.sendall(
                    encode(
                        MessageType.PONG.value,
                        {
                            "status": "ok"
                        }
                    )
                )

        except Exception as e:

            print(e)

            break

    conn.close()

    print("[NETWORK] Client disconnected")
