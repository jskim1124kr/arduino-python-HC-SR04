import serial


ser = serial.Serial('COM3')
ser.flush()
ser.write([0])

print(ser.readline().decode())