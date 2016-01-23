'''
['a', 'c', ' ', ' ', 'b']
[['a','c'], ['b']]

edge cases:
- multiple spaces
- space at beginning
- space in the end
- last word

'g', 'o', ' ', t h e r e
e r e h t ' ' o g
'''

def solution(arr):
   res = [] #array to return

   #useless
   words = [] #list of words
   tmp = []
   ind = 0
   for index, i in enumerate(arr):
      if i is ' ':
         if tmp: #if I added the previous word already doesn't add it again
            words.append(arr[ind:index])
         ind = index + 1

   if tmp:
      words.append(arr[ind:index])

   while words:
      res.extend(words.pop())
      res.append(' ')

   return res

def solution2(arr):
   reverse(arr, 0, len(arr)-1)
   start = 0
   for index, char in enumerate(arr):
      if char is ' ' or index is len(arr)-1:
            if index is len(arr - 1):
                index += 1
                reverse(arr, start, index - 1)
            start = index + 1

def reverse(arr, start, end):
   while start != end:
      arr[start], arr[end] = arr[end], arr[start]
      start += 1
      end -= 1

"""
Given an array of integers arr, write a function that returns another array at the same length where the value at each index i is the product of all array values except arr[i].

Solve without using division and analyze the runtime and space complexity

Example: given the array [2, 7, 3, 4]
your function would return: [84, 24, 56, 42] (by calculating: [7*3*4, 2*3*4, 2*7*4, 2*7*3])

https://www.pramp.com/question/2WBx3Axln1t7JQ2jQq96

https://www.pramp.com/question/7Lg1WA1nZqfoWgPbgM0M

https://www.interviewcake.com/question/python/product-of-other-numbers

"""