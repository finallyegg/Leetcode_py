# Hard

# Ordereddict

# Thoughts, using a priority queue or treemap or ordered dict.
# Do a traverse from left to right'

# first push 0 in, when insert some node, if a node value is start current max changes, record that node
# if node is end and after remove it, the current max changes, record (x, current_max)

# if two nodes is start, bigger first
# end, smaller first
# start and end, start first

def comp(a, b):
    if a[0] != b[0]:
        return a[0] < b[0]
    else:
        if a[2] == 's' and b[2] == 's':
            if a[1] > b[1]:
                return -1
            else:
                return 1
        elif a[2] == 'e' and b[2] == 'e':
            if a[1] < b[1]:
                return -1
            else:
                return 1
        else:
            if a[2] == 's':
                return -1
            else:
                return 1
