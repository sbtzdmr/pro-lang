#include<stdio.h>
#include<string.h>

int main(void) {
    char c[10];
    int k=0,m=0;
    gets(c); /* kalvyeden grilen karekter dizilerini oku */
    while(c[k]!='\0'){ /* sonland�r�c� karektere kadar karekterleri say*/
             k++;  
             if (c[k] == 32) 
                   m++;  
                   }    
           printf("kelime say�s�: %d", (m+1)); /* bo�luk say�s�ndan bir fazlas�n� yaz */
           printf("karekter say�s�: %d", (k));
        getch();

}
