# Boulder Esp8266

Projeto responsável por controlar a sequencia de luzes que ficaram ligadas.

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
