# ***************** Import des librairies ***************************************************
from bluetooth import BLE, UUID, FLAG_NOTIFY
import struct
import pyb
import time
import utime
import machine

from fonctions import log # Affiche un message dans la console (comme print) et enregistre le
# message dans un fichier .log
from buzzer import Buzzer
buz = Buzzer()
# *******************************************************************************************

#****************** Configuration GPIO ******************************************************
# Configuration des broches du HC-SR04
trigger = pyb.Pin('D3', pyb.Pin.OUT_PP) # Broche TRIG liée au HCSR04 en sortie push-pull
echo = pyb.Pin('D4', pyb.Pin.IN) # Broche Echo liée au HCSR04 en entrée

LED1 = pyb.LED(1) # LED bleu de la carte STM32
# *******************************************************************************************

# *************** Classe de gestion du BLE **************************************************
class BLEPresenceSensor:
#   Méthode d'initialisation ou encore fonction constructeur (jargon)
    def __init__(self, name="HC_SR04_Sensor"):
        self.ble = BLE()
        self.ble.active(True)
        self.ble.irq(self._irq)

        self.name = name
        self._connections = set()

        self._uuid_service = UUID("12345678-1234-5678-1234-56789abcdef0")
        self._uuid_presence_char = UUID("abcdef01-1234-5678-1234-56789abcdef0")

        self._presence_handle = None
        self._register_services()
        self._advertise(self.name)

#   Méthode d'enregistrement des services BLE
    def _register_services(self):
        service = (
            self._uuid_service,
            ((self._uuid_presence_char, FLAG_NOTIFY),)
        )
        ((self._presence_handle,),) = self.ble.gatts_register_services((service,))

#   Méthode de "publicité" pour la visibilité Bluetooth de notre appareil (STM32)
    def _advertise(self, name):
        payload = bytearray(
            b'\x02\x01\x06' +
            bytes([len(name) + 1, 0x09]) +
            name.encode('utf-8')
        )
        self.ble.gap_advertise(100_000, payload)
        log("Attente de connexion BLE ...")

#   Gestion des évènements BLE en interruption (connexion | déconnexion)
    def _irq(self, event, data):
        if event == 1:  # Connect
            conn_handle, _, _ = data
            self._connections.add(conn_handle)
            log("BLE connecté")
            buz.sing_mi2()
        elif event == 2:  # Disconnect
            conn_handle, _, _ = data
            self._connections.discard(conn_handle)
            self._advertise(self.name)
            log("BLE déconnecté")
            buz.sing_do2()
            log("")
    
#   Méthode de mesure de distance
    def read_distance(self):
        trigger.low()
        time.sleep_us(2)
        trigger.high()
        time.sleep_us(10)
        trigger.low()

        start = time.ticks_us()
        while echo.value() == 0:
            start = time.ticks_us()
        while echo.value() == 1:
            end = time.ticks_us()

        duration = time.ticks_diff(end, start)
        distance_cm = duration / 58.0
        log(f"Distance mesurée : {distance_cm : .2f} cm")
        return int(distance_cm)

#   Méthode d'envoie de la distance mesurée via BLE (GATT)
    def send_presence(self):
        if not self._connections:
            return

        LED1.on()
        distance = self.read_distance()
        timestamp = int(time.time())
    
        if distance <= 30:
            buz.sing_si3()
            buz.sing_si3()
            buz.sing_si3()
        elif distance <= 70:
            buz.sing_re3()
            buz.sing_re3()
        elif distance <= 120:
            buz.sing_re1()
            buz.sing_re1()
        else:
            print("----------------------------")
            #buz.sing_do1()
        
        data = struct.pack("<HI", distance, timestamp)
        for conn in self._connections:
            self.ble.gatts_notify(conn, self._presence_handle, data)
        LED1.off()
# *******************************************************************************************



