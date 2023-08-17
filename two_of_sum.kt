package com.algoexpert.program

fun twoNumberSum(array: MutableList<Int>, targetSum: Int): List<Int> {

    val numberSet = HashSet<Int>()

    for (element in array) {
        val expectedPair = targetSum - element
        if (numberSet.contains(expectedPair)) {
            return listOf(element, expectedPair)
        }
        numberSet.add(element)
    }
    return listOf()
}
