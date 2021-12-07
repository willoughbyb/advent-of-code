package aoc2021

import java.io.File
import java.lang.Exception

class AOCInputReader {
    companion object {
        fun readDay(day: Int): List<String> {
            val file = File("input/day${day.toString().padStart(2, '0')}.txt")
            if (file.exists()) {
                return file.useLines { it.toList() }
            }

            throw Exception("Unable to get input for: ${file.name}")
        }
    }
}
