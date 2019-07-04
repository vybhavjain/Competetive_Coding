class Solution:
	# @param A : string
	# @param B : tuple of strings
	# @return a list of integers
	def findSubstring(self, A, B):
	    total_length = len(B) * len(B[0])
        len_sub = len(B[0])
	    start = []
	    for i in range(0,len(A) - total_length + 1):
	        s2 = A[i:i+total_length]
            flag = 0
	        for k in range(len(B)):
	            s3 = B[k]
	            if s3 not in s2 :
                    flag = 1
	                break
	        if flag == 0:
	                if i not in start:
	                    start.append(i)
        return start
