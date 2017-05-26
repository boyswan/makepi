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

allCol = [
    "RED",
    "PIN",
    "PUR",
    "BLU",
    "TUR",
    "GRE",
    "YEL"
]


def sendSeq(broadcast, conn):

    def send(pattern):
        broadcast(pattern, conn)

    for pi in allPi:
        send(pi + "TUR")
        print(pi + "TUR")
        sleep(0.25)

    print('sleeping 2 ....')
    sleep(2)

    for pi in allPi:
        send(pi + "OFF")
        print(pi + "OFF")
        sleep(0.25)

    print('sleeping 2 ....')
    sleep(2)

    for col in allCol:
        for pi in allPi:
            send(pi + col)
            print(pi + col)
            sleep(0.25)
        print('sleeping 6 ....')
        sleep(2)

    print('sleeping 2 ....')
    sleep(2)

    for pi in allPi[::-1]:
        send(pi + "OFF")
        print(pi + "OFF")
        print('sleeping 1 ....')
        sleep(0.5)

    print('Sequenced finished ...!')
