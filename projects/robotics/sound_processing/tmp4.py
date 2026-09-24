#Real-time detection of microphone signaling
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



#Serial communication problems:
#1.Send and read conflict
#2. Baud rate:9600 => 960 bytes per second


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
        plotgraph = states() #This function returns a value
        try:
            CHUNK = int(CHUNK_var.get())
            RATE = int(RATE_var.get())
            mic = int(mic_var.get())
            display_var.set("Chunk:{0}\n Rate:{1}\n Microphone:{2}".format(CHUNK, RATE, mic))
            my_window.destroy()
            Run(CHUNK,RATE,mic,plotgraph)
        except:
            display_var.set("ERROR")
            return


    def soundinfo():
        tk = Tk()
        micinfo = str(sd.query_devices())
        tk.title("DevicesInfo")
        soundlabel = Label(tk, text=micinfo)
        soundlabel.grid(row=0, column=0)
        print(sd.query_devices())
        tk.mainloop()


    my_window = Tk()
    window_title = my_window.title("Initiation Panel")
    display_var = StringVar(value='Please select the microphone \n and sampling rate for audio.')

    CHUNK_var = StringVar(my_window,value='44100')
    RATE_var = StringVar(my_window,value='44100')
    mic_var = StringVar(my_window,value='2')

    # img = PhotoImage(file="../venv/GiddyFarawayGalapagossealion-max-1mb.gif")
    img = PhotoImage(file="GiddyFarawayGalapagossealion-max-1mb.gif")
    label_1 = Label(my_window, text="CHUNK:")  # Label can use text   or textvariable
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

    #add_on button for showing sound devices
    button_2 = Button(my_window,text="Show Available Devices",command = soundinfo)
    button_2.grid(row=3)
    # add_on for audio graph plot
    plot = IntVar()
    def states():
        if plot.get() == 1:
            graph = True
        else:
            graph = False
        return graph #the returned variable name not same as the allocated var
    checkbox1 = Checkbutton(my_window, text="Plotting Graph", variable=plot)
    checkbox1.grid(row=4, column=1)

    my_window.mainloop()
    # root = tk.Tk()
    # frame = tk.Frame(root)
    # frame.pack(side = tk.BOTTOM) #put the btn into the bottom of frame
    # root.title("Control")
    # btn1 = tk.Button(frame,text="Run",fg="red",command=Run)
    # img1 = tk.PhotoImage(file="./GiddyFarawayGalapagossealion-max-1mb.gif")
    # btn1.config(image=img1) #adjust the dimension of btn
    # btn1.pack(side=tk.LEFT)
    # # def reset():
    # #     labelYourBMI2 = tk.Button(frame, text="")
    # #     return
    # # ButtonReset = tk.Button(frame, text="Reset", command=reset)
    # # ButtonReset.pack()
    # root.mainloop()



