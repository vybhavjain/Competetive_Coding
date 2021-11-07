#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char str[100][100];
    int i,j,n,k,n1;
    int count=0;
    char temp;
    int count1[10];
    scanf("%d", &n);
    for(i=0; i< n ; i++) {
        scanf("%s",str[i]);
    }
    
    for(k=0;k<n;k++)
    {
        n1=strlen(str[k]);
        for (i = 0; i < n1-1; i++) {
        for (j = i+1; j < n1; j++) {
         if (str[k][i] > str[k][j]) {
            temp = str[k][i];
            str[k][i] = str[k][j];
            str[k][j] = temp;
         }
      }
   }
    }
        
        for (i = 0; i < n; i++) 
        {
            count=0;
        for (j = 0; j < n; j++) 
        {
            if (strcmp(str[i],str[j]) == 0)
              count++;
        }
            count=(count);
            count1[i]=count;
        }
       int max = count1[0];
 
    for (  int c = 0 ; c <i ; c++ ) 
    {
        if ( count1[c] >= max ) 
        {
           max = count1[c];
        }
    } 

    printf("%d",max);
}
