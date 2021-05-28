


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        dates  = []
        for birth, death in logs:
            dates.append((birth, 1))
            dates.append((death, -1))

        dates.sort()

        population, max_population, max_year = 0, 0, 0
        for year, value in dates:
            population += value
            if population > max_population:
                max_population = population
                max_year = year

        return max_year