package aoc2021

fun main() {
    val input = AOCInputReader.readDay(1).map { it.toInt() }

    var increaseCount = 0
    var windowIncreaseCount = 0
    for (i in input.indices) {
        if (i > 0 && input[i] > input[i - 1]) {
            increaseCount++
        }
        if (i >= 3) {
            val window1sum = input[i - 1] + input[i - 2] + input[i - 3]
            val window2sum = input[i - 0] + input[i - 1] + input[i - 2]
            if (window2sum > window1sum) {
                windowIncreaseCount++
            }
        }
    }
    println()

    println("Increases: $increaseCount")
    println("Window Increases: $windowIncreaseCount")
}
