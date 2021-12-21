package aoc2021

import java.util.*
import kotlin.math.floor

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

fun checkCorruption(line: String): Long? {
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
                    return null // -points[closers.indexOf(ch)]
                }
            }
        }
    } while (scanner.hasNext())

    if (chunks.size > 0) {
        println("Chunk is unclosed: $chunks")
        // get closing list
        val closingList = chunks.map { closers[openers.indexOf(it)] }.joinToString("")
        val closingListValue = closingList.toCharArray()
            .fold(0L) { sum, e -> (sum * 5) + (closers.indexOf(e) + 1) }
        println("  to close: $closingListValue -> $closingList")

        return closingListValue
    }
    return 0
}

fun main() {
    val input = AOCInputReader.readDay(10)
    val valids = input.mapNotNull { checkCorruption(it) }
        .sorted()
    println(valids)

    val middleIndex = floor(valids.size / 2.0).toInt()
    println("$middleIndex -> ${valids[middleIndex]}")
}
