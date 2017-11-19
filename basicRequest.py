import requests
import serial

serial_port = '/dev/tty96B0'
baud_rate = 9600 #In arduino, Serial.begin(baud_rate)
write_to_file_path = "output.txt"

output_file = open(write_to_file_path, "w+")
ser = serial.Serial(serial_port, baud_rate)
peopleSinceLastClean = 0
methaneLevel=0
buttonPushedCount = 0  # Button is pushed to reset count
doorPassConstant =100
previousPushTrueCount = 0

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
        buttonPushedCount +=1
        previousPushTrueCount +=1
    else:
        previousPushTrueCount=0
    photoLevel = int(line[2])
    methaneLevel1 = int(line[3])
    methaneLevel2 = int(line[4])

    if(previousPushTrueCount >5):
        peopleSinceLastClean = 0
        
    names = ["peopleSinceLastClean","photoLevel", "methaneLevel1","methaneLevel2", "buttonPushCount"]
    datasets = [peopleSinceLastClean,photoLevel,methaneLevel1,methaneLevel2, buttonPushedCount]

    dataDict = {}
    for name in names:
        dataDict[name] = datasets[names.index(name)]

    r = requests.post("http://www.dweet.io/dweet/for/lesDragooner1",
                      data=dataDict)
    if(peopleSinceLastClean >=50):
        r2 = requests.post("https://hooks.zapier.com/hooks/catch/2688900/s9rhbo/", data={'doge': "Orange doge"})

    print(line)
