class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_database = {}

        for element in s:
            if element not in my_database:
                my_database[element] = 1
            else:
                my_database[element] += 1

        for element in t:
            if element not in my_database:
                return False
            else:
                my_database[element] -= 1  
            
            if my_database[element] == 0:
                del my_database[element]

        if not bool(my_database):
            return True
        else:
            return False
