class Solution:
	
	# Was able to find a simple version of the code online. (Still learning...)
	def longestPalin(self, s):
		# ^ and $ are sentinels appended to each end to avoid bounds. 
		T = '#'.join('^{}$'.format(s))

		n = len(T)
		P = [0] * n
		C = R = 0
		
		for i in range(1, n-1):

			# i - C is the mirror index value
			i_mirror = C - (i - C)

			if R > i:
				P[i] = min(R - i, P[i_mirror])			
			P[i] = 0

			while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
				P[i] += 1

			if i + P[i] > R:
				C = i
				R = i + P[i]

			print('Iteration:', '%2s' % i, P, '%10s' % i_mirror, '%10s' % C, '%10s' % R)
		return max(P)


c = Solution()
c.longestPalin("theracecaris") 