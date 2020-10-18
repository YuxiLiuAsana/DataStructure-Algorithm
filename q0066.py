class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += carry
            carry = digits[i]//10
            digits[i] = digits[i]%10
            if carry == 0: break
        if carry != 0:
            return [carry] + digits
        else:
            return digits