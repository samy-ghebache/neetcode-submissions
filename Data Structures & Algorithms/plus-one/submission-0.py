class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        offset = 1
        for i in range(len(digits) - 1, -1, -1):
            tempSum = (digits[i] + offset)
            digits[i] = tempSum % 10
            offset = tempSum // 10
            if offset == 0:
                break
        if offset > 0:
            digits.insert(0, offset)
        return digits
