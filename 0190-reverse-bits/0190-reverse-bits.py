class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # removing the '0b' prefix after converting to bin
        bstr = bin(n)[2:]
        
        # Paddoing 32 bits
        bstr = bstr.zfill(32)
        
        # Rev the binary string
        rev_str = bstr[::-1]
        
        # Convert the reversed binary string back to an integer
        return int(rev_str, 2)