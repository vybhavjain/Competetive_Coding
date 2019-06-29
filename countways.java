import java.util.*;
class TestClass {
    public static void main(String args[] ) throws Exception {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int m = in.nextInt();
        int[] ar = new int[m];
        for( int i = 0; i < m; i++ ){
            ar[i] = in.nextInt();
        }
        int count = 0;
        for( int j = 0; j < ar.length-1; j++ ){
             if( (n%ar[j]) == 0 ){
                 count += 1;
             }
            for( int k = j+1; k < ar.length; k++ ){
                  if( (ar[j] + ar[k]) == n ){
                      count += 1;
                  }
                  if( ar[j] + ar[k] < n ){
                      int sum = ar[j] + ar[k] + ar[k];
                      int sum1 = ar[j] + ar[j] + ar[k];
                    inner:while( sum <= n || sum1 <= n){
                          if( sum == n ){
                              count += 1;
                              break inner;
                          }
                          else if( sum1 == n ){
                              count += 1;
                              break inner;
                          }
                          else{
                              
                              sum += ar[k];
                              sum1 += ar[j];
                          }
                      }
                  }
            }
        }
        if( (n%ar[m-1]) == 0 ){
            count += 1;
        }
        System.out.println(count);
    }
}
