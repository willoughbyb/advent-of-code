package day08

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/willoughbyb/adventofcode.2020/common"
)

var (
	accumulator int
	pointer     int
	history     []int
)

// Do ...
func Do() {
	input := common.GetInput("day08/input")

	accumulator = 0
	pointer = 0

	for pointer < len(input) {
		instruction := input[pointer]
		fmt.Println("instruction:", instruction)

		parts := strings.Split(instruction, " ")
		value, _ := strconv.Atoi(parts[1])

		checkHistory()
		exec(parts[0], value)
	}
	fmt.Println("Program Exited", accumulator)
}

func checkHistory() {
	if common.ContainsInt(history, pointer) {
		fmt.Println("accumulator", accumulator)
		panic("command already performed")
	}
	history = append(history, pointer)
}

func exec(command string, value int) {
	switch command {
	case "acc":
		accumulator += value
		pointer++
	case "nop":
		pointer++
	case "jmp":
		pointer += value
	}
}
