#include<stdio.h>
#include<ctype.h>

int main(void) {
    int c;
    c=getchar();
    if(isalnum(c)!=0 && isdigit(c)!=0)
          printf("Bu bir say�d�r\n");
              
    else
          printf("Bu bir karekter dizisidir\n");
          
       
         
    getch();
}
    
