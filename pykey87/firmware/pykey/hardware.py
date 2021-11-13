# SPDX-FileCopyrightText: Copyright (c) 2021 Pierre Constantineau
#
# SPDX-License-Identifier: MIT
"""
`jpconstantineau_pykey`
================================================================================
A helper library for hardware keyboards
* Author(s): Pierre Constantineau

Implementation Notes
--------------------
**Hardware:**


**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

* Adafruit's CircuitPython NeoPixel library:
  https://github.com/adafruit/Adafruit_CircuitPython_NeoPixel

* Adafruit's CircuitPython HID library:
  https://github.com/adafruit/Adafruit_CircuitPython_HID

"""

import os
import usb_hid
from adafruit_hid.keyboard import Keyboard

class PK_Hardware:
    """
    Class representing a keyboard Hardware without the specifics...
    """

    def __init__(self):


        self._board_type = os.uname().machine
        self._keyboard = None
        self._pixels = None
        self._leds = None
        self._speaker =  None


    @property
    def keys(self):
        """
        The keys on the MacroPad. Uses events to track key number and state, e.g. pressed or
        released. You must fetch the events using ``keys.events.get()`` and then the events are
        available for usage in your code. Each event has three properties:
        * ``key_number``: the number of the key that changed. Keys are numbered starting at 0.
        * ``pressed``: ``True`` if the event is a transition from released to pressed.
        * ``released``: ``True`` if the event is a transition from pressed to released.
                        ``released`` is always the opposite of ``pressed``; it's provided
                        for convenience and clarity, in case you want to test for
                        key-release events explicitly.
        The following example prints the key press and release events to the serial console.
        .. code-block:: python
            from adafruit_macropad import MacroPad
            macropad = MacroPad()
            while True:
                key_event = macropad.keys.events.get()
                if key_event:
                    print(key_event)
        """
        return self._keys

    @property
    def encoder(self):
        """
        The rotary encoder relative rotation position. Always begins at 0 when the code is run, so
        the value returned is relative to the initial location.
        The following example prints the relative position to the serial console.
        .. code-block:: python
            from adafruit_macropad import MacroPad
            macropad = MacroPad()
            while True:
                print(macropad.encoder)
        """
        return self._encoder.position

    @property
    def speaker(self):
        return self._speaker

    @property
    def leds(self):
        return self._leds

    @property
    def pixels(self):
        """Sequence-like object representing the twelve NeoPixel LEDs in a 3 x 4 grid on the
        MacroPad. Each pixel is at a certain index in the sequence, numbered 0-11. Colors can be an
        RGB tuple like (255, 0, 0) where (R, G, B), or an RGB hex value like 0xFF0000 for red where
        each two digits are a color (0xRRGGBB). Set the global brightness using any number from 0
        to 1 to represent a percentage, i.e. 0.3 sets global brightness to 30%. Brightness defaults
        to 1.
        See ``neopixel.NeoPixel`` for more info.
        The following example turns all the pixels green at 50% brightness.
        .. code-block:: python
            from adafruit_macropad import MacroPad
            macropad = MacroPad()
            macropad.pixels.brightness = 0.5
            while True:
                macropad.pixels.fill((0, 255, 0))
        The following example sets the first pixel red and the twelfth pixel blue.
        .. code-block:: python
            from adafruit_macropad import MacroPad
            macropad = MacroPad()
            while True:
                macropad.pixels[0] = (255, 0, 0)
                macropad.pixels[11] = (0, 0, 255)
        """
        return self._pixels

    @property
    def keyboard(self):
        """
        A keyboard object used to send HID reports. For details, see the ``Keyboard`` documentation
        in CircuitPython HID: https://circuitpython.readthedocs.io/projects/hid/en/latest/index.html
        The following example types out the letter "a" when the rotary encoder switch is pressed.
        .. code-block:: python
            from adafruit_macropad import MacroPad
            macropad = MacroPad()
            while True:
                if macropad.encoder_switch:
                    macropad.keyboard.send(macropad.Keycode.A)
        """
        if self._keyboard is None:
            self._keyboard = Keyboard(usb_hid.devices)
        return self._keyboard

