#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <wiringPi.h>
int main (void)
{
	int i = 0;
	if (wiringPiSetup () == -1)
		exit (1) ;
	//printf ("Success\n") ;
	pinMode (0, OUTPUT) ;
	pinMode (1, PWM_OUTPUT) ;
	for (i = 0; i < 1; i++)
	{
		digitalWrite (0, LOW) ;
		pwmWrite (1, 1023) ;
		delay (500);

		digitalWrite (0, LOW) ;
		pwmWrite (1, 0) ;
		delay (500);
	}
	return 0 ;
}