package day01

import (
	"fmt"
	"strconv"

	"github.com/willoughbyb/adventofcode.2020/common"
)

// Do is the main entry point for the module
func Do() {
	lines := common.GetInput("day01/input")

	for i := 0; i < len(lines); i++ {
		a, _ := strconv.ParseInt(lines[i], 10, 32)

		for j := 0; j < len(lines); j++ {
			if j == i {
				continue
			}
			b, _ := strconv.ParseInt(lines[j], 10, 32)

			for k := 0; k < len(lines); k++ {
				if k == i || k == j {
					continue
				}

				c, _ := strconv.ParseInt(lines[k], 10, 32)

				if a+b+c == 2020 {
					fmt.Println(a, b, c, a*b*c)
					return
				}
			}
		}
	}
}
