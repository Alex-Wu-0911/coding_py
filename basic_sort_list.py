#bubble sort list
def bubble_sort(self):
        if self.head is None or self.length == 1:
            return
        
        swap = False
        
        for i in range(self.length-1):
            current_node = self.head
            while current_node.next is not None:
                if current_node.value > current_node.next.value:
                    temp = current_node.next.value
                    current_node.next.value = current_node.value
                    current_node.value = temp
                    swap = True
                current_node = current_node.next
            if swap != True:
                break
        return self.head

def selection_sort(self):
        
        if self.length < 2:
            return
        
        index_node = self.head
        
        for i in range(self.length-1):
            current_node = index_node
            min_node = current_node
            while current_node is not None:
                if current_node.value < min_node.value:
                    min_node = current_node
                current_node = current_node.next
                
            if min_node != index_node:
                temp = min_node.value
                min_node.value = index_node.value
                index_node.value = temp    
            index_node = index_node.next
                    
        return self.head

def insertion_sort(self):
        if self.length <2:
            return
        
        sorted_list_head = self.head
        unsorted_list_head = self.head.next
        sorted_list_head.next = None
        
        while unsorted_list_head is not None:
            current = unsorted_list_head
            unsorted_list_head = unsorted_list_head.next
            
            if current.value < sorted_list_head.value:
                current.next = sorted_list_head
                sorted_list_head = current 
                
            else:
                search_pointer = sorted_list_head
                while search_pointer.next is not None and current.value > search_pointer.next.value:
                    search_pointer = search_pointer.next
                current.next = search_pointer.next
                search_pointer.next = current
                
        self.head = sorted_list_head
        return self.head
        