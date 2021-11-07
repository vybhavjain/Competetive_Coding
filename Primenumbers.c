#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int a[100][100];


int prime(int num1)
{
    int num, j, flag;
    num=num1;
    if(num == 2)
        return 1;
    if (num <= 1)
    {
        printf("%d is not a prime numbers \n", num);
    }
    flag = 0;
    for (j = 2; j <= num / 2; j++)
    {
        if ((num % j) == 0)
        {
            flag = 1;
            break;
        }
    }
    if (flag == 0)
        return 1;
     else
        return 0;
}


int main() {
    int n,i,j;
    int count=0;
    int num1=0;
    scanf("%d",&n);
    for(i=0;i<=0;i++)
        for(j=0;j<=n;j++)
            a[i][j]=0;
    for(j=0;j<=0;j++)
        for(i=0;i<=0;i++)
            a[i][j]=0;
    for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
            scanf("%d",&a[i][j]);
    for(i=1;i<=n;i++)
        for(j=1;j<=n;j++)
        {
            num1= a[i-1][j]+ a[i+1][j]+ a[i][j+1]+ a[i][j-1];
            int flag=prime(num1);
            if(flag==1)
                count++;
        }
    printf("%d",count);
    return 0;
}
