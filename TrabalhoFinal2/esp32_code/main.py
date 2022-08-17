import network
import urequests
import time
from machine import Pin, Timer, PWM, ADC
from wifi_manager import WifiManager

wm = WifiManager()

lampada_quarto = PWM(Pin(2))
lampada_sala = PWM(Pin(4))
lampada_suite = PWM(Pin(5))
lampada_cozinha = PWM(Pin(15))
ventilador_quarto = PWM(Pin(16))
ventilador_sala = PWM(Pin(17))
climatizador_suite = PWM(Pin(18))
forno = PWM(Pin(19))
liquidificador = PWM(Pin(21))
tim0 = Timer(0)
sensor_temperatura = ADC(Pin(34))

temperatura = 0

def connect_wifi():
    wifi = network.WLAN(network.STA_IF)
    wifi.active(False)
    wifi.active(True)
    wifi.disconnect()
    wifi.connect('PAULO-RAFA-JOSSY','rafanin2602')
    if not wifi.isconnected():
        print('connecting..')
        timeout = 0
        while (not wifi.isconnected() and timeout < 5):
            print(5 - timeout)
            timeout = timeout + 1
            time.sleep(1)
    if(wifi.isconnected()):
        print('connected')
    else:
        print('not connected')

def timer_callback(timer):
    global temperatura
    temperatura = sensor_temperatura.read_u16()*50/65535


def att_gpio(gpio):
    if gpio['lampada_quarto'][0] == 'on':
        lampada_quarto.duty_u16(int(gpio['lampada_quarto'][1]))
    else:
        lampada_quarto.duty_u16(0)
    if gpio['lampada_sala'][0] == 'on':
        lampada_sala.duty_u16(int(gpio['lampada_sala'][1]))
    else:
        lampada_sala.duty_u16(0)
    if gpio['lampada_suite'][0] == 'on':
        lampada_suite.duty_u16(int(gpio['lampada_suite'][1]))
    else:
        lampada_suite.duty_u16(0)
    if gpio['lampada_cozinha'][0] == 'on':
        lampada_cozinha.duty_u16(int(gpio['lampada_cozinha'][1]))
    else:
        lampada_cozinha.duty_u16(0)
    if gpio['ventilador_sala'][0] == 'on':
        ventilador_sala.duty_u16(int(gpio['ventilador_sala'][1]))
    else:
        ventilador_sala.duty_u16(0)
    if gpio['ventilador_quarto'][0] == 'on':
        ventilador_quarto.duty_u16(int(gpio['ventilador_quarto'][1]))
    else:
        ventilador_quarto.duty_u16(0)
    if gpio['climatizador_suite'][0] == 'on':
        climatizador_suite.duty_u16(int(gpio['climatizador_suite'][1]))
    else:
        climatizador_suite.duty_u16(0)
    if gpio['forno'][0] == 'on':
        forno.duty_u16(int(gpio['forno'][1]))
    else:
        forno.duty_u16(0)
    if gpio['liquidificador'][0] == 'on':
        liquidificador.duty_u16(int(gpio['liquidificador'][1]))
    else:
        liquidificador.duty_u16(0)
    

def app_init():
    #connect_wifi()
    wm.connect()
    tim0.init(period=1000, mode=Timer.PERIODIC, callback=timer_callback)
    

def app_loop():
    while True:
        if wm.is_connected():
            gpio = urequests.get('http://rafaeldaysiot-env.eba-kyfwcpag.sa-east-1.elasticbeanstalk.com/get-data' + '?temp=' + str(round(temperatura,1))).json()
            att_gpio(gpio)
        else:
            print('Not connected, yet!')
        

app_init()
app_loop()