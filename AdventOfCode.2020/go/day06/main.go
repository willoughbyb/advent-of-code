package day06

import (
	"fmt"
	"strings"

	"github.com/willoughbyb/adventofcode.2020/common"
)

// Do ...
func Do() {
	input := common.GetInputDoubleNewline("day06/input")

	sumUnique := 0
	sumSame := 0
	for _, data := range input {
		unique := countUniqueAnswers(data)
		same := countSameAnswers(data)

		fmt.Println(data, unique, same)
		sumUnique += unique
		sumSame += same
	}

	fmt.Println("unique", sumUnique, "same", sumSame)
}

func countUniqueAnswers(line string) int {
	letterMap := mapString(line)
	return len(letterMap)
}

func countSameAnswers(line string) int {
	groupSize := len(strings.Split(line, " "))
	letterMap := mapString(line)

	count := 0
	for _, v := range letterMap {
		if v == groupSize {
			count++
		}
	}
	return count
}

func mapString(line string) map[string]int {
	letterMap := make(map[string]int)
	for _, s := range line {
		letterMap[string(s)]++
	}
	delete(letterMap, " ")

	return letterMap
}
