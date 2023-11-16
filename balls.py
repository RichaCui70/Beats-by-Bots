import serial

arduino_port = "COM3"
baud_rate = 9600

a = 1
try:
    ser = serial.Serial(arduino_port, baud_rate)
    while True:
        rfid = ser.readline().decode('utf-8').strip()
        if (rfid == "90EF9020"):
            print(a)
            a += 1
except Exception as e:
    print(f"Error: {e}")
finally:
    ser.close()