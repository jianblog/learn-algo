"""
归并排序：
  归并排序分两个过程，一个是将较长的数组拆分成两部分进行递归拆分调用，边界条件是数组仅有一个元素；
  然后是对返回的数组进行合并操作
"""
def split(arr):
  n = len(arr)
  if n <= 1:
    return arr
  num = n // 2    #选择中间点对数组进行拆分
  left = split(arr[:num])
  right = split(arr[num:])
  return mergeSort(left, right)
def mergeSort(x, y):
  i, j = 0, 0
  result = []
  while i < len(x) and j < len(y):
    # 遍历比较，最终只可能剩余一个数组
    if x[i] < y[j]:
      result.append(x[i])
      i += 1
    else:
      result.append(y[j])
      j += 1
  # 将比较剩余的数组添加到result之后
  result.extend(x[i:])    
  result.extend(y[j:])
  return result

