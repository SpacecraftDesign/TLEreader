#include <ESP8266WiFi.h>

#include <ESP8266HTTPClient.h>


const char* ssid = "SFR_B228";
const char* password = "9kpm59hjht6cay63arwa";

WiFiClient Client;
#define host "www.celestrak.com"

//const char fingerprint[] PROGMEM = "3a ce 54 bc 41 42 e7 4f 54 60 c9 3c a9 e7 a8 71 1b 5a 5e 1c";
const int httpsPort = 80; //443 for HTTPS

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid,password);
  Serial.flush();  // not sure what this command does
  Serial.println("Connecting to wifi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("...");
  }

  makeHTTPSrequest();
}

void makeHTTPSrequest(){

  if (WiFi.status() == WL_CONNECTED) {
      Serial.println("Connected to WiFi");
      //httpsClient.setFingerprint(fingerprint);
      //httpsClient.setTimeout(1000);
      delay(1000);
      int val = httpsClient.connect(testHost, 80);
      Serial.println(val);
      if (httpsClient.connect(host, 80) > 0){
        Serial.println(F("Ready for request"));
        return;
      }
      char c = 0;
      while(httpsClient.available()){
        Serial.println("The Client is available");
        httpsClient.readBytes(&c,1);
        Serial.println(c);
      }

  }
}

void loop() {
}
