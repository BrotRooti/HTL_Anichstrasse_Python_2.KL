#include <kipr/wombat.h>

void rotate(){
	mav(0,-1500);
    mav(2,-1485);
    msleep(400);
    mav(0,1500);
    msleep(450);
    ao();
}

int main()

{
    while (digital(0) == 0){
    msleep(20);
    }
    		for (;;){
    		while  (analog(5)<2600){
    		msleep(50);
            mav(0,1500);
    		mav(2,1485);
            if (analog(0) < 100){
             	return 0;	}
    		}
    
    		ao();
    		rotate();
            } 
    
    return 0;
}

