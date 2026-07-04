class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(reverse=True)

        for i in range(len(cars)):
            time = (target - cars[i][0]) / cars[i][1]
            if i == 0:
                times = [time]
                continue
            times.append(time)

        fleet = []  # stack
        for i in range(len(times)):
            if i != 0 and times[i] <= fleet[-1]:
                continue
            fleet.append(times[i])
        return len(fleet)