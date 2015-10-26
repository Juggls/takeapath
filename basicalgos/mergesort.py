def mergesort(elements):
	if len(elements) > 1:
		left = mergesort(elements[:len(elements)/2])
		right = mergesort(elements[len(elements)/2:])
		sortedlist = merge(left, right)
		return sortedlist

	else:
		return elements

def merge(list1, list2):
	sortedlist = []

	j = 0
	i = 0
	while True:
		if i >= len(list1) or j >= len(list2):
			break 

		if list1[i] > list2[j]:
			sortedlist.append(list2[j])
			j +=1
		else:
			sortedlist.append(list1[i])
			i+=1

	while(i < len(list1)):
		sortedlist.append(list1[i])
		i+=1
	while(j < len(list2)):
		sortedlist.append(list2[j])
		j+=1

	return sortedlist

	

unsorted_l = [0,10,40,50,-2,5,6,7,8,8,9,-40,-192,72,6]

sorted_l = mergesort(unsorted_l)

print sorted_l