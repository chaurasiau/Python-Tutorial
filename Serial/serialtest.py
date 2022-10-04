import serial

# we need to install pyserial
ser = serial.Serial(port='COM4', baudrate=19200, bytesize=8,
                    parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)

print(f"Port Name is - {ser.name}")
print(f"Is the Port Opend - {ser.is_open}")
ser.close()
print(f"Is the Port Opend - {ser.is_open}")
