import serial.tools.list_ports

class Ports:
    def __init__(self):
        ports = serial.tools.list_ports.comports()
        portsList=[]
        portVar ="COM3"

        for onePort in ports:
            portsList.append(str(onePort))

        val = 3
        for x in range(0,len(portsList)):
            if portsList[x].startswith("COM" + str(val)):
                portVar = "COM" + str(val)


        self.serialInstance = serial.Serial()
        self.serialInstance.baudrate = 9600
        self.serialInstance.port = portVar

    def open(self):
        try:
            self.serialInstance.open()
        except:
            print("Não foi possível abrir conexão com o arduino")

    def write(self, message):
        if self.serialInstance.is_open:
            finalMessage =  message.encode("utf-8")
            self.serialInstance.write(finalMessage)

