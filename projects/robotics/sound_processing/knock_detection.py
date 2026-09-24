"""Real-time knock detection for the sound-processing robot experiment.
Captures microphone audio, streams samples to MATLAB for classification
(classify_tile.m), and toggles the Arduino spray/hammer rig over serial.
"""
# Real-time detection of microphone signaling
import pyaudio
import numpy as np
import time
from datetime import datetime
import sys
import wave
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pymatbridge import Matlab
from time import sleep
import serial
from tkinter import *
from threading import Lock
for name in sys.path:
    print(name)
# --- Serial communication notes ---
# 1. Send and read conflict
# 2. Baud rate 9600 => ~960 bytes per second
# signal1 = True
# signal2 = True
# def LedOn():
#
#     while True:
#         ser.write('S'.encode('utf-8'))
#         print(ser.readline().decode('utf-8'))
#         if ser.readline().decode('utf-8').strip(" ") == "Spray!":
#             pass
#         break
#
#
#
#
# def LedOff():
#
#     for i in range(0):
#
#         while True:
#             ser.write('U'.encode('utf-8'))
#             print(ser.readline().decode('utf-8'))
#             if ser.readline().decode('utf-8') == "Unspray":
#                 pass
#             break
#
# while True:
#     root = tk.Tk()
#
#     frame = tk.Frame(root)
#
#     frame.pack(side = tk.BOTTOM) #put the btn into the bottom of frame
#
#     btn1 = tk.Button(frame,text="LedOn",fg="red",command=LedOn)
#     btn1.config(height=10, width=10) #adjust the dimension of btn
#     btn1.pack(side=tk.LEFT)
#
#     btn2 = tk.Button(frame,text = "LedOff",command =LedOff)
#     btn2.config(height=10, width=10)
#     btn2.pack(side = tk.RIGHT)
#     root.mainloop() #To make the btn box static
#Matlab source: https://ww2.mathworks.cn/help/matlab/matlab_external/matlab-arrays-as-python-variables.html
import sounddevice as sd
def main():
    def set_value():
        # Read the chosen values, close the panel and start the capture loop.
        plotgraph = states()  # whether "Plotting Graph" is checked
        try:
            CHUNK = int(CHUNK_var.get())
            RATE = int(RATE_var.get())
            mic = int(mic_var.get())
            display_var.set("Chunk:{0}\n Rate:{1}\n Microphone:{2}".format(CHUNK, RATE, mic))
            my_window.destroy()
            Run(CHUNK, RATE, mic, plotgraph)
        except:
            display_var.set("ERROR")
            return
    def soundinfo():
        # Show every audio device detected by sounddevice.
        tk = Tk()
        micinfo = str(sd.query_devices())
        tk.title("DevicesInfo")
        soundlabel = Label(tk, text=micinfo)
        soundlabel.grid(row=0, column=0)
        print(sd.query_devices())
        tk.mainloop()
    # --- Initiation panel: pick chunk size, sample rate and microphone ---
    my_window = Tk()
    window_title = my_window.title("Initiation Panel")
    display_var = StringVar(value='Please select the microphone \n and sampling rate for audio.')
    CHUNK_var = StringVar(my_window, value='44100')
    RATE_var = StringVar(my_window, value='44100')
    mic_var = StringVar(my_window, value='2')
    # img = PhotoImage(file="../venv/GiddyFarawayGalapagossealion-max-1mb.gif")
    img = PhotoImage(file="GiddyFarawayGalapagossealion-max-1mb.gif")
    label_1 = Label(my_window, text="CHUNK:")  # a Label takes text or textvariable
    entry_1 = Entry(my_window, textvariable=CHUNK_var)
    label_4 = Label(my_window, text='RATE:')
    entry_3 = Entry(my_window, textvariable=RATE_var)
    label_3 = Label(my_window, text='Microphone:')
    entry_2 = Entry(my_window, textvariable=mic_var)
    button_1 = Button(my_window, text="Enter values:", command=set_value)
    button_1.config(image=img)
    label_2 = Label(my_window, textvariable=display_var)
    label_1.grid(row=0, column=0)
    entry_1.grid(row=0, column=1)
    label_4.grid(row=1, column=0)
    entry_3.grid(row=1, column=1)
    label_3.grid(row=2, column=0)
    entry_2.grid(row=2, column=1)
    button_1.grid(row=5, column=0)
    label_2.grid(row=5, column=1)
    # Add-on button that lists the available sound devices
    button_2 = Button(my_window, text="Show Available Devices", command=soundinfo)
    button_2.grid(row=3)
    # Add-on checkbox that turns the audio waveform plot on/off
    plot = IntVar()
    def states():
        # Read the checkbox value into a plain boolean.
        if plot.get() == 1:
            graph = True
        else:
            graph = False
        return graph  # the returned name differs from the stored var
    checkbox1 = Checkbutton(my_window, text="Plotting Graph", variable=plot)
    checkbox1.grid(row=4, column=1)
    my_window.mainloop()
