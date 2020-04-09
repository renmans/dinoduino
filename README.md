# Dinoduino

![Dinoduino Gif](src/img/game.gif)

The program responds to changes in sensor readings and sends data to the virtual keyboard for control.

## Simple solution
If you have Leonardo, Esplora, Zero or Due boards, solution looks like this (you don't need a python script):

```C++
#include <Keyboard.h>

#define JUMP_SENSOR_PIN A0
#define DUCK_SENSOR_PIN A1

void setup() {
    Keyboard.begin();
}

void loop() {
    int jump_data = analogRead(JUMP_SENSOR_PIN);
    int duck_data = analogRead(DUCK_SENSOR_PIN);

    if (jump_data >= 250) {
        Keyboard.write(0x20);
    }

    if (duck_data >= 250) {
        Keyboard.write(0xE0);
        Keyboard.write(0x50);
    }
}
```

## Running
Assemble the device as shown in diagram

![Assembly Diagram](src/img/diagram.png)

Attach photoresistors to the points shown in image

![Attachment Points](src/img/points.png)

Upload sketch to the Board and connect it to your computer using Arduino IDE

Install necessary libraries and run script
```
pip install -r requirements.txt
python3 main.py
```
