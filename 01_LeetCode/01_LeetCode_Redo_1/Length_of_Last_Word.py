"""
"Hello World"
"a"
""
"ks llllllllllllll"
"@#!@ 452'"
" "
" @"
" $ "
"""

# I think the main thin I am getting out of this, I need to make sure what test cases are going to be. 
# So you need to ask the right questions. Or else you cannot solve the problem sucessfully. 
class prob_58:
	# Low level no functions
	def lengthfLastWord_2(self, s:str) -> int:
		# Edge cases
        if not s:
            return 0
        if s == " ":
            return 0
        if len(s) == 1:
            return 1
        
        length = len(s) - 1
        while length >= 0:
            if s[length] == " ":
                return len(s[length+1:])
            length -= 1
        return len(s)

    # High level using Python split
    def lengthOfLastWord_1(self, s: str) -> int:
        # Edge cases
        if s == "":
            return 0
        
        # Main logic
        s = s.split(" ")
        length = len(s)-1
        while length >= 0:
            if s[length]:
                return len(s[length])
            length -= 1
        return 0
