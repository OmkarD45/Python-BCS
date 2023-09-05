
#list as a queue


from collections import deque
list1=deque([10,20,30,40,50,60])
print("original element in list:\t",list1)
list1.remove(40)
print("after remove list is:\t",list1)
list1.pop()
print("after poping list is:\t",list1)
list1.popleft()
print("after left poping list is: ",list1)
