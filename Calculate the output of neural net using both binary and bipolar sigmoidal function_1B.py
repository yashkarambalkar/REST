'''The inputs and weight are 
[x1, x2, x3] = [0.3, 0.5, 0.6]
[w1, w2, w3] = [0.2, 0.1, -0.3]
The net input can be calculated as 
Yin = x1w1+x2w2+x3w3
 = 0.3*0.2+0.5*0.1+0.6*(-0.3)
 = -0.07
'''

# number of elements as input 
n = int(input("Enter number of elements : ")) 
# In[2]:
print("Enter the inputs")
inputs = [] # creating an empty list for inputs
# iterating till the range 
for i in range(0, n): 
    ele = float(input()) 
    inputs.append(ele) # adding the element 
print(inputs) 
# In[3]:
print("Enter the weights")
# creating an empty list for weights
weights = [] 
# iterating till the range 
for i in range(0, n): 
    ele = float(input()) 
    weights.append(ele) # adding the element 
print(weights) 
# In[4]:
print("The net input can be calculated as Yin = x1w1 + x2w2 + x3w3")
# In[5]:
Yin = []
for i in range(0, n):
    Yin.append(inputs[i]*weights[i])
print(round(sum(Yin),3))
