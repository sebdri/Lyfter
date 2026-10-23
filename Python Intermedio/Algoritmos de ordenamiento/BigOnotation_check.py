'''Analice los siguientes algoritmos usando la Big O Notation'''


# print_numbers_times_2

def print_numbers_times_2(numbers_list): 
	for number in numbers_list: #o(n)
		print(number * 2) #o(1)



# check_if_lists_have_an_equal

def check_if_lists_have_an_equal(list_a, list_b):
	for element_a in list_a: # o(n)
		for element_b in list_b: #o(n²)
			if element_a == element_b: # o(1)
				return True #o(1)
				
	return False #o(1)


#print_10_or_less_elements 


def print_10_or_less_elements(list_to_print):
	list_len = len(list_to_print) #o(1)
	for index in range(min(list_len, 10)): #o(1) 
		print(list_to_print[index]) #o(1)



#generate_list_trios


def generate_list_trios(list_a, list_b, list_c):
	result_list = [] #O(1)
	for element_a in list_a: #o(n)
		for element_b in list_b: #o(n²)
			for element_c in list_c: #o(n³)
				result_list.append(f'{element_a} {element_b} {element_c}') #o(1)
				
	return result_list #o(1)