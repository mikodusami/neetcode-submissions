class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        b = Counter("balloon")
        c = Counter(text)
        count = 0

        def remove_non_baloon_chars():
            removal = set()
            for key in c.keys():
                if key not in {"b", "a", "l", "n", "o"}:
                    removal.add(c[key])
            for key in removal:
                del c[key]

        def satisfies_baloon():
            for letter in {"b", "a", "l", "n", "o"}:
                if b[letter] > c[letter]:
                    return False
            
            return True
        
        def decrement_characters():
            for letter in {"b", "a", "l", "n", "o"}:
                c[letter] -= b[letter]
        
        remove_non_baloon_chars()
        x = 0
        while True:
            print(b, c, x)
            if not satisfies_baloon():
                break
            x += 1
            decrement_characters()

        return x
