import webview
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

html_path = resource_path("index.html")

webview.create_window(
    "Pulse Sickbay",
    html_path,
    width=1000,
    height=650
)

webview.start()
