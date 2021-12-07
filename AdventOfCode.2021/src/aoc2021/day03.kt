package aoc2021

fun getUniqueCounts(input: Array<IntArray>): Array<HashMap<Int, Int>> {
    val length = input[0].size
    val counts = Array(length) { _ -> HashMap<Int, Int>() }

    for (line in input) {
        for (i in 0 until length) {
            val v = line[i]
            val count = counts[i]
            count[v] = count[v]?.let { it + 1 } ?: 1
        }
    }

    return counts
}

fun getGammaRate(input: Array<IntArray>): IntArray {
    val length = input[0].size
    val counts = getUniqueCounts(input)
    val result = IntArray(length)

    // get most common bits for each position
    for (i in 0 until length) {
        result[i] = counts[i].maxByOrNull { e -> e.value }?.key ?: 0
        val duplicates = counts[i].filter { e -> e.value == counts[i][result[i]] }
        if (duplicates.size > 1) {
            result[i] = 1
        }
    }

    return result
}

fun getEpsilonRate(input: Array<IntArray>): IntArray {
    val length = input[0].size
    val counts = getUniqueCounts(input)
    val result = IntArray(length)

    // get least common bits for each position
    for (i in 0 until length) {
        result[i] = counts[i].minByOrNull { e -> e.value }?.key ?: 1
        val duplicates = counts[i].filter { e -> e.value == counts[i][result[i]] }
        if (duplicates.size > 1) {
            result[i] = 0
        }
    }

    return result
}

fun getOxygenGeneratorRating(input: Array<IntArray>): IntArray {
    var gamma = getGammaRate(input)[0]
    var results = input.filter { arr -> arr[0] == gamma }

    var index = 1
    do {
        gamma = getGammaRate(results.toTypedArray())[index]
        results = results.filter { arr -> arr[index] == gamma }
        index++
    } while (results.size > 1)

    return results[0]
}

fun getCO2ScrubRating(input: Array<IntArray>): IntArray {
    var epsilon = getEpsilonRate(input)[0]
    var results = input.filter { arr -> arr[0] == epsilon }

    var index = 1
    do {
        epsilon = getEpsilonRate(results.toTypedArray())[index]
        results = results.filter { arr -> arr[index] == epsilon }
        index++
    } while (results.size > 1)

    return results[0]
}

fun main() {
    val input = AOCInputReader.readDay(3)
        .map { it.toCharArray().map { i -> i.toString().toInt() }.toIntArray() }
        .toTypedArray()

    val gammaRate = getGammaRate(input)
    val gammaRateStr = gammaRate.joinToString(separator = "")
    println("Gamma Rate:   $gammaRateStr - ${gammaRateStr.toInt(2)}")

    val epsilonRate = getEpsilonRate(input)
    val epsilonRateStr = epsilonRate.joinToString(separator = "")
    println("Epsilon Rate: $epsilonRateStr - ${epsilonRateStr.toInt(2)}")

    println("Consumption:  ${gammaRateStr.toInt(2) * epsilonRateStr.toInt(2)}")

    val oxyGenRating = getOxygenGeneratorRating(input)
    val oxyGenRatingStr = oxyGenRating.joinToString(separator = "")
    println("OGR:          $oxyGenRatingStr - ${oxyGenRatingStr.toInt(2)}")

    val co2ScrubRating = getCO2ScrubRating(input)
    val co2ScrubRatingStr = co2ScrubRating.joinToString(separator = "")
    println("CO2 Scrub:    $co2ScrubRatingStr - ${co2ScrubRatingStr.toInt(2)}")

    println("Life Support: ${oxyGenRatingStr.toInt(2) * co2ScrubRatingStr.toInt(2)}")
}