def Run(C,R,mic,Plot):
    CHUNK = 44100  # number of data points to read at a time 4096
    CHUNK = C
    # 4096 byte
    # the number of frames
    RATE = 44100  # 176400  # time resolution for reading device (Hz) 44100 samples/second
    RATE = R
    # sampling rate i.e the number of frames per second
    serSignal = 'S'
    KnockSignal = 'K'
    Input_Device_Index = 2
    Input_Device_Index = mic
    plot = Plot

    # Define the serial port
    ser_port = "COM8"  # for window computer, int must be used COM1 = 0,COM2=1 ...
    baud_rate = 9600
    count = 0
    flag =False
    signal =False


    mlab =Matlab(executable=r"D:\MATLAB\bin\matlab.exe")
    mlab.start()
    p = pyaudio.PyAudio()

    # while True:
    #     ser.write(serSignal.encode('utf-8'))
    #     if ser.readline().decode('utf-8') != "Spray":
    #         break

    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE, input=True, input_device_index=None
                    , frames_per_buffer=CHUNK)
    ser = serial.Serial(ser_port, baud_rate)
    print(ser.readline().decode("utf-8"))
    print("Input delay is %f" % stream.get_input_latency())
    while(True):
        for i in range(int(3)): #only loop forA int(??) times
            #if(count>1):
            #    sleep(1)
            if(count==1):
                ser.write(KnockSignal.encode("utf-8"))  # encode is used for string.encode()
                sleep(.32) # **change here (0.1s per 5000samples)
                flag = True
                print("Must Knock Here")
            # The input device id "2"   => built-in microphone
            # info = p.get_host_api_info_by_index(0)
            # numdevices = info.get('deviceCount')
            # for i in range(0, numdevices):
            #     if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            #         pass
                    #print('Input Device id', i, '-', p.get_device_info_by_host_api_device_index(0, i).get('name'))
            # get the default device info
            #print(p.get_default_input_device_info())

            # create a numpy array holding a single read of audio data

            #now = datetime.now()

            if flag == True:
                # if count ==1:
                #     sleep(.5)

                np.set_printoptions(threshold=sys.maxsize)

                data = np.fromstring(stream.read(CHUNK),dtype=np.short)
                #print(stream)
                time = np.arange(0, CHUNK)

                #peak=np.average(np.abs(data))*21
                #bars="#"*int(50*peak/2**16)
                #print("%04d %s"%(i,data))
                #print("%s %s" % (data/32768,now ))

                #print("Input data is ", type(data))

            # Test Matlab data 1
                #res = mlab.run_func('jk.m', {'arg1': data})
                #print("Output data is ", type(res['result']))
                #data1 = res['result']  # The data in matlab is float64 (e.g for 64bit window) https://stackoverflow.com/questions/8855574/convert-ndarray-from-float64-to-integer
                #M_data1 = data1[0] / 32768
                #print("jk.m is",res)


                # data1 = np.array(res['result'], dtype=np.float64).astype(np.int64)
                # print(type(data1))

            #Write data to text file before matlab
                # with open("SignalTest1.txt", "wt") as file:
                #     file.write("%s" % (str(M_data1).lstrip('[').rstrip(']')))
                #     file.flush()
                #     file.close()
                #     # file.writelines("%s %04d %s\n"%(now,i,data))
                #     # close the stream gracefully


                # max_val =np.amax(data)
                # print(max_val)
                # if max_val >30000:

                #data/32768
                #print(M_data1)

                if count == 1:
                    print("Write")
                    with open("SignalTest.txt","wt") as out_file:
                        out_file.writelines(str(data)) #it can only write string

                if plot == True and count==2:

                    past = stream.get_time()
                    np.set_printoptions(threshold=sys.maxsize)
                    data = np.fromstring(stream.read(CHUNK), dtype=np.short)
                    present = stream.get_time()
                    delay = present - past
                    print("The delay is %f" % delay)

                    plt.title('AudioSample')
                    plt.plot(time,data)
                    plt.ylim(-40000,40000)
                    plt.ylabel('Amplitude')
                    plt.xlabel('Sample Size')
                    #plt.pause(.0000000000000000000000000000000000000000000000000000000001)
                    #plt.clf()

                    #print(stream.get_time())

                    dataprocess = mlab.run_func('final_judge.m', {"arg1": data})  # ,{'arg1':data}
                    # print("The input data is ",M_data1)
                    print(np.amax(data))
                    print(dataprocess['result'])
                    d1 = dataprocess['result']

                    if d1 == 1:
                        ser.write(serSignal.encode("utf-8"))  # encode is used for string.encode()
                        # print(ser.write(serSignal.encode("utf-8")))
                        #print(ser.readline().decode("utf-8"))
                        #d1 = 2
                    plt.show()
                    flag=False

                    count=0
            count += 1

        #ser.reset_output_buffer()
    mlab.stop()
    out_file.close()
    stream.stop_stream()
    stream.close()
    p.terminate()

    sys.exit(0)

main()
