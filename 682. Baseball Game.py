class Solution:
    def calPoints(self, operations: List[str]) -> int:
        tally = []
        def is_integer(n):
            try:
                int(n)
                return True
            except ValueError:
                return False
            
        for index, element in enumerate(operations):
            if  is_integer(element):
                tally.append(int(element))
            elif element == "C":
                tally.pop(-1)
            elif element == "D":
                tally.append(int(tally[-1])*2)
            elif element == "+":
                tally.append(int(tally[-2] ) + int(tally[-1]))
            else:
                pass
            
        return sum(tally)
