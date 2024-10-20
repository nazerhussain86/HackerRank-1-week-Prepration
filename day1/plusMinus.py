def plusMinus(arr):
    # Write your code here
    
    positiveNums = []
    negativeNums =[]
    zeros=[]
    
    for i in arr:
        if i == 0:
            zeros.append(i)
        elif i > 0:
            positiveNums.append(i)
        else:
            negativeNums.append(i)
            
    lengthofArr = len(arr)
    
    lenofPos = len(positiveNums)
    lenofNeg = len(negativeNums)
    lenofZeo = len(zeros)
    
    print(lenofPos/lengthofArr)
    print(lenofNeg/lengthofArr)
    print(lenofZeo/lengthofArr)
