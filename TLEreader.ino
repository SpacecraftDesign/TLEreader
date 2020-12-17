#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>


const char* ssid = "yourSSID";    // fill in with your wifi network name
const char* password = "yourPASSWORD"; // fill in with you wifi network password
char servername[]="celestrak.com";

WiFiClient client;

//const char fingerprint[] PROGMEM = "3a ce 54 bc 41 42 e7 4f 54 60 c9 3c a9 e7 a8 71 1b 5a 5e 1c";
const int httpsPort = 80; //443 for HTTPS

void setup() {
  Serial.begin(9600);   // changing baud rate for serial monitor

  WiFi.begin(ssid,password);
  Serial.println("Connecting to wifi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("...");
  }

  makeHTTPSrequest();
}

void makeHTTPSrequest(){
  // Port number for HTTPS connection: 443
  // if you get a connection, report back via serial:
  if (client.connect(servername, 80)) {
  Serial.println("connected to server");
  Serial.println();
  Serial.print("TLE for: ");
  // Make HTTP request:
  client.println("GET /NORAD/elements/iridium-33-debris.txt HTTP/1.0");     // rest of url, i.e extension following celestrak.com
  client.println();                                                         // necessary to call on rest of server information
  }

char c;
int lineCounter=0;
while (!client.available()){
// while loop runs while waiting for server availability
}

// Skip HTTP headers
char endOfHeaders[] = "\r\n\r\n";
if (!client.find(endOfHeaders))
{
  Serial.println(F("Invalid response"));
  return;
}

// if there are incoming bytes available from the server, read them and print them:
while (client.available()) {
  c = client.read();
  Serial.print(c);

  if (c == '\n'){
    lineCounter = lineCounter+1;
    //Serial.print("Line count: ");
    //Serial.print(lineCounter);
  }

  if (lineCounter==3){
    client.stop();
    break;
  }
}

// if the server becomes disconnected, stop the client:
if (!client.connected()) {
  Serial.println();
  Serial.println("disconnecting from server");
  client.stop();
}
}

void loop() {
}
