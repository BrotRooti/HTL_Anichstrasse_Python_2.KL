#include <kipr/wombat.h>
void check (){
    while  (analog(0)<2600){
    motor(0,93.97);
    motor(2,100);
    }
    
    ao();
}
void rotate(){
	motor(0,-93.97);
    motor(2,-100);
    msleep(200);
    motor(0,93.97);
    msleep(450);
    ao();
}

int main()

{
    
    while (digital(0) == 0){
    check();
    rotate();
    }    
    
    return 0;
}
