"""
https://programmers.co.kr/learn/courses/30/lessons/60057
"""

def solution(s):
    if len(s) == 1:
        return 1
    INF = int(1e9)
    answer = INF
    length = len(s)
    for step in range(1, length//2+1):
        compressed = []
        ref = s[0:step]
        same_count = 1        
        for j in range(step, length+1, step):
            word = s[j:j+step]
            if ref == word:
                same_count += 1
            else:
                if same_count == 1:
                    compressed += ref
                else:
                    compressed += str(same_count) + ref
                ref = word
                same_count = 1
        compressed += s[j:]
        answer = min(answer, len(compressed))
    return answer
