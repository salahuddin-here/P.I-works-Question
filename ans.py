def read_text(path):
    return([[item for item in line.split()] for line in open(path)])

def checkNotprimeNumber(num): 
    for i in range(2, num //2):
       if (num % i) == 0:
           return True 
    
    return False
    
def MaximumNumber(arr):

    for i in range (1,arr.__len__()):
        for j in range(0,i+1):
            if checkNotprimeNumber(arr[i][j]) :
                if (j==0):
                    arr[i][j] = arr[i-1][j] + arr[i][j]
                elif j<i and j>0:
                    if arr[i-1][j] > arr[i-1][j-1]:
                        arr[i][j] = arr[i-1][j] + arr[i][j]
                    else:
                        arr[i][j] = arr[i-1][j-1] + arr[i][j]
                else:
                    arr[i][j] = arr[i-1][j-1] + arr[i][j]
                
    return arr
f1 = "triangle1.txt"
f2 = "triangle2.txt"
file_name = input("Enter 1 for " + f1 + ", & 2 for "+f2+" :" )
if file_name == '1':
    file_name = f1
elif file_name == '2':
    file_name = f2
arr = read_text(file_name)
new_Arr =[[int(arr[0][0])]]
for i in range (1,arr.__len__()):
    new_Arr.append([])
    for j in range(0, i+1):
        new_Arr[i].append(int(arr[i][j]))
print (new_Arr)
f_arr = MaximumNumber(new_Arr)
row = f_arr.__len__()-1
temp = 0
for j in range(0, row):
    if f_arr[row][j] > temp :
        temp = f_arr[row][j]
print("\n\n")
print(f_arr)
print("\nMaximum Sum is = " + str(temp))




  
