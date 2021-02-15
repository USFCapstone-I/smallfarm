#include <Arduino.h>

#define PHPIN 13          // the pH meter Analog output is connected with the Arduino’s Analog
unsigned long int avgValue;  //Store the average value of the sensor feedback
int buf[10],holder;

void setup(){
  Serial.begin(115200);  
}
void loop(){
  for(int i=0;i<10;i++){       //Get 10 sample value from the sensor for smooth the value 
    buf[i]= analogRead(PHPIN);
    delay(10);
  }
  for(int i=0;i<9;i++){        //sort the analog from small to large
    for(int j=i+1;j<10;j++){
      if(buf[i]>buf[j]){
        holder=buf[i];
        buf[i]=buf[j];
        buf[j]=holder;
      }
    }
  }
  avgValue=0;
  
  for(int i = 2; i<8; i++){                      //take the average value of 6 center sample
    avgValue+=buf[i];
  }
  float phValue = (float)avgValue * 3.3/1023/6; //convert the analog into volt
  phValue = 3 + phValue;                      //convert the volt into pH value
  Serial.println("pH:" + String(phValue)); 
  Serial.println(" ");
}