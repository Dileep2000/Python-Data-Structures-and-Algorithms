class Hashing:
    '''
      What is hashing?
      Why we need it?
      Hash functions
      Collision resultion techniquw
      Hash tables
      practical use of hashing

      What is hashing?
      Hashing is a method of sorting and indexing data. The idea behind hashing is to allow large amount of data to be indexed using keys commonly created by formulas
                        magic function
      Apple                             18
      Applications                      20
      Appmillers                        22

      why hasing?
      It is time efficient case of searrch operation
      Data structure   Time complexit for search
      Array/Python list   O(logn)
      linked list         O(n)
      tree                O(logn)
      hashing             O(1) / O(n)

      Hashing Terminology
      Hash function - It is a function that can be used to map a arbitary size to data of fixed size
      Key: Input data by a user
      Hash value - A value that is returned by the hashing function
      Hash table - It is a data structure which implements an associtaive array abstract data type, a strucre that can map keys and values
      Collision - A collicsion occurs when two diffrent keys to a hashfunction produces same output
      
      Hash Functions
       Mod Function
       def mod(number,cellNumber):
        return number%cellNumber
       ASCII function
       def modAscii(string,cellNumber):
        total = 0
        for i in string:
            total += ord(i)
        return total%cellNumber
      
      Properties of goot hash function
      - It distributes hash values uniformly across hash tables
      - It has to use all input data

      Collision resolution techniques
      Direct Chaining
      Open Addressing
       - Linear Probing
       - Quadratic Probing
       - Double hashing
      Direct Chaining - implements the buckets as linked list. Coliding elements are soted in lists
      open addressing - colliding elements are stored in other vacant buckets. During storage and lookup these are found through so called probing
      Linear probing - It pleaces new key into closest following empty cell
      Quadratic probing - Adding arbitary quadratic polynomial to the index untill an empty cell is found
      Double hasing - Interval between probles is complutef by another hash function

      hash table is full
      Direct chaining - This situatuion never arise
      openaddressing - create 2x size of current hash table and recall hashing for current keys
      pros and cons of collision resolution techniques
      Direct chaining - 
      - Hash table never gets full
      - Higher linked list causes performance leaks(The time complexity of search operation becomes O(n)).
      open addressing
      - Easy implementation
      - when hash table is full, creation of new hash table affexts performance (Time complexity for search operation becomes O(n)).

      If input size is known we always use open addressing
      If we perform deletion operartion more frequently we use "Direct chaining"

      Practical use of Hasing
      - password verification
      - File system 0 File path is mapped to physical location on disk

      Pros and cons of hasing
      On average insertion/Deletion/Search operations take O(1) time.
      when hash function is not not good enough insertion/deletion/search operation take O(n) time
    '''
if __name__ == '__main__':
    hash = Hashing()
    print(hash.__doc__)