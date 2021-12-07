package day03

import (
	"fmt"

	"github.com/willoughbyb/adventofcode.2020/common"
)

// Point is a coordinate
type Point struct {
	X int
	Y int
}

// Do is the main entry point
func Do() {
	input := common.GetInput("day03/input")

	slopes := []Point{
		Point{X: 1, Y: 1},
		Point{X: 3, Y: 1},
		Point{X: 5, Y: 1},
		Point{X: 7, Y: 1},
		Point{X: 1, Y: 2},
	}

	treeCount := 1
	for i := 0; i < len(slopes); i++ {
		treeCount *= countTreesForSlope(input, &slopes[i])
	}
	fmt.Println("Tree Count:", treeCount)
}

func countTreesForSlope(geology []string, slope *Point) int {
	point := Point{X: 0, Y: 0}

	treeCount := 0
	for point.Y < len(geology) {
		row := geology[point.Y]

		if row[point.X] == '#' {
			treeCount++
		}

		point.X += slope.X
		point.Y += slope.Y

		if point.X >= len(row) {
			point.X = point.X % len(row)
		}
	}

	return treeCount
}

func printMap(geology []string, coord *Point) {
	fmt.Println("--------------------------------------------------------------------------------")
	for i := 0; i < len(geology); i++ {
		for j := 0; j < len(geology[i]); j++ {
			if i == coord.Y && j == coord.X {
				fmt.Print("O")
			} else {
				fmt.Print(string(geology[i][j]))
			}
		}
		fmt.Println()
	}
	fmt.Scanln()
}
