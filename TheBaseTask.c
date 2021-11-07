#include <assert.h>
#include <ctype.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char a[100][100];
    int n,i,j,n1,k;
    char temp;
    int count=0;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
        scanf("%s",a[i]);   
        for(k=1;k<=n;k++)
    {
        n1=strlen(a[k]);
        for (i = 0; i < n1-1; i++) {
        for (j = i+1; j < n1; j++) {
         if (a[k][i] > a[k][j]) {
            temp = a[k][i];
            a[k][i] = a[k][j];
            a[k][j] = temp;
         }
      }
   }
    }
     for(k=1;k<=n;k++)
    {
            for(j=0;j<strlen(a[k]);j++)
            {
            if(a[k][j]!=a[k][j+1])
            count++;
            }
            printf("%d \n",count);
            count=0;
    }  
        
}
