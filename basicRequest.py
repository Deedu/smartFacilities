import requests
import serial

serial_port = '/dev/tty96B0'
baud_rate = 9600 #In arduino, Serial.begin(baud_rate)
write_to_file_path = "output.txt"

output_file = open(write_to_file_path, "w+")
ser = serial.Serial(serial_port, baud_rate)
peopleSinceLastClean = 0
methaneLevel=0
buttonPushed = False  # Button is pushed to reset count
doorPassConstant =100

while True:
    line = ser.readline()
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    line = line.split('~')

    ## Line Order is
    ##               buttonPushed~distanceMeasurement~PhotoMeasurement~MethaneMeasurement1~MethaneMeasurement2
    buttonPushed = line[0]
    distance = int(line[1])
    if(distance < doorPassConstant):
        peopleSinceLastClean +=1
    if buttonPushed=="1":
        peopleSinceLastClean=0
    photoLevel = int(line[2])
    methaneLevel1 = int(line[3])
    methaneLevel2 = int(line[4])

    names = ["peopleSinceLastClean","photoLevel", "methaneLevel1","methaneLevel2"]
    r = requests.post("http://www.dweet.io/dweet/for/lesDragooner1",
                      data={"People_since_last_clean": peopleSinceLastClean,
                            "Methane_level": methaneLevel,
                            "Button Pushed": buttonPushed})

    print(line)
    output_file.write(line)
