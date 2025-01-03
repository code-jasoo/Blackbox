#ifndef Blackbox_h
#define Blackbox_h
#include "Arduino.h"

class Blackbox {
    public:
        Blackbox(int dataOut, int dataIn, int statusPin);
    private:
        void pulse(int ms);
        int _dataOut;
        int _dataIn;
        int statusPin;
};
#endif