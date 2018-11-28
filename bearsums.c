#include <stdio.h>
#include <stdlib.h>

// not complete solution 

int main() {
    int i,n,j,k;
    int sum[10],number_elements[10];
    int arr[10];
    int flag = 0;
    int flag1 = 0;
    scanf("%d ", &n);
    for(i = 0 ;i < n ;i++)
    {
     //   printf("this is the %d try",i);
     scanf("%d", &sum[i]);
     scanf("%d", &number_elements[i]);
     for(j = 0 ; j < number_elements[i] ;j++)
       scanf("%d",&arr[j]);
     for(j = 0 ; j < number_elements[i]  ;j++)
      {
          flag = 0 ;
          for(k = 0 ; k < number_elements[i] ; k++)
            {
                int check = 111111 ; 
                if(j!=k)
                {
                    check = arr[j] + arr[k];
                }
                if (check == sum[i])
                {
                    if (arr[j] < arr[k])
                     printf("%d %d \n",arr[j],arr[k]);
                    else
                    printf("%d %d \n",arr[k],arr[j]);
                    flag = 1 ;
                    flag1 = 1;
                    break;
                }
            }
            if (flag1 == 1)
            {
            flag1=0;
            break;
            }
            }
      if(flag == 0)
                printf("!OK \n");
    }
    return 0;
}
