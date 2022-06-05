x="hello world"
# while not len(x)==5:  #len is 11 more 6 to 5
    # x=x[1:]           #will keep on until the string is sliced 5 times in the form
# print(x)
#Request for users input
#have two staring point variables,one as zero and the other one
#loop through the range of the input
#Assign each variable to the sum of the two first variables.
#Do it for the next number.
#Display each variable.
 #End function  
               #using recursion.
 
    #create function and pass in a parameter
    #subtract 2 from parameter and + 1 from parameter
    #loop through th range of that number to print the number in a sequence,kindly start at 0 coz fibonacci starts at zero
    #print each variable. 
def fibonacci():           
   z=int(input("Enter a number:"))  #request for user input
   p=0                             #two default variables start
   w=1 
  #  f=1                    
   for i in range(1,z):              #loop through all the numbers up to that number,to give youposition
       
                   #mean next is 2                   #next number is made up of sum of the two numbers
        
          next=p+w 
          p=w                 #p has moved from 0 to 1     0,1,1,2                #
          w=next        #update value of w and p        
                            #each value will come on the left operand,so continuation of add
         
        
            #w has moved to 2
   return w 
def fiboring(numby:int):         
      if numby==0:
            return 0
      elif numby==1:
            return 1
      else:
         return (fiboring(numby-1) + fiboring(numby-2))
numby=int(input("Enter a number "))
for i in range(0,numby):
  print(fiboring(i))  
  
 #purpose of the range #doesn't have to include the z   #why do we need to loop through if output is same
                                                        #prints 0 to 3
                                        #meannig next is 1
                                                #0,1,1,2,3,5,8,13,21,34,55,89,144,         
                                    
print(fibonacci())  
# def fibo():
#Create function
#pass in parameter   


#have two staring variables 0 and 1
#to get the next number  need the starters,
#
#

#i have asigned all my i