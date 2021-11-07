import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args){
         Scanner in = new Scanner(System.in);
         int t = in.nextInt();
         while( t-- >0 )
         {
             int count = 0;
             String num = in.next();
             int[] numarray = new int[200];
             String number = String.valueOf(num);
             for( int i = 0; i < number.length(); i++ )
             {
                 char nu = number.charAt(i);
                 int nu_m = Character.getNumericValue(nu);
                 numarray[nu_m] += 1;
             }
             for( int j = 0; j < numarray.length; j++ )
             {
                 if( numarray[j] >= 1 )
                 {
                     count += 1;
                 }
             }
             if( count == 1 )
             {
                 System.out.println("2");
             }
             else
             {
              System.out.println( count );
             }
         }
       
}
}
