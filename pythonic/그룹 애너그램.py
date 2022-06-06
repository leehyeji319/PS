from typing import List
import collections

input = ["eat", "tea", "tan", "ate", "nat", "bat"]

def grouptAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)
    
    for word in strs:
        #정렬하여 딕셔너리 추가
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()