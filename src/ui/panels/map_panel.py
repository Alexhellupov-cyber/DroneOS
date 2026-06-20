from pathlib import Path
from PySide6.QtWebEngineCore import QWebEngineSettings
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import (
    QGroupBox,
    QVBoxLayout,
)

from PySide6.QtWebEngineWidgets import (
    QWebEngineView,
)


class MapPanel(QGroupBox):

    def __init__(self):

        super().__init__("🗺 Карта")

        layout = QVBoxLayout()

        self.browser = QWebEngineView()

        settings = self.browser.settings()

        settings.setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls,
            True
        )

        settings.setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls,
            True
        )


        html = (
            Path(__file__).parent.parent
            / "web"
            / "index.html"
        )

        self.browser.load(
            QUrl.fromLocalFile(
                str(html.resolve())
            )
        )

        self.browser.loadFinished.connect(
            lambda ok: print("Map loaded:", ok)
        )

        layout.addWidget(self.browser)

        self.setLayout(layout)

    def update_position(self, latitude, longitude):

        self.browser.page().runJavaScript(
            f"updateDrone({latitude}, {longitude});"
        )
    def center_on_drone(self):

        self.browser.page().runJavaScript(
            "followDroneEnable();"
        )