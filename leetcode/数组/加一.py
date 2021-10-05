class Solution(object):
    def plusOne(digits):
        n=len(digits)
        for i in range(1,n+1):
            if digits[n-i]==9:
                digits[n-i]=0
            else:
                digits[n-i]+=1
                break
            if digits[0]==0:
                digits.insert(0,1)
        return digits

    digit=[9,9]
    plusOne(digit)
