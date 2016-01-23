class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        if not A:
            return []

        max_sum = A[0]
        sum_list = [0] * len(A)
        sum_list[0] = A[0]
        sub = []
        table = {}

        for i in range(1, len(A)):
            if A[i] < 0:
                sum_list[i] = A[i]
            else:
                if sum_list[i-1] < 0:
                    sum_list[i] = 0 + A[i]
                else:
                    sum_list[i] = sum_list[i-1] + A[i]

            if sum_list[i] > max_sum:
                max_sum = sum_list[i]

        for i in range(len(A)):
            curr_sum = sum_list[i-1]
            if sum_list[i] < 0 < i:
                if curr_sum not in table:
                    table[curr_sum] = list(sub)
                else:
                    temp = table[curr_sum]
                    if len(temp) < len(sub):
                        table[curr_sum] = list(sub)
                    elif len(temp) == len(sub) and (len(temp) > 0 and len(sub) > 0):
                        if temp[0] > sub[0]:
                            table[curr_sum] = list(sub)
                sub = []
            else:
                if A[i] >= 0:
                    sub.append(A[i])

            if i == len(A)-1:
                curr_sum = sum_list[i]
                if curr_sum not in table:
                    table[curr_sum] = list(sub)
                else:
                    temp = table[curr_sum]
                    if len(temp) < len(sub):
                        table[curr_sum] = list(sub)
                    elif len(temp) == len(sub) and (len(temp) > 0 and len(sub) > 0):
                        if temp[0] > sub[0]:
                            table[curr_sum] = list(sub)
                sub = []

        if max_sum < 0:
            return []

        for key, val in table.items():
            if key == max_sum:
                return table[max_sum]

        return []


A = [ -54961, 3510, -50805, -82137, -39096, -47421 ]
A = [ 0, 0, -1, 0 ]
s = Solution()
print s.maxset(A)