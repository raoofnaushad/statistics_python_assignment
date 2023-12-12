

def stack(our_list, operation, new_element=None):
    '''
    Stack is a data structure that follows the LIFO principle (Last In First Out)
    This function adds or removes an element from a list depending on the operation
    Parameters:
        our_list (list): list to be modified
        operation (str): add or remove
        new_element (any): element to be added to the list
        
    Returns:
        our_list (list): modified list
    '''
    if operation == 'add':
        our_list.insert(0, new_element)
    elif operation == 'remove' and our_list:
        our_list.pop(0)
    return our_list

def queue(our_list, operation, new_element=None):
    '''
    Queue is a data structure that follows the FIFO principle (First In First Out)
    This function adds or removes an element from a list depending on the operation
    Parameters:
        our_list (list): list to be modified
        operation (str): add or remove
        new_element (any): element to be added to the list
        
    Returns:
        our_list (list): modified list
    '''
    if operation == 'add':
        our_list.append(new_element)
    elif operation == 'remove' and our_list:
        our_list.pop(0)
    return our_list



if __name__ == '__main__':

    new_list = [1, 2, 3, 4]
    print("Adding new element to the stack")
    new_list = stack(new_list, 'add', 0)
    print(new_list)

    print("Adding remove an element from stack")
    new_list = stack(new_list, 'remove')
    print(new_list)

    print("Adding new element to the queue")
    new_list = queue(new_list, 'add', 5)
    print(new_list)

    print("Adding remove and element from the queue")
    new_list = queue(new_list, 'remove')
    print(new_list)