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

##  Enviar os arquivos para o esp8266

```cmd
cd src && \
ampy -p /dev/ttyUSB0 get boot.py && \
ampy -p /dev/ttyUSB0 put boot.py  && \
ampy -p /dev/ttyUSB0 put main.py  && \
ampy -p /dev/ttyUSB0 put mqtt.py  && \
ampy -p /dev/ttyUSB0 put wifi.py  && \
ampy -p /dev/ttyUSB0 put micropython/awsCer/root-CA.der  && \
ampy -p /dev/ttyUSB0 put micropython/awsCer/teste.cert.der  && \
ampy -p /dev/ttyUSB0 put micropython/awsCer/teste.private.der  && \
ampy -p /dev/ttyUSB0 ls
```
###  Como entrar no dispositivo

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