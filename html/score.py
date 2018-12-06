import argparse
# import RPi.GIPO as GPIO
import serial
import sqlite3
import string
import sys

# GPIO.setmode(GPIO.BOARD)

onlyWhiteSpaceAlphaNum = string.letters + string.digits + ' '
sqlDB = 'score.db'


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("arduinoName", required=True)

    args = parser.parse_args()

    ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
    ser.open()

    try:
        conn = sqlite3.connect(sqlDB)
    except Exception as e:
        print e
        sys.exit(1)

    # Forever loop
    while True:

        name = raw_input("Enter your name: ")
        name = ''.join(c for c in name if c in onlyWhiteSpaceAlphaNum)

        # TODO Get score from arduino
        score = ser.readline()

        conn.execute("INSERT INTO scores (name, score, device) VALUES ({},{},{})".format(name, score, args.arduinoName))


if __name__ == '__main__':
    Main()
