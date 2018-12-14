import argparse
import os.path
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
    
    if not os.path.exists(args.interface):
        print "{} Does not exist, exiting".format(args.interface)
        sys.exit(1)

    ser = serial.Serial(args.interface, 9600, timeout=1) # TODO verify interface is valid
    # ser.open()

    try:
        conn = sqlite3.connect(sqlDB)
    except Exception as e:
        print e
        sys.exit(2)

    # Forever loop
    while True:

        inName = raw_input("Enter your name: ")
        inName = ''.join(c for c in name if c in onlyWhiteSpaceAlphaNum)

        score = ''
        # TODO Get score from arduino
        while not len(score):
            score = ser.readline()

        conn.execute("INSERT INTO scores (name, score, device) VALUES ({},{},{})".format(inName, score, args.arduinoName))
        conn.commit()

def Main2():
    parser = argparse.ArgumentParser()
    parser.add_argument("-an", "--arduinoName", required=True, help="name of the arduino (expected a1 or a2)")
    
    args = parser.parse_args()
    
    try:
        conn = sqlite3.connect(sqlDB)
    except Exception as e:
        print e
        sys.exit(1)
        
    while True:
        inName = raw_input("Enter your name: ")
        inName = ''.join(c for c in inName if c in onlyWhiteSpaceAlphaNum)
        while True:
            score = raw_input("Enter the Score: ")
            score = ''.join(c for c in score if c in (string.digits + '-'))
            if len(score) > 1 and score[0] == '-':
                score = score[0] + ''.join(c for c in score[1:] if c in string.digits)
            else:
                score = ''.join(c for c in score if c in string.digits)
            if len(score) > 0:
                if int(score) > 7:
                    score = 7
                elif int(score) < -7:
                    score = -7
                break
                
        conn.execute("INSERT INTO scores (name, score, device) VALUES ({},{},{})".format(inName, score, args.arduinoName))
        conn.commit()
        
        
if __name__ == '__main__':
    # Main()
    Main2()
