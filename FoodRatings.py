import heapq


class FoodRatings:
    def __init__(self, foods, cuisines, ratings):
        self.foods = {
            food: {"cuisine": cuisine, "rating": rating}
            for food, cuisine, rating in zip(foods, cuisines, ratings)
        }
        self.cuisine_max_heap = {}
        for food, info in self.foods.items():
            cuisine = info["cuisine"]
            if cuisine not in self.cuisine_max_heap:
                self.cuisine_max_heap[cuisine] = []
            # Using negative ratings because heapq is a min heap, and we need max heap functionality
            heapq.heappush(self.cuisine_max_heap[cuisine], (-info["rating"], food))

    def changeRating(self, food, newRating):
        cuisine = self.foods[food]["cuisine"]
        # Change the rating in the foods dictionary
        self.foods[food]["rating"] = newRating
        # Add the new rating to the heap (old rating remains but will be ignored in highestRated)
        heapq.heappush(self.cuisine_max_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine):
        # Remove and skip over any food whose current rating doesn't match the one in the heap
        while self.cuisine_max_heap[cuisine]:
            rating, food = self.cuisine_max_heap[cuisine][0]
            if -rating == self.foods[food]["rating"]:
                return food
            heapq.heappop(self.cuisine_max_heap[cuisine])


# Testing the optimized implementation
food_ratings_optimized = FoodRatings(
    ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
    ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
    [9, 12, 8, 15, 14, 7],
)

# Testing the functionality based on the provided example
outputs_optimized = []
outputs_optimized.append(food_ratings_optimized.highestRated("korean"))
outputs_optimized.append(food_ratings_optimized.highestRated("japanese"))
food_ratings_optimized.changeRating("sushi", 16)
outputs_optimized.append(food_ratings_optimized.highestRated("japanese"))
food_ratings_optimized.changeRating("ramen", 16)
outputs_optimized.append(food_ratings_optimized.highestRated("japanese"))

print(outputs_optimized)
