/* Libraries */
#include <iostream>
#include <pigpio.h>
// g++ -Wall -pthread -o pwmBlinky pwmBlinky.cpp -lpigpio -lrt

/* Variables and Constants */
using namespace std;
#define LED 16
#define HIGH 225
#define HALF 128
#define OFF 0
/* Main function */

int main(void)
{
    cout << "Raspberry Pi initialized!" << endl;
    if (gpioInitialise() < 0) exit(1);

    gpioSetMode(LED, PI_OUTPUT); // 3.3V PIN

    for (;;)
    {
        gpioPWM(LED, 255);
        gpioDelay(5000);  //In MicroSeconds 
        gpioPWM(LED, 128);
        gpioDelay(5000);
    }

    gpioTerminate();

}
