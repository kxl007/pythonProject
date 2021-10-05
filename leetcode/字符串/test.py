
import re
#h="mississippi"
#k="issip"
#n=re.search(k,h)
#print(h)

def binary_search(sort_seq, target):
    left = 0
    right = len(sort_seq) - 1
    while(left <= right):
        print(left,right)
        midpoint = (left + right)//2
        print(midpoint)
        current_item = sort_seq[midpoint]
        if current_item == target:
             return midpoint
        elif target < sort_seq[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
sort_seq=[1,2,3,4]
tar=2




binary_search(sort_seq,tar)


c='[[-99927, 2246, 97681], [-99927, 12687, 87240], [-99927, 14861, 85066], [-99927, 17307, 82620], [-99927, 24208, 75719], [-99927, 25014, 74913], [-99927, 27134, 72793], [-99927, 33447, 66480], [-99927, 37446, 62481], [-99927, 40680, 59247]]'


