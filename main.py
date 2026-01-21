from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO: 1) Create a LinkedList instance
    linked_list = LinkedList()    

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    linked_list.insert_at_front(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_front(30)
    linked_list.insert_at_end(40)
    
    # TODO: 3) Display the list to verify insertion
    linked_list.display()    

    # TODO: 4) Call recursive_sum and print the result
    total_sum = linked_list.recursive_sum()
    print(f"Total Sum: {total_sum}")    

    # TODO: 5) Call recursive_search with a target and print result
    target = 20
    found = linked_list.recursive_search(target)
    print(f"Element {target} found: {found}")    

    # TODO: 6) Call recursive_reverse, then display the reversed list
    reversed_list = linked_list.recursive_reverse()
    print("Reversed List:")
    reversed_list.display()    


# 