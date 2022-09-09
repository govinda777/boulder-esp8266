.PHONY: deploy
deploy:
	@cd src && ampy -p /dev/ttyUSB0 put boot.py  && ampy -p /dev/ttyUSB0 put main.py  && ampy -p /dev/ttyUSB0 put mqtt.py  && ampy -p /dev/ttyUSB0 put wifi.py  && ampy -p /dev/ttyUSB0 put micropython/awsCer/root-CA.der  && ampy -p /dev/ttyUSB0 put micropython/awsCer/teste.cert.der  && ampy -p /dev/ttyUSB0 put micropython/awsCer/teste.private.der