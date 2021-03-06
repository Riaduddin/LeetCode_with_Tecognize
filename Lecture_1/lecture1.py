
"""
Time complexity is O(n), but it takes too much time for many operations. It iterate to every element of the list.
"""
class Two_sum1:
  def twoSum(nums: list, target: int)->list:
    a=nums
    results=[]
    p=0
    q=len(a)
    s=0
    i=e=1
    for j in range(1,q):
      p=p+j
    while p!=0:
      x=a[s]
      y=a[e]
      sum=x+y
      if sum==target:
        results+=s,e
      e+=1
      if e==q:
        s+=1
        i+=1
        e=i
      p-=1
    return results
  
"""
Using hash functions
"""

class Two_sum2:
    def twoSum(self, nums: list, target: int):
          values= {}
          for i, n in enumerate(nums):
              if target - n in values:
                  return [values[target-n], i]
              values[n] = i