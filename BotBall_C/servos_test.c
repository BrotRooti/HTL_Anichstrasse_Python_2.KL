#include <kipr/wombat.h>




int main()

{
    
    //while  (analog(5)<2600){
    //motor(0,93.97);
    //motor(2,100);
    //}
    //ao();    
    enable_servos();
    set_servo_position(0,0);
    set_servo_position(1,1000);
    
    
    msleep(500);
    set_servo_position(0,900);
    msleep(1000);
    set_servo_position(1,0);
    msleep(2000);
    set_servo_position(1,1000);
    set_servo_position(0,0);
    
    return 0;
}



