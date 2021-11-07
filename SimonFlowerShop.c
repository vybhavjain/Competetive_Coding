#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int n,a,b,x,y;
    int i=0;
    int cost[1000000];
    scanf("%d",&n);
    scanf("%d",&a);
    scanf("%d",&b);
    x=n;
    y=0;
    while(x!= -1)
    {    
        cost[i++]= a*x*x + b*y*y;
        x=x-1;
        y=y+1;
    }       

    int minimum = cost[0];
 
    for (  int c = 0 ; c <i ; c++ ) 
    {
        if ( cost[c] <= minimum ) 
        {
           minimum = cost[c];
        }
    } 

    printf("%d",minimum);
}
