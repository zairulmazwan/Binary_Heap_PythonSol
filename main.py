from BinaryHeap import Heap

data = [47,57,23,43,31,29,17]

print("\nMaximum Heap Tree")

heap_tree = Heap(len(data))
heap_tree.create_max_heap(data)
heap_tree.print_heap()

print("\nAfter deleting a node")
heap_tree.delete_node(1)
heap_tree.print_heap()

sorted  = heap_tree.descending_order()
print("\nDescending order")
heap_tree.print_list(sorted)

print("\n\nMinimum Heap Tree")
min_heap = Heap(len(data))
min_heap.create_min_heap(data)
min_heap.print_heap()

print("\nAscending order")
asc = min_heap.ascending_order()
min_heap.print_list(asc)
min_heap.delete_node_min(2)
print()
min_heap.print_heap()

# ©Zairul Mazwan©