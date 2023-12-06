def count_digit_one(n):
    count = 0
    factor = 1  # Represents the current place value (1, 10, 100, ...)

    while factor <= n:
        # Calculate the number of full groups of 10 that fit in the current place value
        full_groups = n // (10 * factor)

        # Calculate the remaining digit after removing the full groups
        remaining = n % (10 * factor)

        # Calculate the number of 1s in the current place value
        count += full_groups * factor

        # Add 1s from the remaining digits, but no more than the current factor
        count += min(factor, max(0, remaining - factor + 1))

        # Move to the next place value
        factor *= 10

    return count

# Example usage:
n = int(input())
result = count_digit_one(n)
print(result)