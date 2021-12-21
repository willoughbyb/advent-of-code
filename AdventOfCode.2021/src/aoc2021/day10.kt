package aoc2021

import java.util.*

data class Scanner(val input: String, var start: Int = 0, var current: Int = 0) {
    fun next(): Char {
        return input[current++]
    }

    fun hasNext(): Boolean {
        return input.length >= current + 1
    }
}

val openers = charArrayOf('(', '[', '{', '<')
val closers = charArrayOf(')', ']', '}', '>')
val points = intArrayOf(3, 57, 1197, 25137)

fun checkCorruption(line: String): Int {
//    println("Checking $line")
    val scanner = Scanner(line)

    var currentChunkIndex: Int = -1
    val chunks = LinkedList<Char>()
    do {
        val ch = scanner.next()
        when (ch) {
            '(', '[', '{', '<' -> {
                chunks.push(ch)
                currentChunkIndex = openers.indexOf(ch)
            }
            ')', ']', '}', '>' -> {
                if (closers.indexOf(ch) == currentChunkIndex) {
                    chunks.pop()
                    currentChunkIndex = if (chunks.size > 0) {
                        openers.indexOf(chunks.peek())
                    } else -1
                } else {
//                    println("  Corrupted Chunk: found $ch, expected ${closers[currentChunkIndex]}")
                    return points[closers.indexOf(ch)]
                }
            }
        }
    } while (scanner.hasNext())

    if (chunks.size > 0) {
//        println("Chunk is unclosed: $chunks")
    }
    return 0
}

fun main() {
    val input = AOCInputReader.readDay(10)
    val valids = input.groupBy { line -> checkCorruption(line) }
        .mapValues { it.value.size }
        .toList()
        .fold(0) { sum, element -> sum + element.first * element.second }
    println(valids)
}
