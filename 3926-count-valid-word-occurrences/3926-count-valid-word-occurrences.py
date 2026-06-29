class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = ''.join(chunks)
        cnt = Counter(re.findall(r'[a-z]+(?:-[a-z]+)*', s))
        return [cnt[q] for q in queries]