def Run(C, R, mic, Plot):
    """Run the live capture/classify loop with the chosen settings."""
    CHUNK = 44100  # number of data points to read at a time (4096)
    CHUNK = C
    # 4096 bytes => frames captured per buffer
    RATE = 44100  # sampling rate in samples/second (Hz)
    RATE = R
    # sampling rate => frames per second read from the device
    serSignal = 'S'
    KnockSignal = 'K'
    Input_Device_Index = 2
    Input_Device_Index = mic
    plot = Plot
    # --- Serial port setup ---
    ser_port = "COM8"  # Windows COM port to the Arduino
    baud_rate = 9600
    count = 0
    flag = False
    signal = False
    # --- Start the MATLAB engine and PyAudio ---
    mlab = Matlab(executable=r"D:\MATLAB\bin\matlab.exe")
    mlab.start()
    p = pyaudio.PyAudio()
    # Open the microphone input stream and the serial link to the Arduino.
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, input_device_index=None
                    , frames_per_buffer=CHUNK)
    ser = serial.Serial(ser_port, baud_rate)
    print(ser.readline().decode("utf-8"))
    print("Input delay is %f" % stream.get_input_latency())
    # --- Live capture loop ---
    while True:
        for i in range(int(3)):  # repeat the capture 3 times per round
            if count == 1:
                # Ask the Arduino to knock, then record the sound that follows.
                ser.write(KnockSignal.encode("utf-8"))  # encode() turns str into bytes
                sleep(.32)  # ** change here (0.1s per 5000 samples)
                flag = True
                print("Must Knock Here")
            # Input device id "2" => built-in microphone
            # info = p.get_host_api_info_by_index(0)
            # numdevices = info.get('deviceCount')
            # for i in range(0, numdevices):
            #     if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            #         pass
            if flag == True:
                np.set_printoptions(threshold=sys.maxsize)
                # Read one chunk of raw 16-bit samples as a numpy array.
                data = np.fromstring(stream.read(CHUNK), dtype=np.short)
                time = np.arange(0, CHUNK)
                # (Commented-out: volume-bar visualisation and bridge_passthrough.m passthrough)
                # peak = np.average(np.abs(data)) * 21
                # bars = "#" * int(50 * peak / 2 ** 16)
                if count == 1:
                    print("Write")
                    with open("SignalTest.txt", "wt") as out_file:
                        out_file.writelines(str(data))  # it can only write strings
                if plot == True and count == 2:
                    # Time the read latency before plotting the waveform.
                    past = stream.get_time()
                    np.set_printoptions(threshold=sys.maxsize)
                    data = np.fromstring(stream.read(CHUNK), dtype=np.short)
                    present = stream.get_time()
                    delay = present - past
                    print("The delay is %f" % delay)
                    plt.title('AudioSample')
                    plt.plot(time, data)
                    plt.ylim(-40000, 40000)
                    plt.ylabel('Amplitude')
                    plt.xlabel('Sample Size')
                    # Classify the window in MATLAB (1 = hollow, 2 = solid).
                    dataprocess = mlab.run_func('classify_tile.m', {"arg1": data})
                    print(np.amax(data))
                    print(dataprocess['result'])
                    d1 = dataprocess['result']
                    if d1 == 1:
                        # Hollow knock detected => trigger the sprayer on the Arduino.
                        ser.write(serSignal.encode("utf-8"))  # encode() turns str into bytes
                    plt.show()
                    flag = False
                    count = 0
            count += 1
        # ser.reset_output_buffer()
    # --- Shut down the MATLAB engine, stream and serial link ---
    mlab.stop()
    out_file.close()
    stream.stop_stream()
    stream.close()
    p.terminate()
    sys.exit(0)
# Entry point of the script.
main()
