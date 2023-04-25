# SPDX-FileCopyrightText: 2021 Pierre Constantineau
# SPDX-License-Identifier: MIT
from adafruit_hid.keycode import Keycode

"""
These keycodes are based on Universal Serial Bus HID Usage Tables Document
Version 1.12
Chapter 10: Keyboard/Keypad Page(0x07) - Page 53
https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
"""

class PK_Keycode(Keycode):
    NO        = 0x00
    XXXXXXX   = 0x00
    ROLL_OVER = 0x01
    TRANSPARENT = 0x01
    TRNS      = 0x01
    _______   = 0x01
    POST_FAIL = 0x02
    UNDEFINED = 0x03

    ENT  = 0x28
    ESC = 0x29
    BSPACE = 0x2A
    BSPC = 0x2A
    SPACE = 0x2C
    MINS = 0x2D

    EQUAL = 0x2E
    LBRACKET = 0x2F
    RBRACKET = 0x30
    BSLASH = 0x31
    NONUS_HASH = 0x32
    SCOLON = 0x33
    QUOT = 0x34
    GRAVE = 0x35
    COMM = 0x36
    DOT = 0x37
    SLASH = 0x38
    CAPSLOCK = 0x39
    CAPS = 0x39
    CLCK = 0x39
    DELETE = 0x4C
    DEL  = 0x4C
    INSERT = 0x49
    INS  = 0x49
    PSCREEN = 0x46
    SCROLLLOCK = 0x47
    PAUS = 0x48
    BRK  = 0x48
    PGUP = 0x4B
    PGDOWN = 0x4E
    RIGHT = 0x4F
    LEFT = 0x50
    DOWN = 0x51
    UP = 0x52
    NUMLOCK = 0x53
    KP_SLASH = 0x54
    KP_ASTERISK = 0x55
    KP_MINUS = 0x56
    KP_PLUS = 0x57
    KP_ENTER = 0x58
    KP_1 = 0x59
    KP_2 = 0x5A
    KP_3 = 0x5B
    KP_4 = 0x5C
    KP_5 = 0x5D
    KP_6 = 0x5E
    KP_7 = 0x5F
    KP_8 = 0x60
    KP_9 = 0x61
    KP_0 = 0x62
    KP_DOT = 0x63
    NONUS_BSLASH = 0x64
    APP  = 0x65
    KP_EQUAL = 0x67
    F20 = 0x6F
    F21 = 0x70
    F22 = 0x71
    F23 = 0x72
    F24 = 0x73
    EXECUTE = 0x74
    HELP = 0x75
    MENU = 0x76
    SELECT = 0x77
    STOP = 0x78
    AGAIN = 0x79
    UNDO = 0x7A
    CUT = 0x7B
    COPY = 0x7C
    PASTE = 0x7D
    FIND = 0x7E
    MUTE = 0x7F
    VOLUP = 0x80
    VOLDOWN = 0x81
    LOCKING_CAPS = 0x82
    LOCKING_NUM = 0x83
    LOCKING_SCROLL = 0x84
    KP_COMMA = 0x85
    KP_EQUAL_AS400 = 0x86
    INT1 = 0x87
    INT2 = 0x88
    INT3 = 0x89
    INT4 = 0x8A
    INT5 = 0x8B
    INT6 = 0x8C
    INT7 = 0x8D
    INT8 = 0x8E
    INT9 = 0x8F
    LANG1 = 0x90
    LANG2 = 0x91
    LANG3 = 0x92
    LANG4 = 0x93
    LANG5 = 0x94
    LANG6 = 0x95
    LANG7 = 0x96
    LANG8 = 0x97
    LANG9 = 0x98
    ALT_ERASE = 0x99
    SYSREQ = 0x9A
    CANCEL = 0x9B
    CLEAR = 0x9C
    PRIOR = 0x9D
    RETURN = 0x9E
    SEPARATOR = 0x9F
    OUT = 0xA0
    OPER = 0xA1
    CLEAR_AGAIN = 0xA2
    CRSEL = 0xA3
    EXSEL = 0xA4

    # LAST OF THE VALID KEYCODES ANYTHING BELOW SHOULD BE FILTERED OUT
    RESERVED_A5 = 0xA5  
    RESERVED_A6 = 0xA6
    RESERVED_A7 = 0xA7
    RESERVED_A8 = 0xA8
    RESERVED_A9 = 0xA9
    RESERVED_AA = 0xAA
    RESERVED_AB = 0xAB
    RESERVED_AC = 0xAC
    RESERVED_AD = 0xAD
    RESERVED_AE = 0xAE
    RESERVED_AF = 0xAF

    LAYER_0  =    0xF0
    LAYER_1  =    0xF1
    LAYER_2  =    0xF2
    LAYER_3  =    0xF3
    LAYER_4  =    0xF4
    LAYER_5  =    0xF5
    LAYER_6  =    0xF6
    LAYER_7  =    0xF7
    LAYER_8  =    0xF8
    LAYER_9  =    0xF9
    LAYER_A  =    0xFA
    LAYER_B  =    0xFB
    LAYER_C  =    0xFC
    LAYER_D  =    0xFD
    LAYER_E  =    0xFE
    LAYER_F  =    0xFF

    LCTL       = 0xE0
    LSFT      = 0xE1
    LSHIFT      = 0xE1
    #LALT        = 0xE2
    LGUI        = 0xE3
    LCMD        = 0xE3
    LWIN        = 0xE3
    RCTL       = 0xE4
    RSFT      = 0xE5
    RSHIFT      = 0xE5
    #RALT        = 0xE6
    RGUI        = 0xE7
    RCMD        = 0xE7
    RWIN        = 0xE7

    RGHT = RIGHT
    PGDN = PGDOWN
    PSCR = PSCREEN
    SLCK = SCROLLLOCK

    NLCK = NUMLOCK
    SPC  = SPACE
    EQL  = EQUAL
    GRV  = GRAVE
    RBRC = RBRACKET
    LBRC = LBRACKET
    
    BSLS = BSLASH
    SLSH = SLASH
    SCLN = SCOLON

    NUHS = NONUS_HASH
    NUBS = NONUS_BSLASH
    LCAP = LOCKING_CAPS
    LNUM = LOCKING_NUM
    LSCR = LOCKING_SCROLL
    ERAS = ALT_ERASE
    CLR  = CLEAR

    # Japanese specific
    ZKHK = GRAVE
    RO   = INT1
    KANA = INT2
    JYEN = INT3
    HENK = INT4
    MHEN = INT5
    # Korean specific
    HAEN = LANG1
    HANJ = LANG2
    # Keypad
    P1   = KP_1
    P2   = KP_2
    P3   = KP_3
    P4   = KP_4
    P5   = KP_5
    P6   = KP_6
    P7   = KP_7
    P8   = KP_8
    P9   = KP_9
    P0   = KP_0
    PDOT = KP_DOT
    PCMM = KP_COMMA
    PSLS = KP_SLASH
    PAST = KP_ASTERISK
    PMNS = KP_MINUS
    PPLS = KP_PLUS
    PEQL = KP_EQUAL
    PENT = KP_ENTER
    # Unix function key
    EXEC = EXECUTE
    SLCT = SELECT
    AGIN = AGAIN
    PSTE = PASTE
