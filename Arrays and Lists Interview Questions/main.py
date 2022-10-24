class Interview:
    '''
    Question 1: Missing Number
    How to find the missing number in an integer array of 1 to 100?
    sum of n number = n*(n+1)/2 Time - O(n) space - O(1)
    Question 2: write a program to find all pairs of integer whose sum is equal to a given number?
    Question 3: How to check if an array contains a number in python?
    Question 4: Find max product of integers in an array.
    Question 5: Implement an algorithm to determine if a list has all unique characters using python list.
    Question 6: Permutations
    Question 7: Given an image represented by an N*N matrix write a program to rotate the image by 90 degrees
    '''
    def __init__(self):
        pass
    def missingNumber(self,lis,n):
        sum = n*(n+1)/2
        lis_sum = sum(lis)
        return sum - lis_sum
    def sumPairs(self,lis,n):
        lis.sort()
        high = len(lis) - 1
        low = 0
        while high>low and low < len(lis) and high > 0:
            if lis[high]+lis[low] == n:
                if(lis[high] != lis[low]):
                    print(lis[high],lis[low])
                low += 1
                high -= 1
            elif lis[high]+lis[low] > n:
                high -= 1
            elif lis[high]+lis[low] < n:
                low += 1
    def doesExist(self,lis,n):
        for i in range(len(lis)):
            if lis[i] == n:
                return True
        return False
    def findMaxProduct(self,lis):
        assert len(lis) >= 2, "array must contain at least 2 elements to get max product"
        lis.sort()
        max1 = lis[0]*lis[1]
        max2 = lis[-1]*lis[-2]
        return max(max1,max2)
    def isUnique(self,lis):
        if len(lis) == 1:
            return True
        elif len(set(lis)) == len(lis):
            return True
        else:
            return False
    def isPermutation(self,str1,str2):
        if len(str1)!= len(str2):
            return False
        else:
            if str1.sort() == str2.sort():
                return True
            else:
                return False
    

if __name__ == '__main__':
    interview = Interview()
    interview.sumPairs([3,2,4],6)