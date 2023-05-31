class UndergroundSystem:
  
    def __init__(self):
        self.check_in_data = {}
        self.journey_data = collections.defaultdict(lambda: [0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName, t]

    def checkOut(self, id: int, end_station: str, t: int) -> None:
        start_station, start_time = self.check_in_data.pop(id)
        self.journey_data[(start_station, end_station)][0] += (t - start_time)
        self.journey_data[(start_station, end_station)][1] += 1
    
    def getAverageTime(self, start_station: str, end_station: str) -> float:
        total_time, total_trips = self.journey_data[(start_station, end_station)]
        return total_time / total_trips