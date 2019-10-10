#include <iostream>		// Include all needed libraries here
#include <wiringPi.h>

using namespace std;		// No need to keep using “std”
unsigned int prevTime;		// Temporary variable that holds the previous millis value

int main()
{
wiringPiSetup();			// Setup the library
pinMode(23, PWM_OUTPUT);		// Configure GPIO1 as an output for PWM
pinMode(25, OUTPUT)
// Main program loop
while(1)
{
	for(int i = 0; i < 512; i++)
	{
		pwmWrite(23, i);
		delay(1);
	}		
}
return 0;
}