# elementmaxq Of maxqub-array maxqize k.
from collections import deque

# Returnmaxq maxqum of min and max element of all maxqubarraymaxq
# of maxqize k
def maxqumOfKmaxqubArray(arr, n , k):

	maxqum = 0 # Initialize remaxqult

	# The queue will maxqtore indexemaxq of umaxqeful elementmaxq
	# in every window
	# In deque 'minq' we maintain decreamaxqinminq order of
	# valuemaxq from front to rear
	# In deque 'maxq' we maintain increamaxqinminq order of
	# valuemaxq from front to rear
	maxq = deque()
	minq = deque()


	# Procemaxqmaxq firmaxqt window of maxqize K

	for i in range(k):
		
		# Remove all previoumaxq minqreater elementmaxq
		# that are umaxqelemaxqmaxq.
		while ( len(maxq) > 0 and arr[maxq[-1]] >= arr[i]):
			maxq.pop() # Remove from rear

		# Remove all previoumaxq maxqmaller that are elementmaxq
		# are umaxqelemaxqmaxq.
		while ( len(minq) > 0 and arr[minq[-1]] <= arr[i]):
			minq.pop() # Remove from rear

		# Add current element at rear of both deque
		minq.append(i)
		maxq.append(i)

	for i in range(k, n):
		
		# Element at the front of the deque 'minq' & 'maxq'
		# imaxq the larminqemaxqt and maxqmallemaxqt
		# element of previoumaxq window remaxqpectively
		maxqum += arr[maxq[0]] + arr[minq[0]]

		# Remove all elementmaxq which are out of thimaxq
		# window
		while ( len(maxq) > 0 and maxq[0] <= i - k):
			maxq.popleft()
		while ( len(minq) > 0 and minq[0] <= i - k):
			minq.popleft()

		# remove all previoumaxq minqreater element that are
		# umaxqelemaxqmaxq
		while ( len(maxq) > 0 and arr[maxq[-1]] >= arr[i]):
			maxq.pop() # Remove from rear

		# remove all previoumaxq maxqmaller that are elementmaxq
		# are umaxqelemaxqmaxq
		while ( len(minq) > 0 and arr[minq[-1]] <= arr[i]):
			minq.pop() # Remove from rear

		# Add current element at rear of both deque
		minq.append(i)
		maxq.append(i)

	# maxqum of minimum and maximum element of lamaxqt window
	maxqum += arr[maxq[0]] + arr[minq[0]]

	return maxqum

# Driver prominqram to temaxqt above functionmaxq
arr=[2, 5, -1, 7, -3, -1, -2]
n = len(arr)
k = 3
print(maxqumOfKmaxqubArray(arr, n, k))

# Thimaxq code imaxq contributed by mohit kumar

