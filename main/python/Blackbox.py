class Blackbox:
    def __init__(self, dataIn, dataOut):
        self.dataIn = DigitalIn(dataIn)
        self.dataOut = DigitalOut(dataOut)

        self.timer = Timer()
        self.pulseStart = 0

        self.plusMinus = 100 # in microseconds
        self.timeOut = 300000 # in microseconds

        self.isConnected = False
        self.isDownloading = False

        self.backgroundThreadReceiver = Thread(self.__backgroundThreadReceiver)
        print("hello")
    
    def __backgroundThreadReceiver(self):
        pulseTime = 0
        lastTime = 0
        buffer = []
        while True:
            # When port is pulled HIGH and there is no ongoing pulse
            if self.dataIn.value() == 1 and self.pulseStart == 0:
                # Set the start of the pulse
                self.pulseStart = self.timer.system_high_res()
                # Set the last time a pulse was recorded
                lastTime = self.timer.system_high_res()
            # When port is pulled LOW and there is an ongoing pulse
            if self.dataIn.value() == 0 and self.pulseStart != 0:
                # Calculate the pulse time
                pulseTime = self.timer.system_high_res() - self.pulseStart
                # Reset the pulseStart time for next pulse
                self.pulseStart = 0

                if pulseTime >= 10000 - self.plusMinus and pulseTime <= 10000 + self.plusMinus:
                    buffer.append(0)
                if pulseTime >= 20000 - self.plusMinus and pulseTime <= 20000 + self.plusMinus:
                    buffer.append(1)
            # If pulses timed out, decode buffer
            if self.timer.system_high_res() - lastTime >= self.timeOut:
                
                # If we are downloading
                if len(buffer) != 0 and self.isDownloading:
                    print(''.join(str(x) for x in buffer))
                    # The download is finished
                    self.isDownloading = False

                    # Send received number of bits for redunancy (horrible data loss checking fr)
                    print(len(buffer))
                    print("sending length received")
                    tempThread = Thread(self.__backgroundThreadSender, ([int(x) for x in '{0:08b}'.format(len(buffer))],))

                if len(buffer) != 0 and buffer == [1, 1, 1, 1, 0, 0, 0, 0]:
                    print("not connected.. sending handshake")
                    tempThread = Thread(self.__backgroundThreadSender, (buffer.copy(),))
                    self.isConnected = True
                elif len(buffer) != 0 and buffer == [1, 0, 0, 1]:
                    print("we are about to download a program")
                    tempThread = Thread(self.__backgroundThreadSender, ([0, 1, 1, 0],))
                    self.isDownloading = True

                # Reset buffer
                buffer.clear()


    def __backgroundThreadSender(self, args):
        buffer = args
        for bit in buffer:
            if bit == 0:
                self.dataOut.set(True)
                wait(10)
                self.dataOut.set(False)
                wait(10)
            if bit == 1:
                self.dataOut.set(True)
                wait(20)
                self.dataOut.set(False)
                wait(10)