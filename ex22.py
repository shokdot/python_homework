def second_largest(arr):
    first = second = float('-inf')
    if len(arr) < 2:
        return None
    for i in arr:
        if i > first:
            second = first
            first = i
        elif first > i > second:
            second = i
    if second == float('-inf'):
        return None
    else:
        return second

arr = [5, 10, 15, 20, 30, 35]
print(second_largest(arr))
            
