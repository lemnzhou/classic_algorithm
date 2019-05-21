'''This script is the algorithm about how to get the k largest item of an array quickly.You maybe 
sort the array first and then get the k largest item,but this method's time consuming is O(NlogN).
Using the Quick-Sort method without merge two subarray can find the k largest item with O(N) time 
consuming.'''

import numpy as np 

class findKlargest():
    def __init__(self,array,k):
        self.array = array
        if k>len(array):
            self.k=len(array)
        else:
            self.k=k
    
    def find(self,st,en,k):
        m = self.array[st]
        if(st==en):
            return m
        i,j = st+1,en
        #print(i,m)
        while(i<j):
            while(i<j and self.array[i]<=m):
                i = i+1
            while(j>i and self.array[j]>m):
                j = j-1
            tmp = self.array[i]
            self.array[i] = self.array[j]
            self.array[j] = tmp
        if self.array[i]<=m:    #the last i position is smaller than m,swap them
            self.array[st] = self.array[i]
            self.array[i] = m   
        else:                  #the last i positon is larger than m,then swap array[i-1] and array[st]
            self.array[st] = self.array[i-1]
            self.array[i-1] = m
            i = i-1
        t = en - i +1 ####item m is the t largest item of array[st,en],in the position array[i]
        if t==k:
            return m
        elif t > k:
            return self.find(i+1,en,k)  ###find the k largest in the larger part when t is larger than k.
        else:
            return self.find(st,i-1,k-t)  ###find the k-t largest in the smaller part when t is smaller than k.
        
    def getKlargest(self):
        m = self.find(0,len(self.array)-1,self.k)
        return m


if __name__ == '__main__':
    array = np.array([0,3,1,1,4,2,10,7,5,11,13,0,9])
    for i in range(1,len(array)+1):
        method = findKlargest(array,i)
        m = method.getKlargest()
        print('the ',i,' largest item of array is :',m)

###the output:
# the  1  largest item of array is : 13
# the  2  largest item of array is : 11
# the  3  largest item of array is : 10
# the  4  largest item of array is : 9
# the  5  largest item of array is : 7
# the  6  largest item of array is : 5
# the  7  largest item of array is : 4
# the  8  largest item of array is : 3
# the  9  largest item of array is : 2
# the  10  largest item of array is : 1
# the  11  largest item of array is : 1
# the  12  largest item of array is : 0
# the  13  largest item of array is : 0