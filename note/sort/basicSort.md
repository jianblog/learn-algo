## 常规的三种排序
### 1. 冒泡排序
算法复杂度
![算法复杂度](bubble1.jpg)

有序度，逆序度用来衡量内部元素之间的有序关系

排序方法，从起始向后，依次进行相邻元素比较，根据比较结果决定是否进行交换操作。经过一轮冒泡遍历后，会将最大的元素置换到最末尾。
每一轮遍历，都会让下一次遍历的终点位置减一。
有序队列是从末尾开始倒着逐渐生成
优化：当某一轮的冒泡没有发生相互交换时，说明已经有序。可以立即终止后续遍历。

![排序方法](bubble3.jpg)

```
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
        if not flag:    # 结果一轮遍历，没有发生位置交换，则说明已经有序
            break
```
### 2. 插入排序

把数列想象成由有序部分和无序两部分组成。每次依次从无序部分中取值，然后依次同有序部分比较，注意这里的比较是从有序部分的末尾开始倒着比较，比较结果决定是否将有序部分的比较元素向后移动一位，当比较结果不会移动有序元素时，则插入最初选择的元素。  因为每次选择的元素是紧挨着有序部分的末尾，所以才能将需要移动的元素依次向后移动。

```
def insertionSort(arr, n):
  if n <= 1:
      return
  for i in range(1,n):
      value = arr[i]
      j = i - 1
      while j >= 0:
          if arr[j] > value:
              arr[j+1] = arr[j]
              j -= 1
          else:
              break
      arr[j+1] = value
```

### 3. 选择排序
仍然想象由有序和无序两部分组成。与插入排序不同点在比较范围和元素移动目标不同
从无序队列中选择最小值，并交换到无序部分第一位，无序部分长度减少一位，最终全部有序

```
def selectionSort(arr, n):
    for i in range(n):
        min = i
        for j in range(i,n):
          if arr[j] < arr[min]:
              min = j
        if min != i:
            tmp = arr[i]
            arr[i] = arr[min]
            arr[min] = tmp 
```

- 插入排序每次从未排序中按次序选一个， 将它同有序部分元素进行倒着比较
- 选择排序是在无序部分中相互比较找到最小值，将它同无序部分第一个元素交换
