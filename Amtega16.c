/*
 * vaibhv.c
 *
 * Created: 11/2/2017 2:45:47 PM
 *  
 */ 


#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
	DDRC=0x00;
	DDRD=0xff;
	DDRA=0xff;
	MCUCSR|=(1<<JTD);
	MCUCSR|=(1<<JTD);
    while(1)
    {
       if(PINC==0x01)               // 1 //
	   {
           PORTD=0x01;
	      PORTA=0xF0;
	   }	   
	   else if(PINC==0x03)		//2//
	   {
		PORTD=0x03; 
		PORTA=0xE0;  
	   }
	   
	   else if(PINC==0x07)		//3//
	   {
	   	   PORTD=0x07;
	   	   PORTA=0xD0;
	   }	   
	   
	   else if(PINC==0x0F)		//4//
	   {
		   PORTD=0x0F;
		   PORTA=0xC0;
	   }		   
	   else if(PINC==0x1F)		//5//
	   {    
              PORTD=0x1F;
		   PORTA=0xB0;
	   }		   
	   else if(PINC==0x3F)		//6//
	   {
		   PORTD=0x3F;
		   PORTA=0xA0;
	   }	
	   else if(PINC==0x7F)		//7//
	   {
		   PORTD=0x7F;
		   PORTA=0x90;
	   }
	   
	   else if(PINC==0xFF)		//8//
	   {
		   PORTD=0xFF;
		   PORTA=0x80;	   
	   }	   
		else
	   {
		   PORTD=0x00;
		   PORTA=0x00;
	   }	    
        }
        }
