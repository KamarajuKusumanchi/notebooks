# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# 387. First Unique Character in a String
#
# Given a string `s`, find the **first** non-repeating character in it and return its index. If it **does not** exist, return `-1`.
#
# **Example 1:**
#
# **Input:** s = "leetcode"
#
# **Output:** 0
#
# **Explanation:**
#
# The character `'l'` at index 0 is the first character that does not occur at any other index.
#
# **Example 2:**
#
# **Input:** s = "loveleetcode"
#
# **Output:** 2
#
# **Example 3:**
#
# **Input:** s = "aabb"
#
# **Output:** -1
#
# **Constraints:**
#
# *   <code>1 <= s.length <= 10<sup>5</sup></code>
# *   `s` consists of only lowercase English letters.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # count the frequency of each character
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        # get the index of the first unique character
        for i in range(len(s)):
            if count[s[i]] == 1:
              return i
        return -1    # fallback


strings = ['leetcode', 'loveleetcode', 'aabb']
ind = [Solution().firstUniqChar(s) for s in strings]
print(ind)


