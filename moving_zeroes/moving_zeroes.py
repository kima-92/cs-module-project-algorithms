'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Set a variable for the new array result
    result = []
    # Set a variable to store the zeros
    zeros = []

    # For each element in arr
    for i in arr:
        # If the element is 0
        if i == 0:
            # Store in zeros
            zeros.append(i)
        # Else
        else:
            # Store in result
            result.append(i)

    # If zeros is not empty
    if len(zeros) != 0:
        # Append each of it's elements to result
        result.extend(zeros)

    # Return the new array result
    return result



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")