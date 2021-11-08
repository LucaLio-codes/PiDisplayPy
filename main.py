#!/bin/python3
import time
import tkinter as tk
import os
import pathlib
import sys
from myUi import MyUiWidget
from WeatherFetcher import getdir
import requests


PROJECT_PATH = pathlib.Path(__file__).parent
WEATHERINTERVAL = 5 * 60 * 1000
old_vals = []

def scan(scan_type):
    file = time.strftime(f'/share/scans/%d-%m-%Y_%H-%M-%S.{scan_type}')
    cmd = f'scanimage -d "pixma:04A91748_106562" --format png > {file}'
    os.system(cmd)
    # TODO Preview


def update_time(time_lbl, date_lbl):
    time_string = time.strftime('%H:%M:%S')
    time_lbl.config(text=time_string)
    date_string = time.strftime(('%A, %d.%m.%Y'))
    date_lbl.config(text=date_string)
    time_lbl.after(1000, lambda: update_time(time_lbl, date_lbl))

def update_weather(img, deg, feel, max_t, min_t, set_s, rise_s, descr):
    global old_vals
    try:
        img_d, deg_d, feel_d, max_d, min_d, set_d, rise_d, descr_d = getdir()
    except requests.exceptions.Timeout:
        img_d, deg_d, feel_d, max_d, min_d, set_d, rise_d, descr_d = old_vals
    old_vals = img_d, deg_d, feel_d, max_d, min_d, set_d, rise_d, descr_d
    #img.configure(image=img_d)
    degstr = str(deg_d) + " °C"
    image = tk.PhotoImage(file=img_d)
    img.config(image=image)
    img.img = image
    deg.configure(text=degstr)
    feel.configure(text=f'Feels like: {feel_d} °C')
    max_t.configure(text=f'{max_d} °C')
    min_t.configure(text=f'{min_d} °C')
    set_s.configure(text=set_d)
    rise_s.configure(text=rise_d)
    descr.configure(text=descr_d)
    img.after(WEATHERINTERVAL, lambda: update_weather(img, deg, feel, max_t, min_t, set_s, rise_s, descr))








def main():
    window = tk.Tk()
    window.attributes('-fullscreen', True)
    widget = MyUiWidget(window)

    # Setup Widget
    widget.scanPng.configure(command=lambda: scan("png"))
    widget.scanPDF.configure(command=lambda: scan("pdf"))
    widget.exitButton.configure(command=lambda: sys.exit())

    # start clock
    update_time(widget.timeLabel, widget.dateLabel)
    update_weather(widget.weatherimg,
                   widget.currentDegreeLabel,
                   widget.currentFeelLabel,
                   widget.maxLabelVal,
                   widget.minLabelVal,
                   widget.sunsetLabelVal,
                   widget.sunriseLabelVal,
                   widget.weatherdescr
                   )

    widget.pack(expand=True, fill='both')
    window.mainloop()


if __name__ == '__main__':
    main()