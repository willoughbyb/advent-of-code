package aoc2021

data class Position(var horizontal: Int, var depth: Int, var aim: Int)

fun main() {
    val position = Position(0, 0, 0)
    val input = AOCInputReader.readDay(2)

    input.forEach {
        val cmd = it.split(' ')[0]
        val amt = it.split(' ')[1].toInt()

        when (cmd) {
            "forward" -> {
                position.horizontal += amt
                position.depth += position.aim * amt
            }
            "down" -> position.aim += amt
            "up" -> position.aim -= amt
        }
    }

    println(position)
    println(position.depth * position.horizontal)
}