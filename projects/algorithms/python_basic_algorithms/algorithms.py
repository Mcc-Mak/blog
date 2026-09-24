import random

#sorting,searching
class Algorithms:
    def __init__(self):
        pass


    def __swap(self,a,b):
        tmp = a
        a = b 
        b = tmp 
        return (a,b)
    
    
    
    def bubblesort(self,nums):
        for _ in range(1,len(nums)):
            for j in range(0,len(nums)-1):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = self.__swap(nums[j],nums[j+1])
                
        return nums
    
    def __merge(self,a,b):
        c = []
        while a and b:
            if a[0]>b[0]:
                c.append(b[0])
                del b[0]
            else:
                c.append(a[0])
                del a[0]
        while a:
            c.append(a[0])
            del a[0]
        while b:
            c.append(b[0])
            del b[0]
        return c
        
    def mergesort(self,nums):
        n = len(nums)
        if(n==1):
            return nums
        a = nums[0:n//2]
        b = nums[n//2:]
        
        a = self.mergesort(a)
        b = self.mergesort(b)
        return self.__merge(a,b)


    #Input:list
    #Output: list
    def selection_sort(self,l):
        for i in range(len(l)):
            MIN = l[i]
            pos = i
            for j in range(i,len(l)):
                if l[j]<MIN:
                    MIN = l[j]
                    pos = j
            tmp = l[i]
            l[i] = MIN
            l[pos] = tmp 
        return l
    
    #Input:int,int,list,int
    #Output: int
    def binarysearch(self,L,R,l,t):
        mid =(L+R)//2
        if L>R:
            return -1
        if l[mid] == t:
            return mid
        elif l[mid] > t:
            return self.binarysearch(L,mid-1,l,t)
        elif l[mid] <t:
            return self.binarysearch(mid+1,R,l,t)





#Test Zone
if __name__ == "__main__":
    algo = Algorithms()
    l = [random.randint(0,100) for _ in range(10)]
    print(l)
    sl = algo.bubblesort(l)
    print(sl)

