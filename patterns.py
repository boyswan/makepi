import time


def off(setLed):
    # "OFF",
    setLed(0.0, 0.0, 0.0)


def onTurquoise(setLed):
    # "TUR",
    setLed(0.0, 255.0, 127.0)


def onPink(setLed):
    # "PIN",
    setLed(255.0, 20.0, 147.0)


def onRed(setLed):
    # "RED",
    setLed(255.0, 0.0, 0.0)


def onBlue(setLed):
    # "BLU",
    setLed(0.0, 0.0, 255)


def onGreen(setLed):
    # "GRE",
    setLed(0.0, 255.0, 0.0)


def onPurple(setLed):
    # "PUR",
    setLed(138.0, 43.0, 226.0)


def onYellow(setLed):
    # "YEL"
    setLed(255.0, 255.0, 0.0)


def onSeq(setLed):
    onRed(setLed)
    time.sleep(5)
    onPink(setLed)
    time.sleep(5)


def getPattern(pattern, setLed):

    if (pattern == 'OFF'):
        off(setLed)
    elif (pattern == 'TUR'):
        onTurquoise(setLed)
    elif (pattern == 'PIN'):
        onPink(setLed)
    elif (pattern == 'RED'):
        onRed(setLed)
    elif (pattern == 'GRE'):
        onGreen(setLed)
    elif (pattern == 'PUR'):
        onPurple(setLed)
    elif (pattern == 'YEL'):
        onYellow(setLed)
    elif (pattern == 'BLU'):
        onBlue(setLed)
