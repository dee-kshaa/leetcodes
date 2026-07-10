class Solution:
    def isNumber(self, s: str) -> bool:
        digit = ex = dot = False

        for i, c in enumerate(s):
            if c.isdigit():
                digit = True
            
            elif c in '+-':
                if not (i == 0 or (s[i - 1]) in 'Ee'):
                    return False
            
            elif c in 'eE':
                if ex or not digit:
                    return False
                ex = True
                digit = False
            
            elif c == '.':
                if dot or ex:
                    return False
                dot = True
            else:
                return False
        
        return digit
            