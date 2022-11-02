# Boulder Esp8266

Projeto responsável por controlar a sequencia de luzes que ficaram ligadas.

![main](./docs/img/main.jpg)

## Diagrama arquitetura solução

![main](./docs/Diagrama%20arquitetura-Arquitetura%20Solucao.drawio.png)

## Diagrama arquitetura sistema

![main](./docs/Diagrama%20arquitetura-Arquitetura%20Sistema.drawio.png)

## Principais tecnologias

* AWS IOT (MQTT Service Broker)
* AWS IAM POLICY
* Autenticação por Certificado (der, pem, key)
* Mongo DB
* NODE MCU 8266
* Micropython
* Esptool
* make (command)


## Como configurar

* [pythom3](https://linuxize.com/post/how-to-install-python-3-9-on-ubuntu-20-04/)
* [pip](https://linuxize.com/post/how-to-install-pip-on-ubuntu-20.04/)
* [ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy) (pip install adafruit-ampy)
* [esptool](https://micropython.org/download/esp8266/) (python -m pip install esptool)
* [screen](/...) (sudo apt install screen)

##  Instalar firmware micropython esp8266

```cmd
esptool.py --chip esp8266 --port /dev/ttyUSB0 erase_flash

esptool.py --port /dev/ttyUSB0 --chip esp8266 --baud 115200 write_flash --flash_size=detect -fm dout 0 esp8266-20210902-v1.17.bin
```

## Deploy no ESP8266

```cmd
make deploy
```

## Como listar os arquivos

```cmd

ampy -p /dev/ttyUSB0 ls

```

##  Como entrar no dispositivo

```cmd

screen /dev/ttyUSB0 115200

```

## Exemplo de Execução

- Execução do programa em micropython
![Execução do programa em micropython](/docs/img/exemplo-execucao.jpeg?raw=true "Execução do programa em micropython")

- Recebimento de mensagem AWS IOT CORE
![Recebimento de mensagem AWS IOT CORE](/docs/img/exemplo-recebimento-mgs-aws.jpeg?raw=true "Recebimento de mensagem AWS IOT CORE")

- Mensagem no terminal
![Mensagem no terminal](/docs/img/informativo-de-msg.jpeg?raw=true "Mensagem no terminal")

- Listagem de arquivos
![Listagem de arquivos](/docs/img/ls-no-esp.jpeg?raw=true "Listagem de arquivos")

## Como criar certificado .DER

```cmd
openssl x509 -in teste.cert.pem -out teste.cert.der -outform DER
openssl x509 -in root-CA.crt -out root-CA.der -outform DER
openssl rsa -in teste.private.key -out teste.private.der -outform DER
```

## Liberar acesso a porta serial

```cmd
sudo chmod a+rw /dev/ttyUSB0 
```

## My Profile Resume

| [<img src="https://avatars.githubusercontent.com/u/498332?s=400&u=9b7a8aa8743ec4dd3c84d8c382aa31fb1b6c8abf&v=4" width=115><br><sub>Govinda</sub>](https://github.com/govinda777) |
| :---: |


[!["Buy Me A Coffee"](https://user-images.githubusercontent.com/1376749/120938564-50c59780-c6e1-11eb-814f-22a0399623c5.png)](https://www.buymeacoffee.com/govinda777)


## Links

* http://www.poncolhijau.web.id/2020/05/kontrol-led-rgb-ws2812b-dengan-android.html
* https://notebook.community/Wei1234c/Elastic_Network_of_Things_with_MQTT_and_MicroPython/notebooks/test/MQTT%20client%20test%20-%20MicroPython
* https://techtotinker.blogspot.com/2020/12/022-esp32-micropython-mqtt-part-2.html
* https://create.arduino.cc/projecthub/B45i/getting-started-with-arduino-cli-7652a5
* https://github.com/ExploreEmbedded/Hornbill-Examples/tree/master/arduino-esp32/AWS_IOT
* https://platformio.org/lib/show/1743/AWS-SDK-ESP
* https://pythonforundergradengineers.com/micropython-install.html
* https://micropython.org/unicorn/
* https://docs.micropython.org/en/latest/reference/packages.html
* https://thingspeak.com/
* https://pubsubclient.knolleary.net/api
* https://nerdyelectronics.com/how-to-connect-nodemcu-to-aws-iot-core/
* [Tutorial configuração Thing](https://www.youtube.com/watch?v=28FS2qix2u4&ab_channel=ElectronicsInnovation)
* [Arduino ESP8266 filesystem uploader](https://github.com/esp8266/arduino-esp8266fs-plugin)
