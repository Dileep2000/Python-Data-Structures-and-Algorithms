class Insertion:
    '''
      Insertion sort
      - Divide the given array into two parts
      - Take first element from unsorted array and fund its correct position in sorted array
      - Repeat untill unsorted array is empty
      Time O(n^2) Space O(1)
      It is in place and stable algorithm

      when to use insertion sort?
      - when we have insufficient memory
      - Easy to implement
      - when we have contiguous inflow of numbers and we want to keep them sorted
      when to avoidd insertion sort
      - when time is a concern
      
    '''
    def sort(self,values,reverse=False):
        if not reverse:
            for i in range(1,len(values)):
                val = values[i]
                j = i-1
                while j >= 0 and val < values[j]:
                    values[j+1] = values[j]
                    j -= 1
                values[j+1] = val
        else:
            for i in range(1,len(values)):
                val = values[i]
                j = i-1
                while j >= 0 and val > values[j]:
                    values[j+1] = values[j]
                    j -= 1
                values[j+1] = val