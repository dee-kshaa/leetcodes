class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        ans = []

        def dfs(idx, cost, prev_one, cur):
            if cost > k:
                return

            if idx == n:
                ans.append("".join(cur))
                return

            cur.append('0')
            dfs(idx + 1, cost, False, cur)
            cur.pop()

            if not prev_one:
                cur.append('1')
                dfs(idx + 1, cost + idx, True, cur)
                cur.pop()

        dfs(0, 0, False, [])
        return ans