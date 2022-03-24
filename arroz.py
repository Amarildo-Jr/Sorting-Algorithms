import sys,time
from bubblesort import bubbleSort

input_array=[]
if (len(sys.argv) < 2):
    print("")
    print("Please input list items as arguments")
    print("\nExample: ./bubblesort.py <item1> [item2] [item3] [item4] ...")
    quit()
i=1
time1 = time.time()
while (i < len(sys.argv)):
    input_array.append(int(sys.argv[i]))
    i+=1

vetor = [8, 27, 9, 6, 16, 21, 5, 3, 26, 10, 15, 17, 29, 24, 14]
#vetor = [19, 24, 23, 21, 28, 3, 30, 11]
#print(mergesort(vetor, 0, len(vetor) - 1))
print(bubbleSort(vetor))