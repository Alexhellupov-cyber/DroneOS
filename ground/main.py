from common.network import DroneClient
from common.protocol import encode, decode
from common.messages import MessageType


client = DroneClient("192.168.0.102")

client.connect()

client.send(
    encode(
        MessageType.PING.value
    )
)

response = client.receive()

print(decode(response))

client.close()
