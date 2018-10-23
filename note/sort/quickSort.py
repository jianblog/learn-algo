"""
## 快速排序
快速排序的核心思想是从待排序数组中选择一个作为参考点，然后经过一轮排序后该参考点左侧都小于参考点，右侧的元素都大于参考点

通过不断递归演算，分别对左侧和右侧的两个数组再次进行上述排序操作，最终实现完全有序

大问题不断化小的分治思想

实现快排的两种思路：

### 非原地排序
排序时额外申请临时空间保存被移动的元素，构成小于参考点的数组和大于参考点的数组
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
