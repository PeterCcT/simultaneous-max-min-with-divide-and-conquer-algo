MinMaxResult = tuple[int, int]


def maxmin_select_divide_conquer(sequence: list[int], left: int, right: int) -> MinMaxResult:
    if left == right:
        return sequence[left], sequence[left]
    
    next_index = left + 1
    if right == next_index:
        if sequence[left] < sequence[right]:
            min_val = sequence[left]
            max_val = sequence[right]
        else:
            min_val = sequence[right]
            max_val = sequence[left]
        
        return min_val, max_val
    
    middle = (left + right) // 2
    middle_next = middle + 1
    
    min_left, max_left = maxmin_select_divide_conquer(sequence, left, middle)
    min_right, max_right = maxmin_select_divide_conquer(sequence, middle_next, right)
    
    min_val = min(min_left, min_right)
    max_val = max(max_left, max_right)
    
    return min_val, max_val


def maxmin_select(sequence: list[int]) -> MinMaxResult:
    if not sequence:
        raise ValueError('A sequência não pode estar vazia')
    
    if len(sequence) == 1:
        return sequence[0], sequence[0]
    
    return maxmin_select_divide_conquer(sequence, 0, len(sequence) - 1)


if __name__ == '__main__':
    tests = [
        [5, 3, 8, 1, 9, 2, 7],
        [42, 15, 23, 8, 4, 16, 42, 108],
        [10, -5, 3, -20, 15, 0, -8, 25],
        [7],
        [3, 1]
    ]
    
    for i, sequence in enumerate(tests, 1):
        print(f'=== Teste {i}: {sequence} ===')
        min_val, max_val = maxmin_select(sequence)
        print(f'Mínimo: {min_val}, Máximo: {max_val}')
