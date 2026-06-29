class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(key=lambda x: -x[0])

        total_profit = 0
        seen = set()
        duplicates = []  # will store duplicate profits in sorted order (ascending)

        # Step 2: Pick the top k items initially
        for i in range(k):
            profit, category = items[i]
            total_profit += profit
            if category in seen:
                # Insert in sorted order (acts like min-heap)
                pos = 0
                while pos < len(duplicates) and duplicates[pos] < profit:
                    pos += 1
                duplicates.insert(pos, profit)
            seen.add(category)

        # Step 3: Calculate initial elegance
        max_elegance = total_profit + len(seen) ** 2

        # Step 4: Try replacing duplicates with new categories
        for i in range(k, len(items)):
            profit, category = items[i]
            if category not in seen and duplicates:
                # Remove the smallest duplicate
                removed_profit = duplicates.pop(0)
                total_profit += profit - removed_profit
                seen.add(category)
                max_elegance = max(max_elegance, total_profit + len(seen) ** 2)

        return max_elegance