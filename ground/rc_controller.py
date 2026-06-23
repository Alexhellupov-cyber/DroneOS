while True:

    packet = rc_service.update()

    network.send_rc(packet)

    time.sleep(0.01)