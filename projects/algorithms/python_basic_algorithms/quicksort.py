"""Quick sort with a pivot value chosen as the left element. O(NlogN)."""
def quicksort(data, left, right):
    if left >= right:
        return
    i = left
    j = right
    key = data[left]  # Pivot value
    while i != j:
        # Search from the right for a value smaller than the pivot value
        while data[j] > key and i < j:
            j -= 1
        # Search from the left for a value bigger than the pivot value
        while data[i] <= key and i < j:
            i += 1
        if i < j:
            # Swap the two if the left and right agents have not met
            data[i], data[j] = data[j], data[i]
    # Put the pivot value at the meeting point of the agents
    # (left side <= pivot, right side >= pivot)
    data[left] = data[i]
    data[i] = key
    # ["88", 34, 23, 78, 67, 23, 66, 29, 79, 55, 78, "89", 92, 96, 96, 100]
    quicksort(data, left, i - 1)  # Sort the smaller part on the left
    quicksort(data, i + 1, right)  # Sort the bigger part on the right
if __name__ == "__main__":
    data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    quicksort(data, 0, len(data) - 1)
    print(data)
    print("__________________________________________________")
    import random
    import math
    test_data = [math.floor(random.random() * 101) for _ in range(100)]
    print("Total Number of Data: {0}\nTest Data: {1}".format(len(test_data), test_data))
    quicksort(test_data, 0, len(test_data) - 1)
    print("Sorted Result: {0}".format(test_data))
