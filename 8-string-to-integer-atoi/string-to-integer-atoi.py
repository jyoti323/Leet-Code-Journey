class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        # Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        # Check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        # Parse digits, skip leading zeros
        result = 0
        started = False
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            if not started:
                if digit == 0:
                    i += 1
                    continue
                started = True
            # Check overflow before adding digit
            if result > (2**31 - 1 - digit) // 10:
                return -2**31 if sign == -1 else 2**31 - 1
            result = result * 10 + digit
            i += 1
        result *= sign
        # Clamp to 32‑bit signed int range
        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1
        return result
        