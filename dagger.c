#include<stdio.h>

void main()

{
	int a[100];
	int n,i ,sum,j,k;
	scanf("%d",&n);
	printf("Enter the array content /n ");
	for (i = 0 ; i <n ; i++)
	{
		scanf("%d",&a[i]);
	}
	printf("0");
	for( j= 1 ; j<n ;j++)
	{
	 sum = 0;
	 k = j;
	 while(k!=0)
	 {
 		sum = sum + a[j]-a[k-1];
 		k--;
 	 }
 	printf("%d",sum);
}}
