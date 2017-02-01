import network 
import socket
import machine
from time import sleep

#led_integrado = machine.Pin(2, machine.Pin.OUT)

IN1 = machine.Pin(5, machine.Pin.OUT)
IN2 = machine.Pin(4, machine.Pin.OUT)
IN3 = machine.Pin(0, machine.Pin.OUT)
IN4 = machine.Pin(2, machine.Pin.OUT)

pines = (5, 4, 0, 2)
controles = (IN1, IN2, IN3, IN4)

# Configuro cada pin como salida. 
for pin in pines:
         machine.Pin(pin, machine.Pin.OUT)

# Pongo los pines en cero!.
def pines_cero():
	for pin in controles:
		pin.low()

SSID=''
PASS=''

def conectar_wifi(SSID, PASS):

	wlan = network.WLAN(network.STA_IF)
	wlan.active(True)
	wlan.connect(SSID, PASS)

	while not wlan.isconnected():
		print("Connecting to network...")
		sleep(5)

	if wlan.isconnected():
		print("Connected to network ", SSID)
		
		# led_integrado.low()
		print("Network settings: \n")
		print('{} {} {} {} {} {} {} {}'.format('IP:', wlan.ifconfig()[0],'Netmask: ', wlan.ifconfig()[1],'Gateway: ', wlan.ifconfig()[2],'DNS: ', wlan.ifconfig()[3]))


def escuchar_pedidos():
	# Preparo el socket
	addr = socket.getaddrinfo('0.0.0.0', 5000)[0][-1]

	s = socket.socket()
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(addr)
	s.listen(1)

	print("Esperando algun cliente en: ", addr)

	while True:
			cliente, direc = s.accept()
			if cliente:
				print("Conexion del cliente ", cliente )
				data = cliente.recv(50)
				if data: 
				# Decodifico lo que envia el cliente, que llega como un objeto del tipo "bytes"!. 
					data = bytes.decode(data)
#					print(data)

					pines_cero()

					if data == 'reversa':
						# der, reversa
						IN4.high()	#GPIO.output(23, 1)
						IN3.low() 	#GPIO.output(27, 0)

						# izq, reversa
						IN1.low()	#GPIO.output(17, 0)
						IN2.high()	#GPIO.output(22, 1)
						sleep(1)
						pines_cero()

						
					elif data == 'avanza':
						# izq, avanza
						IN1.high()	#GPIO.output(17, 1)
						IN2.low()	#GPIO.output(22, 0)

						# der, avanza 
						IN4.low()	#GPIO.output(23, 0)
						IN3.high()	#GPIO.output(27, 1)
						sleep(1)
						pines_cero()


					elif data == 'derecha':
						# der, avanza 
						IN4.low()	#GPIO.output(23, 0)
						IN3.high()	#GPIO.output(27, 1)
						sleep(0.5)
						pines_cero()

					elif data == 'izquierda':
						# izq, avanza
						IN1.high()	#GPIO.output(17, 1)
						IN2.low()	#GPIO.output(22, 0)
						sleep(0.5)
						pines_cero()

					elif data == 'rotar_derecha':
						# izq, avanza
						IN1.high()	#GPIO.output(17, 1)
						IN2.low()	#GPIO.output(22, 0)
						# der, reversa
						IN4.high()	#GPIO.output(23, 1)
						IN3.low()
						sleep(0.5)
						pines_cero()

					elif data == 'rotar_izq':
						# der, avanza 
						IN4.low()	#GPIO.output(23, 0)
						IN3.high()	#GPIO.output(27, 1)
						# izq, reversa
						IN1.low()	#GPIO.output(17, 0)
						IN2.high()	#GPIO.output(22, 1)
						sleep(0.5)
						pines_cero()

					cliente.close()

conectar_wifi('Mi_SSID', 'ClaveSecreta')
escuchar_pedidos()	
