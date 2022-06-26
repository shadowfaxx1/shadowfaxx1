#include<stdio.h>
#include<stdlib.h>

int main()
{
     int ar[5]={3,5,4,2,1};
       int n=sizeof(ar)/sizeof(ar[0]);
       printf("%d",n);

       int i ,j ;

     for( i=0;i<n-1;i++)
     {
         int m=ar[i];

         for( j=i;j<n;j++)
         {
              
           if(ar[m]>ar[j])
              m=j;
            //  printf("m=%d",m);


         }
         int temp=ar[m];
         ar[m]=ar[i];
         ar[i]=temp;
      // printf("t=%d",temp);


     }

     for( i=0;i<n;i++)
     printf("%d",ar[i]);
     
}