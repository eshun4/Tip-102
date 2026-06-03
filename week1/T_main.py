def count_less_than(race_times, threshold):
    # Counter for the elements less than threshold
    counter = 0
    # Iterate through the elements in the array 
    for rt in race_times:
	    # Compare each element to threshold (<)
	    if rt < threshold:
	        # Count the elements that go through
	        counter = counter + 1
    return counter
	
race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
print(count_less_than(race_times, threshold))

race_times = []
threshold = 4
print(count_less_than(race_times, threshold))
	    