#include "HX711.h"
#define DOUT  4
#define CLK  5
 
HX711 scale(DOUT, CLK);
 
float calibration_factor = 12.4; //=100g
float output;
int readIndex;
float total=0;
float average=0;
float average_last=0;
const int cycles=20;
float readings[cycles];
 
void setup() {
     Serial.begin(57600);

     scale.set_scale();
     scale.tare();     //Reset the scale to 0
     
     long zero_factor = scale.read_average(); //Get a baseline reading
 
}
 
void loop() {
 
     scale.set_scale(calibration_factor); //Adjust to this calibration factor
     
     
     output=scale.get_units(), 2;
   
     
     total = total - readings[readIndex];
     readings[readIndex] = scale.get_units(), 2;
     total = total + readings[readIndex];
     readIndex = readIndex + 1;
     
     if (readIndex >= cycles) {
          readIndex = 0;
     }
     average = total / cycles;
     
     average=scale.get_units(), 2;
     
     
     if((average_last>average+0.03 || average_last<average-0.03)){
          if (average<0.06) {
               average=0;
          } 
          Serial.println((float)(average / 1000), 2);
          average_last=average;
     }
     else{
          Serial.println((float)(average / 1000), 2);
     }
     delay(500);
   

}
