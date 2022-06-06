# 조건: 대소문자 구분x, banned 단어는 포함 x, 기호는 x 
import re
from typing import List
import collections 

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph) \
        .lower().split() if word not in banned]
    
    counts = collections.Counter(words)
    #가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
    return counts.most_common(1)[0][0]
    