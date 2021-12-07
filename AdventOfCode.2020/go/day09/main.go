package day09

import (
	"fmt"
	"strconv"

	"github.com/willoughbyb/adventofcode.2020/common"
)

var (
	preamble int = 25
)

// Do ...
func Do() {
	input := common.GetInput("day09/input")
	var nums []int
	for _, numString := range input {
		num, _ := strconv.Atoi(numString)
		nums = append(nums, num)
	}
	fmt.Println(nums)

	var invalidNum int
	for i := preamble; i < len(nums); i++ {
		isValid := checkIsValid(nums, i-preamble, i-1, nums[i])
		if !isValid {
			invalidNum = nums[i]
			break
		}
	}
	fmt.Println("value", invalidNum, "is not valid")

	for startIndex := 0; startIndex < len(nums); startIndex++ {
		for endIndex := startIndex + 1; endIndex < len(nums); endIndex++ {
			//

		}
	}
}

func checkIsValid(numbers []int, startIndex int, endIndex int, value int) bool {
	fmt.Println("Checking", value, startIndex, endIndex, numbers[startIndex:endIndex+1])
	for i := startIndex; i <= endIndex; i++ {
		for j := startIndex; j <= endIndex; j++ {
			if j == i || numbers[i] == numbers[j] {
				continue
			}

			if numbers[i]+numbers[j] == value {
				return true
			}
		}
	}

	return false
}

func checkContiguous(numbers []int, startIndex int, value int) (int, int) {
	endIndex := startIndex
	total := 0
	for i := startIndex; i < len(numbers); i++ {
		total += numbers[i]

		if total > value {
			return -1, -1
		}
	}
}
