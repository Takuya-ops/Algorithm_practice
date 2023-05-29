class ParkingSystem(_big: Int, _medium: Int, _small: Int) {
    var bigLimit: Int = _big
    var mediumLimit: Int = _medium
    var smallLimit: Int = _small

    var parkingArray: Array[Int] = Array.fill(bigLimit + mediumLimit + smallLimit)(-1)

    def addCar(carType: Int): Boolean = {
        var limit = 0
        if (carType == 1) {
            limit = bigLimit
        } else if (carType == 2) {
            limit = mediumLimit
        } else {
            limit = smallLimit
        }
        var count = 0
        for (i <- 0 until bigLimit + mediumLimit + smallLimit) {
            if (parkingArray(i) == carType) {
                count += 1
            }
            if (count == limit) {
                return false
            }
            if (parkingArray(i) == -1) {
                parkingArray(i) = carType
                return true
            }
        }
        return false
    }
}