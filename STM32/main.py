# ************ Import des modules internes ******************************************
import time    # time.sleep(temps en seconde) | time.sleep_us(temps en microseconde)

# ************ Import des modules externes ******************************************
from ble import BLEPresenceSensor

# *************** Programme principal ************************************************
sensor = BLEPresenceSensor() # Instantiation de la classe BLEPresenceSensor

#**************** Boucle principale **************************************************
while True:
    sensor.send_presence() # Envoie de la distatance mesurée par BLE
    time.sleep(1)		   # chaque demi-seconde (500 ms)

