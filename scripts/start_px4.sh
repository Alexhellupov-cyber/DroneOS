def start_px4(self):

    self.stop_px4()

    time.sleep(2)

    self.log.emit("Starting PX4 SITL...")

    cmd = f"""
    unset VIRTUAL_ENV
    cd "{self.project_dir}"
    exec make px4_sitl gz_x500
    """

    self.process = subprocess.Popen(
        ["bash", "-lc", cmd],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )

    threading.Thread(
        target=self._reader,
        daemon=True
    ).start()

    self.started.emit()