# Decimal - 74 97 110 105 115
# Binary -  00110111 00110100 00111001 00110111 00110001 00110001 00110000 00110001 00110000 00110101 00110001 00110001 00110101
# Name -Janis


def bubbleSort(arr):
    n = len(arr)

    for i in range(n):

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [74, 97, 110, 105, 115, ]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i]),


