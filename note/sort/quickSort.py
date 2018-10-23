"""
## 快速排序
快速排序的核心思想是从待排序数组中选择一个作为参考点，然后经过一轮排序后该参考点左侧都小于参考点，右侧的元素都大于参考点

通过不断递归演算，分别对左侧和右侧的两个数组再次进行上述排序操作，最终实现完全有序

大问题不断化小的分治思想

实现快排的两种思路：

### 非原地排序
排序时额外申请临时空间保存被移动的元素，组成小于参考点的数组和大于参考点的数组，然后递归对前后两部分数据再次排序，中间的参考点直接添加到最终结果
"""

def quickSort1(arr):
  length = len(arr)
  flag = arr[-1]
  left = []
  right = []
  
  for i in range(length-1):
    if arr[i] < flag:
      left.append(arr[i])
    else:
      right.append(arr[i])
  # 对三个部分进行合并
  result = quickSort1(left)
  result.append(flag)
  result.extend(quickSort1(right))
  return result


### 原地排序
# 使用前后两个指针轮流读取逐渐向中间逼近,移动单个元素

def quick_sort1(arr, left, right):
  low = left
  high = right
  if low >= high:
    return
  
  flag = arr[right]
  while left < right:  # 左右各有一个指针根据比较结果向中间逼近
    while left < right and arr[left] < flag:
      left += 1             # 左侧指针向右逼近，指针左侧的都小于参考点
    arr[right] = arr[left]  # 寻找大于参考点的元素并与参考点交换到最右边
    while right > left and arr[right] >= flag:
      right -= 1
    arr[left] = arr[right]  # 该移动操作能执行的前提就是之前已经将arr[left]移动到right，再次发现右边的较小值就移动到该空位
  arr[right] = flag         # 最后一次执行的是将右侧移动到左侧，最终将原始参考点放在当前right位置
  
  quick_sort1(arr, low, left-1)
  quick_sort1(arr, left+1, high)
  return arr


# 左右交换方式
def quick_sort2(arr, left, right):
  if left >= right:
    return
  flag = arr[right]
  i = left
  for j in range(i, right+1):
    if arr[j] < flag:
      arr[i], arr[j] = arr[j], arr[i]   # 发现遍历的j元素小于参考点时，交换这个较小值与i位置值
      i += 1                            # i位置总是指向了当前数组第一个比参考点大的元素
  arr[i], arr[right] = arr[right], arr[i]  # 最后将参考点与第一个比它大的i位值交换，实现了参考点左右两侧数据符合要求
  quick_sort2(arr, left, i-1)
  quick_sort2(arr, i+1, right)
