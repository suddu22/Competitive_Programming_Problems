def pramp():
   print "Practice Makes Perfect"

pramp()

def intersection(a1, a2):
   m = len(a1) #1st Array
   n = len(a2)

   i = 0 #1st array
   j = 0

   res = []

   while i < m and j < n:
      if a1[i] == a2[j]:
         res.append(a1[i])
         i += 1
         j += 1
      elif a1[i] > a2[j]:
         j += 1
      else:
         i += 1

   return res

def intersection2(a1, a2):
   m = len(a1) #1st Array
   n = len(a2)
   res = []
   for num in a2:
      r = binarSearch(a1, num)
      if r != -1:
         res.append(r)

   return res

def binarSearch(arr, num):

   left = 0
   right = len(arr)-1

   while left < right:
      mid = (left + right) / 2
      if arr[mid] > num:
         left = mid + 1
      elif arr[mid] < num:
         right = mid - 1
      else:
         return arr[mid]
   return -1
