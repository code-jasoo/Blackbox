#ifndef Blackbox_h
#define Blackbox_h
#include "Arduino.h"

#include <Adafruit_SSD1306.h>

class Blackbox {
    public:
        Blackbox(int dataOut, int dataIn, int statusPin);
        void update();
    private:
        void pulse(int ms);
        void ping();
        void updateScreen();
        void receive(int* buffer, int size, int timeout);
        int _dataOut;
        int _dataIn;
        int _statusPin;
        bool _connectionStatus;
        Adafruit_SSD1306 display;
};
#endif