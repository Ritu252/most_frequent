s = input()
def most_frequent(string):
    list1 = []
    for i in string:
        list1.append(i)
    list2 = []
    for ele in list1:
        x = list1.count(ele)
        list2.append(x)
    for ele in list1:
        if list1.count(ele)>1:
            list1.remove(ele)
    for ele in list2:
        if list2.count(ele)>1:
            list2.remove(ele)
    for i in range(len(list2)):
        print(list1[i],list2[i])
most_frequent(s)
        
    














































