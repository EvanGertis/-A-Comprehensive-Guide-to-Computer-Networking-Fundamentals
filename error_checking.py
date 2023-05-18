def parity_check(binary_string):
    # Count the number of 1s in the binary string
    count = binary_string.count('1')

    # Determine the parity based on whether the count is even or odd
    if count % 2 == 0:
        return 'even'
    else:
        return 'odd'

binary_string = '110101'
parity = parity_check(binary_string)
print(f'The parity of {binary_string} is {parity}.')