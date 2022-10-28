class Selection:
    '''
      Selection Sort
      - In case of selection sort we repeatedly find the minimum element and move it to the sorted part of array to make unsorted part sorted
      It is unstable and in place alogithm
      Time O(N^2) Space O(1)
      we can make it space by moving the elements between min and index to left and placing the min at index

      When to use selection sort?
      - when we have insufficuent memory
      - Easy to implement
      when to avoid selection sort?
      - whwn time is a concern
    '''
    def sort(self,values,reverse=False):
        if not reverse:
            for i in range(len(values)):
                min_index = i
                for j in range(i+1,len(values)):
                    if values[min_index] > values[j]:
                        min_index = j
                values[i], values[min_index] = values[min_index], values[i]
        else:
            for i in range(len(values)):
                max_index = i
                for j in range(i+1,len(values)):
                    if values[max_index] < values[j]:
                        max_index = j
                values[i], values[max_index] = values[max_index], values[i]
    def stable(self, values,reverse=False):
        if not reverse:
            for i in range(len(values)):
                min_index = i
                for j in range(i+1,len(values)):
                    if values[min_index] > values[j]:
                        min_index = j
                val = values[min_index]
                while min_index > i:
                    values[min_index] = values[min_index - 1]
                    min_index -= 1
                values[i] = val
        else:
            for i in range(len(values)):
                max_index = i
                for j in range(i+1,len(values)):
                    if values[max_index] < values[j]:
                        max_index = j
                val = values[max_index]
                while max_index > i:
                    values[max_index] = values[max_index - 1]
                    max_index -= 1
                values[i] = val