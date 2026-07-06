from flask import Flask, Response

from backend.video import VideoCamera

app = Flask(__name__)

camera = VideoCamera()


def generate():

    while True:

        frame = camera.get_frame()

        if frame is None:
            continue

        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + frame
            + b"\r\n"
        )


@app.route("/video")
def video():

    return Response(
        generate(),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        threaded=True,
    )

@app.route("/")
def index():
    return """
    <h1>DroneOS Backend</h1>
    <a href="/video">Open Video Stream</a>
    """