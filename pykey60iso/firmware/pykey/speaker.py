
class PK_Speaker:

    def __init__(self, speaker_pin):
        import time
        import pwmio
        self.speaker_pin = speaker_pin
        self.buzzer = pwmio.PWMOut(speaker_pin, variable_frequency=True)
        self.buzzer.frequency = 440

    def play_startup_tune(self):
        OFF = 0
        ON = 2**15
        self.buzzer.duty_cycle = ON
        self.buzzer.frequency = 440
        time.sleep(0.05)
        self.buzzer.frequency = 880
        time.sleep(0.05)
        self.buzzer.frequency = 1660
        time.sleep(0.05)
        self.buzzer.duty_cycle = OFF

    def play_shutdown_tune(self):
        OFF = 0
        ON = 2**15
        self.buzzer.duty_cycle = ON
        self.buzzer.frequency = 1660
        time.sleep(0.05)
        self.buzzer.frequency = 880
        time.sleep(0.1)
        self.buzzer.frequency = 440
        time.sleep(0.15)
        self.buzzer.duty_cycle = OFF
