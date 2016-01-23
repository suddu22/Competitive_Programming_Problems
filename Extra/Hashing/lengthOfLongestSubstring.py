def lengthOfLongestSubstring(st):
    cur_set = {}
    cnt = 0
    max_set = 0
    i = 0
    while i < len(st):
        if st[i] not in cur_set:
            cnt += 1
            cur_set[st[i]] = i
            i += 1
        else:
            i = cur_set[st[i]] + 1
            if cnt > max_set:
                max_set = cnt
            cnt = 0
            cur_set = {}

    if len(cur_set) > max_set:
        max_set = len(cur_set)

    return max_set


print lengthOfLongestSubstring("abcabcbb")
# print lengthOfLongestSubstring("u")
# print lengthOfLongestSubstring("dadbc")


def fractionToDecimal(n, d):
    if n == 0:
        return "0"
    if d == 0:
        return ""

    ans = ""
    if ((n < 0) ^ (d < 0)) > 0:
        ans += "-"

    n = abs(n)
    d = abs(d)
    ans += str(n / d)
    r = (n % d) * 10
    if r == 0:
        return ans
    dic = {}
    ans += "."
    while r != 0:
        if r in dic:
            c = dic[r]
            ans = ans[:c] + "(" + ans[c:len(ans)] + ")"
            return ans
        dic[r] = len(ans)
        t = r / d
        ans += str(t)
        r = (r % d) * 10
    return ans


#print fractionToDecimal(2, 3)
