// author : Ji Su - Kim
// date : 18.06.14

int trigPin = 5;
int echoPin = 10;
int speakerPin = 3;
  int count = 0;

void setup() 
{
  Serial.begin (9600);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(speakerPin, OUTPUT);
}

void loop() 
{
  long duration, distance;      // 시간, 거리      
  digitalWrite(trigPin,HIGH);        
  delay(10);
  digitalWrite(trigPin, LOW);


  
  duration = pulseIn(echoPin, HIGH);
  distance = ((float)(duration*340)/10000)/2;
  
  if (Serial.available() > 0)
     {  
      Serial.flush();  
      int cmd = Serial.read();
      if (cmd == 0) Serial.println(distance);
      else if (cmd == 1) { 
        digitalWrite(speakerPin, HIGH);
        delay(500);
        digitalWrite(speakerPin, LOW);
        
      } 
      else if (cmd == 2) { 
        digitalWrite(speakerPin, HIGH);
        delay(200);
        digitalWrite(speakerPin, LOW);
        delay(200);
        digitalWrite(speakerPin, HIGH);
        delay(200);
        digitalWrite(speakerPin, LOW);
      } 
      else if (cmd == 3) { 
        digitalWrite(speakerPin, HIGH);
        delay(200);
        digitalWrite(speakerPin, LOW);
        delay(200);
        
        digitalWrite(speakerPin, HIGH);
        delay(200);
        digitalWrite(speakerPin, LOW);
        delay(200);
        
        digitalWrite(speakerPin, HIGH);
        delay(200);
        digitalWrite(speakerPin, LOW);
      }
    } 
       
        
      
  delay(1000);
}

