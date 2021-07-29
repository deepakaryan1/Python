from __future__ import print_function
import paho.mqtt.publish as publish
import string
import Adafruit_DHT
import MySQLdb

import time

import tkinter as tk

class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.text = tk.Text(self, height=16, width=40)
        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.vsb.pack(side="right", fill="y")
        self.text.pack(side="left", fill="both", expand=True)

        self.add_value()

    def add_value(self):
             if humidity is not None and temperature is not None:
                 print('Temp = {0:0.1f}*C Humidity = {1:0.1f}%'. format(temperature, humidity))
                 sql="INSERT INTO temp_humidity ( tempereture, humidity) VALUES ( %s, %s)"
                 val = (temperature, humidity)
                 mycursor . execute(sql, val)
                 mydb . commit()
                 print(mycursor . rowcount, "record inserted.")
                 self.text.insert("end", "Temp = "+str(temperature) + "  Humidity = "+str(humidity)+"\n")
                 self.text.see("end")
                 self.after(1000, self.add_value)
             else:
                 print("data no fetcheng")

if __name__ == "__main__":
    root =tk.Tk() 
    mydb = MySQLdb.connect(host="localhost", user="root", password="",database="deepak")
    mycursor=mydb.cursor()
    gpio = 4
    sensor=Adafruit_DHT.DHT11
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
    frame = Example(root)
    frame.pack(fill="both", expand=True)
    root.mainloop()
