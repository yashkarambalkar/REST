'''[x1, X2] = [0.2, 0.6] and the weights are [w1, w2] =[0.3, 0.7]. Since the bias is included 
b = 0.45 and bias input xo is equal to 1, the net input is calculated as
Yin= b+x1W1 +X2W2
 = 0.45 + 0.2 X 0.3 + 0.6 X 0.7
 = 0.45 + 0.06 + 0.42 = 0.93
Therefore ym = 0.93 is the net input.'''

n = int(input("Enter number of elements : ")) 
print("Enter the inputs:")

inputs = [] # creating an empty list for inputs
for i in range(0, n): 
    ele = float(input()) 
    inputs.append(ele) # adding the element 
print(inputs)

print("Enter the weights:")
weights = [] 
for i in range(0, n): 
    ele = float(input()) 
    weights.append(ele) # adding the element 
print(weights)

b=float(input("Enter bias value:"))
print("The net input can be calculated as Yin = b + x1w1 + x2w2:")

Yin = []
for i in range(0, n):
    Yin.append(inputs[i]*weights[i])
print(round((sum(Yin)+b),3))


'''Enter number of elements : 2
Enter the inputs:
0.2
0.6
[0.2, 0.6]
Enter the weights:
0.3
0.7
[0.3, 0.7]
Enter bias value:0.45
The net input can be calculated as Yin = b + x1w1 + x2w2:
0.93'''
