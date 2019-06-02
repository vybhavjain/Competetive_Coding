import java.util.Scanner;

public class ques2 {
	static int getfactors(int n,int num) {
		int count_num = 0;
		for(int i = 1; i <= Math.min(n,Math.sqrt(num)); i++ ) {
			if(num%i == 0) {
				int comp = num/i;
				if( comp <= n && comp != i ) {
					count_num += 2;
				}
				else {
				count_num +=1;
				}
			}
		}
		
		return count_num;
	}
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int[] ar = new int[n];
		for(int i = 0; i < n; i++ ) {
			ar[i] = in.nextInt();
		}
		int count = 0;
		for( int i = 0; i < ar.length; i++ ) {
			count += getfactors(n,ar[i]);
		}
		System.out.println(count);
	}

}
