class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        if i == 0:
            if digits[i] == 9:
                digits[0] = 0
                return [1] + digits
            else:
                digits[i] = digits[i] + 1
                return digits
        while i > 0:
            if digits[i] == 9:
                digits[i] = 0
                i -= 1
            else:
                digits[i] = digits[i] + 1
                return digits
        if digits[0] == 9:
            digits[0] = 0
            return [1] + digits
        else:
            digits[i] = digits[i] + 1
            return digits

        