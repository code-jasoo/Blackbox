# Blackbox
Simple autonomous programming and data transfer for VEX Robotics.

### Dependencies for Blackbox device
- [Adafruit_SSD1306 Library](https://github.com/adafruit/Adafruit_SSD1306) (version 2.5.13 used)
- [Adafruit GFX Library](https://github.com/adafruit/Adafruit-GFX-Library) (version 1.11.11 used)

## Why?
While developing auton programs for our robot, a majority of the time is waiting for the program to recompile and download onto the robot. To expedite this process, I created Blackbox (along with custom PID commands) which can wirelessly download auton programs onto the robot's micro SD card without needing to recompile the entire program.

## How?
The Blackbox uses a simple one wire protocol which utilizes small digital pulses. Depending on the length of the pulse, it will represent 0 or 1 in binary. The first four bits in the binary array will represent the opcode. The length of the command will be based on the opcode, for example, if the opcode were `moveForward`, the parameters will be the distance which will be represented using 8 bits (1 byte), therefore, the complete length of the command will be 12 bits. Binary is used for the commands to make data transferring faster as the one wire protocol is limited to a 10ms pulse minimum which is very long. This is due to the sample rate of the three wire ports on the VEX V5 Brain.

## Is this legal?
This *should* be legal as long as the Blackbox device is not used during competitions. The Blackbox device is *only* supposed to download the auton programs quickly. Again, this <ins>**should not be used during competitions**</ins>. Although, I believe in VEXU, microcontroller use is legal but <ins>**I do not know as I am not doing VEXU. Please refer to the VEXU rules!**</ins>

## Do I need a Blackbox?
No you don't! You can simply download the auton programs into an SD card directly.

## Feedback
If you have any issues or would like to give feedback, please feel free to open up an issue.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
