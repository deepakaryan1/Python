from __future__ import print_function
import paho.mqtt.subscribe as subscribe
import string
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
        try:
            ms=subscribe.simple(topic0, hostname=mqttHost, transport=tTransport, port=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})
            msg=subscribe.simple(topic, hostname=mqttHost, transport=tTransport, port=tPort,auth={'username':mqttUsername,'password':mqttAPIKey})
            print("Tempe = "+str(ms.payload)+"Humidity = "+ str(msg.payload))
            self.text.insert("end","Tempe = "+str(ms.payload)+"Humidity = "+ str(msg.payload)+"\n")
            self.text.see("end")
            self.after(1000, self.add_value)
        except:
            print ("There was an error while subscrbing the data.")
           

if __name__ == "__main__":
    root =tk.Tk()
    # The ThingSpeak Channel ID.
    # Replace <YOUR-CHANNEL-ID> with your channel ID.
    channelID = "1423845"

    # The write API key for the channel.
    # Replace <YOUR-CHANNEL-WRITEAPIKEY> with your write API key.
    writeAPIKey = "O3MK0JWZ9R1OJYO2"

    # The hostname of the ThingSpeak MQTT broker.
    mqttHost = "mqtt.thingspeak.com"

    # You can use any username.
    mqttUsername = "mwa0000022884785"

    # Your MQTT API key from Account > My Profile.
    mqttAPIKey = "ZRHDWRDMOXC5P5QC"

    readAPIKey ="Y99TY2SPBKIL08W0"

    tTransport = "websockets"
    tPort = 80

    # Create the topic string.
    topic0 = "channels/"+channelID+"/subscribe/fields/field1/"+readAPIKey
    topic = "channels/" + channelID+"/subscribe/fields/field2/" + readAPIKey
    frame = Example(root)
    frame.pack(fill="both", expand=True)
    root.mainloop()