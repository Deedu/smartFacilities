import requests
import serial

r=requests.post("http://www.dweet.io/dweet/for/nixon-is-pres1",
                data={"DogeProperty": 'Magnificent'})

serial_port = '/dev/ttyACM0'
baud_rate = 9600 #In arduino, Serial.begin(baud_rate)
write_to_file_path = "output.txt"

output_file = open(write_to_file_path, "w+")
ser = serial.Serial(serial_port, baud_rate)
while True:
    line = ser.readline()
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    print(line)
    output_file.write(line)