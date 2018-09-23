import paho.mqtt.client as mqtt
from Tkinter import *
import ConfigParser, os
#########################################
config = ConfigParser.ConfigParser()
config.read("config.ini")
subs = config.get("settings", "subscribe")
usr = config.get("settings", "user")
passw = config.get("settings", "pass")
srv = config.get("settings", "server")
port = config.get("settings", "port")
##########################################

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(subs)


# # The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
#     print(msg.topic+" "+str(msg.payload))
    

# def Open1(self):
#     if not self.child_window:
#         self.child_window = Second(self.master)

def alert():
    root = Tk()
    root.title("INFO")
    root.geometry("600x200")
    root.after(5000, lambda: root.destroy())

    one=Label(root, text='Wykryto ruch!', bg="red", fg="white", font="none 32 bold")
    one.config(wraplength=600, bg="red")
    one.pack()

    two=Button(root, text="EXIT")
    two.pack() 
    
    root.mainloop()
    

def on_message(client, userdata, msg):
    if msg.payload == "1":
        alert()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(usr, password=passw)
client.clean_session = True

client.connect(srv, int(port), 60)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
