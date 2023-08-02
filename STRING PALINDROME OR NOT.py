def isPalindrome(s):
	return s == s[::-1]
s =input("enter the word :")
ans = isPalindrome(s)
if ans:
	print("Yes")
else:
	print("No")
