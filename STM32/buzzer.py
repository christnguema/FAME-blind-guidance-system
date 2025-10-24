import pyb
import time

class Buzzer():
    def __init__(self):
        self.buzzer = pyb.Pin('D5')
        self.tim = pyb.Timer(2, freq=440)  # La 440 Hz
        self.ch = self.tim.channel(1, pyb.Timer.PWM, pin=self.buzzer)
        self.notes = [262, 294, 330, 349, 392, 440, 494, 523]  # Do Ré Mi Fa Sol La Si Do

    def sing(self):
        for freq in self.notes:
            self.tim.freq(freq)
            self.ch.pulse_width_percent(50)
            time.sleep(0.3)
            self.ch.pulse_width_percent(0)
            time.sleep(0.1)
            
        time.sleep(0.5)
        
        for i in range((len(self.notes) - 1), 0, -1):
            self.tim.freq(self.notes[i])
            self.ch.pulse_width_percent(50)
            time.sleep(0.3)
            self.ch.pulse_width_percent(0)
            time.sleep(0.1)

        self.ch.pulse_width_percent(0)

    #--------------- DO ----------------------------------------------------
    def sing_do1(self):
        self.tim.freq(262)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)
        
    def sing_do2(self):
        self.tim.freq(524)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)
        
    def sing_do3(self):
        self.tim.freq(1048)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)
        
    def sing_do4(self):
        self.tim.freq(2096)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)
        
    def sing_do5(self):
        self.tim.freq(4192)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    #--------------- RÉ ----------------------------------------------------
    def sing_re1(self):
        self.tim.freq(294)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_re2(self):
        self.tim.freq(588)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_re3(self):
        self.tim.freq(1176)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_re4(self):
        self.tim.freq(2352)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_re5(self):
        self.tim.freq(4704)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    #--------------- MI ----------------------------------------------------
    def sing_mi1(self):
        self.tim.freq(330)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_mi2(self):
        self.tim.freq(660)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_mi3(self):
        self.tim.freq(1320)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_mi4(self):
        self.tim.freq(2640)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_mi5(self):
        self.tim.freq(5280)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    #--------------- FA ----------------------------------------------------
    def sing_fa1(self):
        self.tim.freq(349)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_fa2(self):
        self.tim.freq(698)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_fa3(self):
        self.tim.freq(1396)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_fa4(self):
        self.tim.freq(2792)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_fa5(self):
        self.tim.freq(5584)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    #--------------- SOL ----------------------------------------------------
    def sing_sol1(self):
        self.tim.freq(392)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_sol2(self):
        self.tim.freq(784)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_sol3(self):
        self.tim.freq(1568)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_sol4(self):
        self.tim.freq(3136)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_sol5(self):
        self.tim.freq(6272)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    #--------------- LA ----------------------------------------------------
    def sing_la1(self):
        self.tim.freq(440)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_la2(self):
        self.tim.freq(880)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_la3(self):
        self.tim.freq(1760)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_la4(self):
        self.tim.freq(3520)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_la5(self):
        self.tim.freq(7040)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    #--------------- SI ----------------------------------------------------
    def sing_si1(self):
        self.tim.freq(494)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_si2(self):
        self.tim.freq(988)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_si3(self):
        self.tim.freq(1976)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_si4(self):
        self.tim.freq(3952)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)

    def sing_si5(self):
        self.tim.freq(7904)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)
    
    def sing_note(self, freq):
        self.tim.freq(freq)
        self.ch.pulse_width_percent(50)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)
        
    def sing_note_wdc(self, freq, duty_cycle):
        self.tim.freq(freq)
        self.ch.pulse_width_percent(duty_cycle)
        time.sleep(0.3)
        self.ch.pulse_width_percent(0)
        time.sleep(0.1)
        
    def sing_warning(self, ctn=3):
        while ctn != 0:
            self.sing_note_wdc(1976, 80)
            self.sing_note_wdc(1976, 80)
            time.sleep(0.4)
            ctn = ctn - 1
        
# ----------- Fur Elise --------------------------------------------------------  
    def play_fur_elise(self):
        """
        Joue une version simplifiée de Für Elise (Beethoven) en environ 2 minutes.
        Basée sur les notes principales, adaptée au buzzer.
        """
        tempo = 0.25  # durée de base pour une note courte (~0.25 s)
        long_note = 2 * tempo
        short_pause = 0.05

        # Première partie du thème principal
        sequence = [
            ("mi3", tempo), ("re#3", tempo), ("mi3", tempo), ("re#3", tempo),
            ("mi3", tempo), ("si2", tempo), ("re3", tempo), ("do3", tempo),
            ("la2", long_note),

            ("do2", tempo), ("mi2", tempo), ("la2", tempo), ("si2", long_note),
            ("mi2", tempo), ("sol#2", tempo), ("si2", tempo), ("do3", long_note),

            ("mi3", tempo), ("re#3", tempo), ("mi3", tempo), ("re#3", tempo),
            ("mi3", tempo), ("si2", tempo), ("re3", tempo), ("do3", tempo),
            ("la2", long_note),

            ("do2", tempo), ("mi2", tempo), ("la2", tempo), ("si2", long_note)
        ]

        # La mélodie fait environ 32 notes. On répète pour atteindre ~2 minutes.
        repeat_count = 6  # 6 répétitions pour ~120 secondes

        for _ in range(repeat_count):
            for note, duration in sequence:
                method_name = f"sing_{note}"
                if hasattr(self, method_name):
                    getattr(self, method_name)()
                else:
                    # Note inconnue, on fait une pause
                    time.sleep(duration)
                time.sleep(short_pause)

