import math

class Collatz:
    
    def __init__(self):
        self.memo = {}
        
        
    def collatzLength(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        
        if n == 1:
            return 1
        if n % 2 == 0:
            length = 1 + self.collatzLength(n // 2)
        else:
            #for any 3*n + 1 you always get an even number can stop from traversing into another recursive call
            length = 2 + self.collatzLength((3 * n + 1) // 2)
            
        self.memo[n] = length
        return length
    
    
    #if divisible by 2 all the way down don't have to look at it. (2, 4, 8, 16, 32, 64)
    def longestInRange(self, a: int, b: int) -> int:
        max_length = 0
        number_with_max_length = a

        for i in range(a, b + 1):
            if math.log2(i) % 1 != 0:
                length = self.collatzLength(i)
                if length > max_length:
                    max_length = length
                    number_with_max_length = i

        return number_with_max_length
    
def main():
    import sys
    
    print("Enter the range:", end=" ")
    a, b = map(int, sys.stdin.readline().strip().split())
    
    collatz = Collatz()
    number = collatz.longestInRange(a, b)
    length = collatz.collatzLength(number)
    
    print(f"The number with the greatest Collatz length in this range: {number}")
    print(f"The Collatz length of {number} is {length}")
        
if __name__ == "__main__":
    main()