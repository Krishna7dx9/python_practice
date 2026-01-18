# ============================================================
# SORTING ALGORITHMS — PYTHON (FOUNDATION → INTERVIEW READY)
# ============================================================
# GOAL:
# 1. Understand HOW each sort works
# 2. Know WHEN to use which sort
# 3. Be able to derive code in interviews
#
# RULE:
# Read → Understand → THEN code from memory later
# ============================================================


# ============================================================
# 1. BUBBLE SORT
# ============================================================
# IDEA:
# - Repeatedly swap adjacent elements if they are in wrong order
# - Largest element "bubbles up" to the end each pass
#
# CHARACTERISTICS:
# - Time: O(n^2) worst / average, O(n) best (optimized)
# - Space: O(1) (in-place)
# - Stable: YES
# - Interview use: Mostly for explanation, not real use


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # optimization: stop if already sorted
        if not swapped:
            break

    return arr


# ============================================================
# 2. SELECTION SORT
# ============================================================
# IDEA:
# - Repeatedly find the minimum element
# - Place it at the beginning
#
# CHARACTERISTICS:
# - Time: O(n^2) always
# - Space: O(1)
# - Stable: NO (by default)
# - Advantage: minimal swaps
# - Interview use: logic clarity


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # place smallest at correct position
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# ============================================================
# 3. INSERTION SORT
# ============================================================
# IDEA:
# - Build sorted array one element at a time
# - Insert current element into its correct position
#
# CHARACTERISTICS:
# - Time: O(n^2) worst, O(n) best
# - Space: O(1)
# - Stable: YES
# - Best for: nearly sorted data
# - Used internally in Timsort


def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # shift elements to right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# ============================================================
# 4. MERGE SORT
# ============================================================
# IDEA:
# - Divide array into halves
# - Sort each half
# - Merge sorted halves
#
# CHARACTERISTICS:
# - Time: O(n log n)
# - Space: O(n)
# - Stable: YES
# - Interview favorite (divide & conquer)
# - Used when stability matters


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ============================================================
# 5. QUICK SORT
# ============================================================
# IDEA:
# - Pick a pivot
# - Partition elements around pivot
# - Recursively sort partitions
#
# CHARACTERISTICS:
# - Time: O(n log n) average, O(n^2) worst
# - Space: O(log n) (recursion)
# - Stable: NO
# - Fastest in practice
# - Interview focus: partition logic


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# ============================================================
# 6. HEAP SORT
# ============================================================
# IDEA:
# - Build a max heap
# - Repeatedly extract max element
#
# CHARACTERISTICS:
# - Time: O(n log n)
# - Space: O(1)
# - Stable: NO
# - Good worst-case guarantee


def heap_sort(arr):
    import heapq

    heap = []
    for x in arr:
        heapq.heappush(heap, x)

    sorted_arr = []
    while heap:
        sorted_arr.append(heapq.heappop(heap))

    return sorted_arr


# ============================================================
# 7. PYTHON BUILT-IN SORT (INTERVIEW NOTE)
# ============================================================
# Python uses TIMSORT:
# - Hybrid of Merge Sort + Insertion Sort
# - Time: O(n log n) worst, O(n) best
# - Stable
# - In-place
#
# arr.sort()        → modifies list
# sorted(arr)       → returns new list


# ============================================================
# SORTING SUMMARY (MEMORIZE)
# ============================================================
# Bubble      → O(n^2), stable, teaching only
# Selection   → O(n^2), not stable, few swaps
# Insertion   → O(n^2), stable, nearly sorted
# Merge       → O(n log n), stable, extra space
# Quick       → O(n log n) avg, fastest, unstable
# Heap        → O(n log n), no recursion risk
# Timsort     → Python default, stable, adaptive
# ============================================================

