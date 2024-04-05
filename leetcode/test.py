class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    # Reverse the input strings to start adding from the least significant digits
    num1 = num1[::-1]
    num2 = num2[::-1]
    # Pad the shorter input string with zeros
    if len(num1) < len(num2):
        num1 += '0' * (len(num2) - len(num1))
    else:
        num2 += '0' * (len(num1) - len(num2))
    
    result = ''
    carry = 0
    
    # Loop through both strings, starting from the least significant digits
    for i in range(len(num1)):
        # Convert the current digit in each string to an integer and add them together
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        # Determine the carry for the next iteration, if any
        carry = digit_sum // 10
        # Append the least significant digit of the sum to the result string
        result += str(digit_sum % 10)
    
    # If there is a carry after the last iteration, append it to the result string
    if carry > 0:
        result += str(carry)
    
    # Reverse the result string to obtain the final sum
    return result[::-1]