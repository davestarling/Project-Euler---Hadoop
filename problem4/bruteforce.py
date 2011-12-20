"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers."""

def is_palindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    return False

maxnum = 1000
palindromes = []

for i in reversed(xrange(1, maxnum)):
    for j in reversed(xrange(1, maxnum)):
        if is_palindrome(i*j):
            palindromes.append(i*j)
            print '{} x {} = {}'.format(i, j, i*j)

print 'Maximum palindrome is {}'.format(max(palindromes))