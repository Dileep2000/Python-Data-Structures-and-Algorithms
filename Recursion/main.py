from math import factorial
from re import A


class recursion:
    '''
      What is recursion?
      It is a way of solving a problem by having a function calling itself.
      Properties of recursion
      - Perfroming the same operation multiple times with different inputs
      - In every strp we try smaller inputs to male the problem smaller
      - Base condtion is needed to stop the recursion, other wise infinite loop will occur.
      Why recursion?
      1. Recursuce thinking is realy important in programming and it helps you break down big problems into smallerr ones and easier to use
      When to choose recursion
      - If you can divine the problem into similar sub problems
      - Design an alogrithm to compute nth...
      - write code to list the n....
      - Implement a method ti cpmoute all
      - practive
      2. The prominent usage of recursion in data structures like trees and graphs
      3. It is used in many algorithms(DAC,Greedy and DP)
      How recursion works
      1. A method calls it self
      2. Exit from infinite loop

      def recursionMethod(parameters):
        if exit from condition satisfied:
            return some value
        else:
            recursionMethod(modified parameters)
                        Recursive VS Itterative Method
      space efficient?  No              Yes            (No stack memory is require in case of itteraion)
      Time efficient?   No              Yes            (In case if recursion system needs more time for pop and push elements to stack memory which makes recursion less time efficient)
      Easy to code?     Yes             No             (We use recursion especially in the cases we know that a propem can be divided into simlar sub problems)
      
      When  to use/Avoid recursion?
        when to use it?
        - when we can easily break down a problem into similar subproblems.
        - when we are fine with extra overhead (both time and space) that comes with it.
        - when we need a quick working solution insted of efficeient one
        - when traverse a tee
        - when we use memoization in recursion
        When we can avoid recursion?
        - If time and space complexity matters for us
        - Recusion uses more memory. If we use embedded memory. For example an application that takes more memory in the phone is not efficient.
        - Recursion can be slow
      How to write recusion in 3 steps?
      Factorial - Product of all positive integers less than or equal to n. Denoted by n!. Only positive numbers. 0! = 1.
      Step 1: Recursive Case - the flow
      n! = n*(n-1)*(n-2)*(n-3)*.....*2*1
      n! = n*(n-1)!
      Step 2: Base casr - the stopping criterion
      0! = 1
      1! = 1
      Srep3: Unintentional case - the constraint
      n>0

      Fibonacci numbers - Recursion
      Fibonacci sequence is a sequence of numbers in which each number is sum of two preceding ones and sequence start with 0 and 1
      0,1,1,2,3,5,8,13,21,34,55,89,....
      f(n) = f(n-1)+f(n-1)
      How to find the sum of digits of a +ve integer number using recursion?
      How to calculate power of number using recursion?
      How to find GCD(greatest common divisor) of two numbers using recursion?
      How to convert a number from decimal to Binary using recursion?
    '''
    def __init__(self):
        print("You have visited recursion")
        self.russian_doll(5)
    def russian_doll(self,doll_size):
        if doll_size == 1:
            print("All Dolls are opened")
        else:
            self.russian_doll(doll_size-1)
    def firstMethod(self):
        self.secondMethod()
        print("I am First Method")
    def secondMethod(self):
        self.thirdMethod()
        print("I am Second Method")
    def thirdMethod(self):
        self.fourthMethod()
        print("I am Third Method")
    def fourthMethod(self):
        print("I am Fourth Method")
    def recursiveMethod(self,n:int):
        if n < 1:
            print("n is less than 1")
        else:
            self.recursiveMethod(n-1)
            print(n)
    def powerOfTwo(self,n):
        if n == 0:
            return 1
        else:
            power = self.powerOfTwo(n-1)
            return power*2
    def powerOfTwoIt(self,n):
        i = 0
        power = 1
        while i < n:
            power = power*2
            i += 1
        return power
    def factorial(self,n):
        assert n>=0 and int(n) ==n, "The nunber must be positive integer only!"
        if n==0 or n==1:
            return 1
        return n*self.factorial(n-1)
    def fibonacci(self,n):
        assert n>=0 and int(n) ==n, "The nunber must be positive integer only!"
        if n in [0,1]:
            return n
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
    def sumdigit(self,n):
        assert n >=0 or int(n) == n, "The nunber must be positive integer only!"
        if n == 0:
            return 0
        else:
            return n%10 + self.sumdigit(n//10)
    def powerOfN(self,n,power):
        assert int(power) == power, "The exponent must be positive integer only!"
        if power == 0:
            return 1
        elif power < 0:
          return 1/n*self.powerOfN(n,power+1)
        return n*self.powerOfN(n,power-1)
    def gcd(self,num1,num2):
        assert int(num1) == num1 and int(num2) == num2, "The numbers must be integers"
        if num1 < 0:
            num1 = -1*num1
        if num2 < 0:
            num2 = -1*num2
        if num2 == 0:
            return num1
        else:
            return self.gcd(num2,num1%num2)
    def decimalToBinary(self,n):
        assert n >=0 or int(n) == n, "The nunber must be positive integer only!"
        if n == 0:
            return 0
        else:
            return n%2 + 10*self.decimalToBinary(n//2)
    
if __name__ == '__main__':
    recur_object = recursion()
    print(recur_object.__doc__)
    recur_object.firstMethod()
    recur_object.recursiveMethod(5)
    print(recur_object.factorial(10))
    print(recur_object.fibonacci(5))
    print(recur_object.sumdigit(112))
    print(recur_object.powerOfN(2,-2))
    print(recur_object.gcd(2,2))
    print(recur_object.decimalToBinary(13))