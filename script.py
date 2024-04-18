import webview
import tkinter as tk
from tkinter import messagebox

webview.create_window("offline.chatgpt", "https://chat.openai.com/")
webview.start()

startUp = print("started")
if startUp:
    print("started")
else:
    print("error")

