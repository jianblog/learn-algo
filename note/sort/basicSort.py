"""
基本排序：
  1. 冒泡
  2. 插入
  3. 选择
"""

def bubbleSort(arr, n):
  if n <= 1:
    return
  for i in range(n):
    flag = False
      for j in range(n-i-1):
        if arr[j] > arr[j+1]:
          tmp = arr[j+1]
          arr[j+1] = arr[j]
          arr[j] = tmp
          flag = True
      if not flag:
        break
        
        
def insertionSort(arr, n):
  if n <= 1:
    return
  for i in range(1,n):    # 外层循环从第2个元素开始
    value = arr[i]
    j = i - 1
    while j >= 0:   # 元素位i分别和i之前的所有有序元素比较，确定合适的插入点，比它大的都依次被向后移动
      if arr[j] > value:
        arr[j+1] = arr[j]
        j -= 1
      else:
        break
    arr[j+1] = value
    
    
def selectionSort(arr, n):
  if n <= 1:
    return
  for i in range(n):    # 每一轮遍历预先设定当前i为最小值
    min = i
    for j in range(i,n):    # 嵌套一层遍历，与参考值比较，发现最小值
      if arr[j] < arr[min]:
        min = j
    if i != min:    # 将最小值与i位交换，进行下一轮遍历并移动i至下一位
      tmp = arr[i]
      arr[i] = arr[min]
      arr[min] = tmp
