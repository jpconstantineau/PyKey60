


class PK_LEDMatrix:
# LEDMatrix(row_pins: Sequence[microcontroller.Pin], column_pins: Sequence[microcontroller.Pin], columns_to_anodes: bool = True)


    def __init__(self, row_pins, column_pins, columns_to_anodes: bool = True):
        from digitalio import DigitalInOut, Direction
        self.row_pins = row_pins
        self.column_pins = column_pins
        self.columns_to_anodes = columns_to_anodes
        self.column_io = []
        self.row_io = []
        for cp in self.column_pins:
            self.column_io.append(DigitalInOut(cp))
        for rp in self.row_pins:
            self.row_io.append(DigitalInOut(rp))

    def reset_leds(self):
        for pin in self.row_io:
            pin.direction = Direction.OUTPUT
            pin.value = False
        for pin in self.column_io:
            pin.direction = Direction.OUTPUT
            pin.value = False

    def led_ON(self, led_number):
        self.reset_leds()
        colcount=len(self.column_io)
        colIOLED = self.column_io[0]
        rowIOLED = self.row_io[0]
        for rownum, rowIO in enumerate(self.row_io):
            for colnum, colIO in enumerate(self.column_io):
                if led_number == (rownum * colcount + colnum):
                    colIOLED = colIO
                    rowIOLED = rowIO
                if self.columns_to_anodes:
                    colIO.value = False
                    rowIO.value = True
                else:
                    colIO.value = True
                    rowIO.value = False
        if self.columns_to_anodes:
            colIOLED.value = True
            rowIOLED.value = False
        else:
            colIOLED.value = False
            rowIOLED.value = True

    def led_OFF(self):
        self.reset_leds()

