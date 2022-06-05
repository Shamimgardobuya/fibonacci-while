# def take():
#     user_input=[(input("enter number:"))]
#     newlist=[]
#     newlist.copy(user_input)
#     print(newlist.reverse())
# take()    

# def reve():
#     new_list=[]
#     while len(new_list)!=10:
#      user=int(input("enter: "))
#      new_list.append(user)
#     x=new_list.reverse()
#     print(x)
# reve()    
# def reve():
#     new_list=[]
#     while len(new_list)!=10:
#      user=int(input("enter: "))
#      new_list.append(user)
#     x=new_list.reverse()
#     print(x)
# reve() 

def average():
    x = []
    while len(x)!=10:
        user = int(input("enter 10 elements"))
        x.append(user)
        y = len(x)
        total = sum(x)
    aver= total/y
    print(aver)   


average()
       