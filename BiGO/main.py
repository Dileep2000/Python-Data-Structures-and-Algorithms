class BigO:
    """
      Big O is the language and metric we use to describe the efficiency of algorithms.
      Algorithm can perfrom diffrently based on the conditions given
      Three scenarios in case of mesuring of algorithms
      - Best case
      - Average case
      - Worst case
      Notations
      Big O : It is a complexity that is going to be less or equal to the worst case.
      Big- Omega : It is a complexity that is going to be at least more than the best case.
      Big Theta: It is a complexity that is within the bounds of the worst case and the best case.
      Big O - O(N)
      Big Omega : Omega(1)
      Big Theta : Theta(n/2)

      Time Complexity examples
      O(1) Constant Accessing an specific element in array
      O(N) Linear time complexity Loop through array elements
      O(LogN) Logrithmic  Find an element in sorted array
      O(N^2) Quadratic Looking for every index in the array twice.
      O(2^N) Exponential Dubole recursion in fibonacci
      
      Sapce Complexity
      Array size of n - O(N)

      Dropping constants and Non Dominant terms in Big O
      O(2N) -> O(N)
      O(N^2+N) -> O(N^2)
      - It is very pissble that O(N) code is frater than O(1) code for specific inputs
      - Different computers with different architectures have different constant factors
      - Different algorithms with the same basic idea and computational complexity might have slightly different constants
      - As n approches infinity constant factores are not really a big deal
      Add VS Multiply
      IF two individual loops then add the Runtimes. If two loops are like do this for each then multiply.
      How to measure the codes using Big O?
      Set of Rules:
      Rule 1 Any assignment statements and if statements that are executed once regqrdless og the size of the problem O(1)
      Rule 2 A sample for loop from 0 to n (with no internal loops) O(n)
      Rule 3 A nested loop of the same type takes Quadratic time complexity O(n^2)
      Rule 4 A loop in which controlling parameters is divided by two at each step )(log n)
      Rule 5 when dealing with multiple statements just add them up
      How to measure Recursive algorithms
      Top 10 Big O Interview Questions
      problem 1: product and sum
      problem 2: print pairs
      problem 3: Print Unordered pairs
      problem 4: Print Unordered pairs 2 arrays
      problem 5: Print Unordered pairs 2 arrays 100000 units
      problem 6: Reverse
      problem 7: factorial O(n)
      problem 8: fibonacci O(log n)
    """
    def findMaxRecur(self,arr,n):
        if n == 1:
            return arr[0]
        else:
            return max(arr[n-1],self.findMaxRecur(arr,n-1))
    def problem1(self,arr):
        sum = 0
        product = 1
        for i in arr:
            sum+=i
        for i in arr:
            product *= i
        print("The time complexity of above the problem is O(n)")
    def problem2(self,arr):
        for i in arr:
            for j in arr:
                print('(',i,',',j,')')
        print("The time complexity of above problem is O(n^2) Quadratic")
    def problem3(self,arr):
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                print('(',i,',',j,')')
        print("The time complexity of above problem is O(n^2) Quadratic")
    def problem4(self,arr,arr1):
        for i in range(0,len(arr)):
            for j in range(0,len(arr1)):
                if arr[i] < arr[j]:
                    print('(',i,',',j,')')
        print("The time complexity of above problem is O(len(arr)*len(arr1))")
    def problem5(self,arr,arr1):
        for i in range(0,len(arr)):
            for j in range(0,len(arr1)):
                for k in range(0,100000):
                    print('(',i,',',j,')')
        print("The time complexity of above problem is O(len(arr)*len(arr1))")
    def problem6(self,arr):
        for i in range(0,int(len(arr)/2)):
            other = len(arr)-i-1
            temp = arr[i]
            arr[i]=arr[other]
            arr[other]=temp
        print(arr)
        print("The time complexity of above problem is O(len(arr))")
    
if __name__ == '__main__':
    bigO = BigO()
    print(bigO.__doc__)
    print(bigO.findMaxRecur([1,2,3],3))