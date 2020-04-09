#define JUMP_SENSOR_PIN A0
#define DUCK_SENSOR_PIN A1

void setup() {
    Serial.begin(9600);
}

void loop() {
    int jump_data = analogRead(JUMP_SENSOR_PIN);
    int duck_data = analogRead(DUCK_SENSOR_PIN);

    if (jump_data >= 250) {
        Serial.println("jump");
        delay(100);
    }

    if (duck_data >= 250) {
        Serial.println("duck");
        delay(100);
    }
}
