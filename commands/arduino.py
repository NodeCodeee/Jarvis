import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portsList = []

for one in ports:
    portsList.append(str(one))
    print(str(one))

com = input("Select Com Port for Arduino #: ")
# com = 3
for i in range(len(portsList)):
    if portsList[i].startswith("COM" + str(com)):
        use = "COM" + str(com)
        print(use)

serialInst.baudrate = 9600
serialInst.port = use
serialInst.open()


async def turnOn():

    command = "ON"
    serialInst.write(command.encode('utf-8'))

async def turnOff():

    command = "OFF"
    serialInst.write(command.encode('utf-8'))



