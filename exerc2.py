def reverso(num):
    nums = str(num)
    numL = len(nums)
    j = -1
    i=0
    rever = []
    while i < len(nums):
        if i < numL:
            rever.append((nums[j]))
            reverso = ''.join(rever)
            j-=1
        i+=1
        
    print('O reverso do número é:',reverso)
    #print(rever)
    
num = int(input('Digite um número inteiro '))
reverso(num) 