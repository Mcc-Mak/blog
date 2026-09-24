#O(NlogN)
def quicksort(data,left,right):
    if left >= right:
        return 
    i = left 
    j = right
    key = data[left] #pivot value
    while i != j:
        while data[j] > key and i<j:
            #Searching from right hand side for value smaller than pivot value
            j -=1
        while data[i] <= key and i<j:
            #Searching from left hand side for value bigger than pivot value
            i += 1
        if i < j:
            #If left and right have not met each other
            data[i], data[j] = data[j], data[i]
    #Set pivot point to meeting point of agents
    #At meeting point, the left hand side cannot be bigger than pivot value and the same as right hand side
    data[left] = data[i]
    data[i] = key
    #["88", 34, 23, 78, 67, 23, 66, 29, 79, 55, 78, "89", 92, 96, 96, 100]
    quicksort(data,left, i-1) #Handle the left hand side of "89", the smaller part
    quicksort(data,i+1,right) #Handle the right hand side from "89", the bigger part
    
    


if __name__ == "__main__":
    data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    quicksort(data,0,len(data)-1)
    print(data)
    print("__________________________________________________")
    import random 
    import math
    test_data = [math.floor(random.random()*101) for _ in range(100)]
    print("Total Number of Data: {0}\nTest Data: {1}".format(len(test_data),test_data))
    quicksort(test_data,0,len(test_data)-1)
    print("Sorted Result: {0}".format(test_data))
    
    
    
