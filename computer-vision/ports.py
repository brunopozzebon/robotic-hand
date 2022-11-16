import serial.tools.list_ports


class Ports:
    def __init__(self):

        self.serialInstance = serial.Serial()
        self.serialInstance.baudrate = 115200
        self.serialInstance.port = "COM4"

    def open(self):
        try:
            self.serialInstance.open()
        except Exception as e:
            print(e)

    def write(self, message):
        if self.serialInstance.is_open:
            finalMessage = message.encode("utf-8")
            self.serialInstance.write(finalMessage)
