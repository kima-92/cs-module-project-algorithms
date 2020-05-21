'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Set a variable to store the current index
    temp_arr = []
    # Set a variable to store the total
    total = 1
    # Set a variable to store the results_arr
    results_arr = []

    # For the range of the length of arr
    for i in range(0, (len(arr)  )):
        # For each element in arr

        element_found = False
        temp_arr = arr
        current_index = 0

        while element_found == False:

            for elem in range(0, len(arr)):
                # If this element is not the element in current
                if arr[elem] != arr[i]:
                    # Multiply the total by this element
                    total = total * arr[elem]
                    #temp_arr.remove(elem)
                    current_index += 1

                else: 
                    element_found = True
                    #temp_arr.remove(elem)
                    current_index += 1
                    break

            # Append this total to the results_arr
            #results_arr.append(total)
            # Set total to 1
            #total = 1

        if current_index <= (len(arr)-1):
            
            for _ in range(current_index, len(arr)):
                # Multiply the total by this element
                total = total * arr[current_index]
                #temp_arr.remove(elem)
                current_index += 1
                
        # Append this total to the results_arr
        results_arr.append(total)
        # Set total to 1
        total = 1



    # Return the results_arr
    return results_arr




if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")

