import paho.mqtt.client as paho


def on_connect(client, userdata, flags, rc):
    print('CONNACK received with code %d.' % (rc))


client = paho.Client()
print(f"Created the Client Object")
client.on_connect = on_connect

client.connect('broker.mqttdashboard.com', 1883)
