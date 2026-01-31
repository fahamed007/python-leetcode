#2126. Destroying Asteroids
#https://leetcode.com/problems/destroying-asteroids/description/
class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        heaviest=asteroids[-1]
        for val in asteroids:
            if mass < val:
                return False
            mass +=val
            if mass >=heaviest:
                return True
        return True
