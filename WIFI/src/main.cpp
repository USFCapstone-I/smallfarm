#include <WiFi.h>
#include <WiFiClientSecure.h>

const char* ssid = "HERE"; // replace HERE with your wifi name
const char* password =  "HERE"; // replace HERE with your wifi password
 
void setup() {
 
  Serial.begin(115200);
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to the WiFi network");
}
 
void loop() {}