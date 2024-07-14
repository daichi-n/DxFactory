# MQTT sample memo

## paho-mqttライブラリのインポート

このライブラリは、PythonでMQTTを使うための一般的なライブラリで、
Azure IoT Hubとの通信に使用します。

## IoT Hubの接続設定

iot_hub_nameには、Azure Portalで設定したIoT Hubの名前を、
device_idにはデバイスのIDを、passwordにはデバイスキーを指定します。

## MQTTクライアントの作成と接続

MQTTクライアントを作成し、username_pw_setとtls_set_contextを使用して、
Azure IoT Hubに接続するための設定を行います。
TLS設定は、SSL/TLSを使用して安全に通信するためのものです。

## データの生成と送信

random.uniform()を使って仮想的な温度データを生成し、JSON形式に変換してpayloadとして送信します。
publish()メソッドを使って、指定したトピックにデータを送信します。

## ループの制御

while Trueループを使用して、
定期的にデータを生成して送信する処理を実行します。
実際のアプリケーションでは、適切なデータ生成方法や送信間隔を設定してください。