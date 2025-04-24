def bubble_sort(power_W): 
    for i in range(len(power_W)-1):
        for j in range(len(power_W)-1-i):
            if power_W[j] > power_W[j+1]:
                power_W[j], power_W[j+1] = power_W[j+1], power_W[j]
    return power_W[::-1]  # Return the sorted array in descending order