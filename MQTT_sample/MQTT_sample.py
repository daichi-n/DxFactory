import time
import json
import random
import paho.mqtt.client as mqtt

# Azure IoT Hubに接続するための設定
iot_hub_name = "<your IoT Hub name>"  # ここに実際のIoT Hubの名前を入力します
device_id = "<your device id>"        # ここに実際のデバイスIDを入力します
username = f"{iot_hub_name}.azure-devices.net/{device_id}/api-version=2018-06-30"
password = "<your IoT Hub device key>"  # ここに実際のデバイスキーを入力します

mqtt_url = f"{iot_hub_name}.azure-devices.net"
mqtt_port = 8883
topic = f"devices/{device_id}/messages/events/"

# MQTTクライアントの作成と接続
client = mqtt.Client(client_id=device_id, protocol=mqtt.MQTTv311)
client.username_pw_set(username=username, password=password)
client.tls_set_context(context=None)  # TLS設定（SSL/TLSを使用する場合）

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to IoT Hub")
    else:
        print(f"Connection failed with code {rc}")

client.on_connect = on_connect

client.connect(mqtt_url, port=mqtt_port)

# データを生成して送信するループ
while True:
    temperature = random.uniform(10.0, 40.0)  # 仮想的な温度データを生成
    data = {
        "deviceId": device_id,
        "temperature": temperature,
        "timestamp": time.strftime('%Y-%m-%dT%H:%M:%S%Z')
    }
    payload = json.dumps(data)
    
    # MQTTでメッセージをIoT Hubに送信
    client.publish(topic, payload=payload, qos=1)
    print(f"Message sent: {payload}")
    
    time.sleep(30)  # 5秒ごとにデータを送信する例です。実際のアプリケーションでは調整が必要です。
