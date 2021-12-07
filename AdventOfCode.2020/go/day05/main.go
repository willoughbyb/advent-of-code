package day05

import (
	"fmt"
	"sort"

	"github.com/willoughbyb/adventofcode.2020/common"
)

// Do ...
func Do() {
	input := common.GetInput("day05/input")
	fmt.Println("Hello from Day 05")

	var seats []int

	maxSeat := 0
	for i := 0; i < len(input); i++ {
		row := getInt(input[i][:7], 127)
		col := getInt(input[i][7:], 7)
		seat := (row * 8) + col
		seats = append(seats, seat)

		fmt.Println(input[i], row, col, "->", seat)

		if seat > maxSeat {
			maxSeat = seat
		}
	}
	sort.Ints(seats)

	fmt.Println("MaxSeat", maxSeat)
	fmt.Println(seats)

	mySeat := findEmptySeat(seats)
	fmt.Println("MySeat", mySeat)
}

func getInt(input string, max int) int {
	lower := 0
	upper := max

	for _, c := range input {
		ch := string(c)
		delta := ((upper - lower) / 2) + 1
		if ch == "F" || ch == "L" {
			upper -= delta
		} else if ch == "B" || ch == "R" {
			lower += delta
		}
	}

	if upper != lower {
		fmt.Println("upper", upper, "lower", lower)
		panic("upper != lower")
	}

	return upper
}

func findEmptySeat(seats []int) int {
	for i := 1; i < len(seats); i++ {
		a := seats[i-1]
		b := seats[i]
		if b-a > 1 {
			fmt.Println(a, b)
			return a + 1
		}
	}

	return -1
}
