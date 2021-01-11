# -*- coding: utf-8 -*-

#======================================
# DHT11 CSV Tool
#======================================
# For Python3

# Revision
# 20210111 r1

# Import
import dht11
import RPi.GPIO as GPIO
import time
import datetime
import csv
import sys
import os

# Define
Temp_sensor = 2                 # GPIO 2 as DHT11 data pin.
CSV_file = "Result.csv"         # Result File Name
RecentData = "RecentResult.csv" # Recent Result File Name
Loop_num = 1000                 # Loop Rimit

# Main
def main():

    # DATE&TIME
    today = datetime.datetime.fromtimestamp(time.time())
    today.strftime("%Y/%m/%d %H:%M:%S")

    # GPIO Setting
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    # Read Sensor
    num = 0
    while (num < Loop_num):

        instance = dht11.DHT11(pin = Temp_sensor)
        result = instance.read()

        if result.temperature == 0 & result.humidity == 0:
            num += 1

        else:
            break

    else:
        print("Sensor Read Error.")
        sys.exit()

    # Print Data
    print(today.strftime("%Y/%m/%d %H:%M:%S"),\
        ",",\
        "Temperature:",result.temperature,"C",\
        ",",\
        " Humidity:",result.humidity,"%")

    # CSV File Absolute File Path
    Result_path = os.path.dirname(os.path.abspath(__file__)) + "/" + CSV_file
    Recent_path = os.path.dirname(os.path.abspath(__file__)) + "/" + RecentData

    # CSV File Output
    with open(Result_path, "a") as f:
        writer = csv.writer(f)
        writer.writerow([today.strftime("%Y/%m/%d %H:%M:%S"),result.temperature,result.humidity])

    # CSV File Output [Recent]
    with open(Recent_path, "w") as f:
        writer = csv.writer(f)
        writer.writerow([today.strftime("%Y/%m/%d %H:%M:%S"),result.temperature,result.humidity])

    time.sleep(1)

    # GPIO Cleanup
    GPIO.cleanup()

if __name__ == "__main__":

    try:
        main()

    except KeyboardInterrupt:
        pass
