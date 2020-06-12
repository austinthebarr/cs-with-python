 #include <stdio.h>

 
    int main (void) {
       int t = 0;
       for (int i = 0; i <= 10; i++) {
          t++;
          for(int j = 0; j <= t; j++) {   
             if(j == t) {
                printf("#");
             }
             printf("#");
          }
          printf("\n");
       }
    }
