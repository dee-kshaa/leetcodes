class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        dist = [[float("inf")] * n for _ in range(n)]
        q = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    q.append((r, c))

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == float("inf"):
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        seen = [[False] * n for _ in range(n)]

        heap = [(-dist[0][0], 0, 0)]

        while heap:
            neg_safe, r, c = heapq.heappop(heap)
            safe = -neg_safe

            if seen[r][c]:
                continue

            seen[r][c] = True

            if r == n - 1 and c == n - 1:
                return safe

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not seen[nr][nc]:
                    new_safe = min(safe, dist[nr][nc])
                    heapq.heappush(heap, (-new_safe, nr, nc))

        return -1