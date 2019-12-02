#include <WiFi.h>
#include <WebServer.h>

/*Put your SSID & Password*/
const char* ssid = "**********";  // Enter YOUR SSID here
const char* password = "*********";  //Enter YOUR Password here
WebServer server(80);
uint8_t led = 2;
bool ledstatus = LOW;

uint8_t m1c1pin = 16;
bool m1c1status = LOW;

uint8_t m1c2pin = 17;
bool m1c2status = LOW;

uint8_t m2c1pin = 18;
bool m2c1status = LOW;

uint8_t m2c2pin = 19;
bool m2c2status = LOW;

bool leftstatus   = LOW;
bool rightstatus  = LOW;
bool centerstatus = LOW;
bool searchstatus = LOW;
  




void setup() {
  Serial.begin(115200);
  delay(100);
  pinMode(m1c1pin, OUTPUT);
  pinMode(m1c2pin, OUTPUT);
  pinMode(m2c1pin, OUTPUT);
  pinMode(m2c2pin, OUTPUT);
  
  Serial.println("Connecting to ");
  Serial.println(ssid);

  //connect to your local wi-fi network
  WiFi.begin(ssid, password);

  //check wi-fi is connected to wi-fi network
  while (WiFi.status() != WL_CONNECTED) {
  delay(1000);
  Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected..!");
  Serial.print("Got IP: ");  Serial.println(WiFi.localIP());

  server.on("/", handle_OnConnect);
  server.on("/left", handle_left);
  server.on("/right", handle_right);
  server.on("/center", handle_center);
  server.on("/search", handle_search);
  // server.on("/stop", handle_search);
  server.onNotFound(handle_NotFound);

  server.begin();
  Serial.println("HTTP server started");
}
void loop() {
  server.handleClient();
  if(leftstatus)
  {
 
  
  Serial.println("LEFT");
  
  digitalWrite(m1c1pin,LOW);
  digitalWrite(m1c2pin,LOW);
  digitalWrite(m2c1pin,HIGH);
  digitalWrite(m2c2pin,LOW);
  delay(200);
  digitalWrite(m2c1pin,LOW);
  digitalWrite(m2c2pin,LOW);  
  leftstatus=LOW;
  }
   if(rightstatus)
  {

  
  Serial.println("RIGHT");
  
  digitalWrite(m1c1pin,HIGH);
  digitalWrite(m1c2pin,LOW);
  digitalWrite(m2c1pin,LOW);
  digitalWrite(m2c2pin,LOW);
  delay(200);
  digitalWrite(m1c1pin,LOW);
  digitalWrite(m1c2pin,LOW);  
  rightstatus=LOW;
  }
   if(centerstatus)
  {

  
  Serial.println("CENTER");
  
  digitalWrite(m1c1pin,LOW);
  digitalWrite(m1c2pin,LOW);
  digitalWrite(m2c1pin,LOW);
  digitalWrite(m2c2pin,LOW);
  centerstatus=LOW;
  }
   if(searchstatus)
  {

  
  Serial.println("SEARCH");
  
  digitalWrite(m1c1pin,LOW);
  digitalWrite(m1c2pin,LOW);
  digitalWrite(m2c1pin,HIGH);
  digitalWrite(m2c2pin,LOW);
  delay(500);
  digitalWrite(m2c1pin,LOW);
  digitalWrite(m2c2pin,LOW);  
  searchstatus=LOW;
  }
 
}

void handle_OnConnect() {

digitalWrite(led, HIGH);
}

void handle_left() {
  leftstatus = HIGH;
 
}

void handle_right() {
  rightstatus=HIGH;


}

void handle_center() {
  centerstatus=HIGH;


}

void handle_search() {
  searchstatus = HIGH;

   
}

void handle_NotFound(){
 
  Serial.println("ERROR");
  
}
