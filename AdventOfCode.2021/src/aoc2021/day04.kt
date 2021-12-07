package aoc2021

class BingoBoard(var board: Array<IntArray>) {
    var selections = Array(board.size) { _ -> IntArray(board.first().size) }
    var hasWon = false

    companion object {
        fun parseMany(input: List<String>): Array<BingoBoard> {
            val bingoBoards = ArrayList<BingoBoard>()

            var index = 2
            while (index < input.size) {
                val boardInput = input.slice(index until index + 5)
                    .map { it.trim().split("\\s+".toRegex()).map { i -> i.toInt() }.toIntArray() }
                    .toTypedArray()
                bingoBoards.add(BingoBoard(boardInput))
                index += 6
            }

            return bingoBoards.toTypedArray()
        }
    }

    fun addSelection(num: Int) {
        val coord = coordOf(num)
        if (coord.first == -1 || coord.second == -1) return
        selections[coord.first][coord.second] = 1
    }

    fun checkWinCondition(): Boolean {
        var hasWon = false
        if (checkRows()) hasWon = true
        else if (checkColumns()) hasWon = true

        if (hasWon) this.hasWon = true

        return hasWon
    }

    fun allUnselectedValues(): IntArray {
        val unselected = ArrayList<Int>()
        for (i in selections.indices) {
            for (j in selections[i].indices) {
                if (selections[i][j] == 0)
                    unselected.add(board[i][j])
            }
        }

        return unselected.toIntArray()
    }

    private fun coordOf(num: Int): Pair<Int, Int> {
        for (i in board.indices) {
            for (j in board[i].indices) {
                if (board[i][j] == num) {
                    return Pair(i, j)
                }
            }
        }

        return Pair(-1, -1)
    }

    private fun checkRows(): Boolean {
        for (i in selections.first().indices) {
            var checked = true
            for (j in selections.indices) {
                checked = checked && selections[i][j] == 1
            }

            if (checked) return true
        }

        return false
    }

    private fun checkColumns(): Boolean {
        for (i in selections.first().indices) {
            var checked = true
            for (j in selections.indices) {
                checked = checked && selections[j][i] == 1
            }

            if (checked) return true
        }

        return false
    }
}

fun main() {
    val input = AOCInputReader.readDay(4)

    val drawnNumbers = input.first().split(",").map { it.toInt() }.toIntArray()
    val bingoBoards = BingoBoard.parseMany(input)
    println("Parsed ${bingoBoards.size} Boards")

    // Game loop
    var winningBoards = 0
    for (i in 0 until drawnNumbers.lastIndex) {
        for (j in bingoBoards.indices) {
            val board = bingoBoards[j]
            if (board.hasWon) continue

            board.addSelection(drawnNumbers[i])
            if (board.checkWinCondition()) {
                println("Winner! $j $board")
                val score = board.allUnselectedValues().sum() * drawnNumbers[i]
                println(score)
                winningBoards++
            }

            if (winningBoards == bingoBoards.size) {
                return
            }
        }
    }
}
