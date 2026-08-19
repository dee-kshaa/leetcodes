class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Each row has 3 possible group positions: 'left', 'middle', 'right'.
        # We will keep track of which positions are unavailable (blocked).
        blocked = defaultdict(set)

        # Iterate over all reserved seats, saving blocked positions.
        for row, col in reservedSeats:
            if col in [2, 3, 4, 5]:
                blocked[row].add('left')
            if col in [4, 5, 6, 7]:
                blocked[row].add('middle')
            if col in [6, 7, 8, 9]:
                blocked[row].add('right')
        
        # The variable total will hold the number of 4-person reservations available.
        # Initialize it with 2 per row having no seats blocked.
        total = 2 * (n - len(blocked))

        # Provide the number of sections available based on the number blocked.
        # For example, if 0 are blocked, 2 are available.
        numAvailable = {0: 2, 1: 1, 2: 1, 3: 0}
        
        # For each row with blocked sections, add the number of available sections.
        for numBlocked in blocked.values():
            total += numAvailable[len(numBlocked)]

        return total