import argparse
import serial
import sqlite3
import string
import sys

onlyWhiteSpaceAlphaNum = string.letters + string.digits + ' '
sqlDB = 'score.db'


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-an", "--arduinoName", required=True, help="name of the arduino (expected a1 or a2)")
    parser.add_argument("-i", "--interface", required=True, help="arduino interface name, in format /dev/ttyUSB*")

    args = parser.parse_args()

    ser = serial.Serial(args.interface, 9600, timeout=1) # TODO verify interface is valid
    # ser.open()

    try:
        conn = sqlite3.connect(sqlDB)
    except Exception as e:
        print e
        sys.exit(1)

    # Forever loop
    while True:

        name = raw_input("Enter your name: ")
        name = ''.join(c for c in name if c in onlyWhiteSpaceAlphaNum)

        score = ''
        # TODO Get score from arduino
        while not len(score):
            score = ser.readline()

        conn.execute("INSERT INTO scores (name, score, device) VALUES ({},{},{})".format(name, score, args.arduinoName))
        conn.commit()

if __name__ == '__main__':
    Main()
