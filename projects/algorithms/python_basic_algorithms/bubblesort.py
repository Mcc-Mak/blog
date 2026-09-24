"""Bubble sort for 1-D arrays: the largest values bubble toward the end."""

# --- Bubble Sort ---
def bubblesort(data):
    n = len(data)
    for i in range(n - 1):
        # Inner range shrinks because the tail is already in place
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


if __name__ == "__main__":
    data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23, 100, 0, 5293019209]
    ans = bubblesort(data)
    print(ans)
