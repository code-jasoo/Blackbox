#ifndef Blackbox_h
#define Blackbox_h
#include "Arduino.h"

#include <Adafruit_SSD1306.h>
#include <WiFi.h>

class Blackbox {
    public:
        Blackbox(int dataOut, int dataIn, int statusPin);
        void update();
        void begin();
    private:
        void pulse(int ms);
        void ping();
        void updateScreen();
        void send(int* message, int length);
        void receive(int* buffer, int size, int timeout);
        bool isMessage(int* buffer, int bufferSize, int* check, int checkSize);
        void updateWiFi();
        void connectToBrain();
        void saveToBrain(int* buffer, int size);
        void decodeSocket(char* buffer, int size);
        int binaryArrayToInt(int* binaryArray, int size);
        WiFiServer wifiServer;
        WiFiClient client;
        int _dataOut;
        int _dataIn;
        int _statusPin;
        bool _connectionStatus;
        bool _clientConnected;
        Adafruit_SSD1306 display;
};
#endif