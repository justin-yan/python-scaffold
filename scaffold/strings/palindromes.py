def isPalindrome(s):
    return s == s[::-1]

# https://leetcode.com/problems/longest-palindromic-substring/
def longestPalindrome(s: str) -> str:
    # The brute-force solution would be to do the N^2 check of every starting index vs. every ending index
    # curmax = 0
    # string = None
    # strlen = len(s)
    # for start in range(strlen):
    #     for end in range(start + 1, strlen + 1):
    #         if isPalindrome(s[start:end]) and end-start > curmax:
    #             curmax = end-start
    #             string = s[start:end]
    # return string

    # The problem is with the palindrome check, which causes this to become N^3 overall.
    # The redundancy in the problem lies mostly with the palincheck, which we can reduce to constant time
    x = y = len(s)
    isPali = [[False for i in range(y)] for j in range(x)]

    curmax = ""
    for i in range(x):
        isPali[i][i] = True
        curmax = s[i]
    for i in range(x - 1):
        if s[i] == s[i+1]:
            isPali[i][i+1] = True
            curmax = s[i:i+2]

    # There are two ways you can iterate through.
    # You can iterate by distance, or, because the DP check decreases your end index by 1, you can iterate by your end index first
    # for palilen in range(3, x + 1):
    #     for start in range(x + 1 - palilen):
    #         end = start + palilen - 1
    #         if s[start] == s[end] and isPali[start+1][end-1]:
    #             isPali[start][end] = True
    #             curmax = s[start:end + 1]
    # return curmax

    for end in range(x):
        for start in range(end):
            if s[start] == s[end] and isPali[start+1][end-1]:
                isPali[start][end] = True
                if end - start + 1 > len(curmax):
                    curmax = s[start:end + 1]
    return curmax