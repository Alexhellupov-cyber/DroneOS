from src.drivers.crsf.encoder import CRSFPacker

channels = [

    CRSFPacker.rc_to_crsf(1500),

    CRSFPacker.rc_to_crsf(1500),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

    CRSFPacker.rc_to_crsf(1000),

]

frame = CRSFPacker.encode(
    channels
)

print(frame.hex())
print(len(frame))