class bubble:
    '''
      Bubble Sort
      - Bubble sort is also reffered as Sinking sort
      -we repeatedly compare each pair of adjacent items and swap them if they are in wrong order
      Time O(N^2) Space O(1)
      When to use bubble sort?
      - when the input is already sorted
      - space is concern
      - easy to implement
      when to avoid bubble sort?
      - Average time complexity is poor

      Is is an in place ans stable type algorithm
    '''
    def sort(self,values,reverse=False):
        if reverse:
            for i in range(len(values)-1):
                for j in range(len(values)-i-1):
                    if values[j] < values[j+1]:
                        values[j], values[j+1] = values[j+1], values[j]
        else:
            for i in range(len(values)-1):
                for j in range(len(values)-i-1):
                    if values[j] > values[j+1]:
                        values[j], values[j+1] = values[j+1], values[j]
    def optimized(self, values,reverse = False):
        if reverse:
            swap = False
            for i in range(len(values)-1):
                for j in range(len(values)-i-1):
                    if values[j] < values[j+1]:
                        values[j], values[j+1] = values[j+1], values[j]
                        swap = True
                if not swap:
                    break
        else:
            swap = False
            for i in range(len(values)-1):
                for j in range(len(values)-i-1):
                    if values[j] > values[j+1]:
                        values[j], values[j+1] = values[j+1], values[j]
                        swap = True
                if not swap:
                    break
    def recursive(self, values,n=None):
        if n is None:
            n = len(values)
        if n == 1: return
        swap = False
        for j in range(n-1):
            if values[j] > values[j+1]:
                values[j], values[j+1] = values[j+1], values[j]
                swap = True
        if not swap:
            return
        self.recursive(values,n-1)