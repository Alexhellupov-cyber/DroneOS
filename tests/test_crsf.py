from src.drivers.crsf.encoder import CRSFPacker

channels = [
    CRSFPacker.rc_to_crsf(1500),  # Roll
    CRSFPacker.rc_to_crsf(1500),  # Pitch
    CRSFPacker.rc_to_crsf(1500),  # Yaw
    CRSFPacker.rc_to_crsf(1500),  # Throttle
]

# дополняем до 16 каналов
while len(channels) < 16:
    channels.append(CRSFPacker.rc_to_crsf(1000))

frame = CRSFPacker.encode(channels)

print("LEN:", len(frame))
print(frame.hex())