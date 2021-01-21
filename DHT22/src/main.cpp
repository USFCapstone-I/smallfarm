#include <Arduino.h>
#include "DHTesp.h"

#define DHTPIN 13
DHTesp dht;

void setup() {
  Serial.begin(115200);
  Serial.println(F("DHT22 test!"));
  dht.setup(DHTPIN, dht.DHT22);
  //dht.begin();
}

void loop() {
  delay(4000);
  // Reading temperature or humidity takes about 250 milliseconds! Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  
  float h = dht.getHumidity();
  float t = dht.getTemperature(); // in C (default)
  float f = dht.toFahrenheit(t); // Read temperature as Fahrenheit (isFahrenheit = true)
  // f = toCelsius(f);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C"));
}