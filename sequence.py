from time import sleep

allPi = [
    "PI_1-",
    "PI_2-",
    "PI_3-",
    "PI_4-",
    "PI_5-",
    "PI_6-",
    "PI_7-",
    "PI_8-"
]

off = "0,0,0"

red = "255,0,0"
pink = "255,20,147"
purple = "138,43,226"
blue = "0,0,255"
turquoise = "0,255,144"
green = "0,255,0"
yellow = "255,255,0"

allCol = [
    red,
    pink,
    purple,
    blue,
    turquoise,
    green,
    yellow
]


def sendSeq(broadcast, conn):

    def send(pattern):
        broadcast(pattern, conn)

    # Each turquoise with half second delay
    for pi in allPi:
        send(pi + turquoise)
        print(pi + turquoise)
        sleep(0.5)

    print('sleeping 5 ....')
    sleep(5)

    # Each off
    send("ALL-" + off)
    print("ALL-" + off)

    print('sleeping 3 ....')
    sleep(3)

    # All rotate
    for col in allCol:
        send("ALL-" + col)
        print('sleeping 5....')
        sleep(3)

    print('sleeping 5 ....')

    # Each off reverse
    for pi in allPi[::-1]:
        send(pi + off)
        print(pi + off)
        print('sleeping 1 ....')
        sleep(1)

    print('Sequenced finished ...!')
