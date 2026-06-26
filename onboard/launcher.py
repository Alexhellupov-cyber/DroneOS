import threading

from backend.app import app
from onboard.server import OnboardServer


def run_flask():
    app.run(
        host="0.0.0.0",
        port=5000,
        threaded=True,
        use_reloader=False
    )


def run_server():
    server = OnboardServer()
    server.start()


if __name__ == "__main__":
    threading.Thread(
        target=run_flask,
        daemon=True
    ).start()

    run_server()