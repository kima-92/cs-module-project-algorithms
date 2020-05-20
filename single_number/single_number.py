'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Set avariable to store duplicates
    duplicates = []
    # Set variable to store the unique element
    uniques = []

    # For each element in arr
    for i in arr:

        # If uniques is not empty
        if uniques != []:
            
            # If the element is not in unique
            if i not in uniques:
                # Add the element in uniques
                uniques.append(i)


            # Else: if the element is already in uniques
            else:
                # Store in duplicates
                duplicates.append(i)
                # Remove the old one from unique,
                # and add it to duplicates
                uniques.remove(i)
                duplicates.append(i)

        # Else: If unique is empty
        else:
            # Add the element to uniques
            uniques.append(i)
    
    # Return the first element in unique
    return uniques[0]



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")