package day02

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/willoughbyb/adventofcode.2020/common"
)

// PasswordPolicy describes the format of the input file
type PasswordPolicy struct {
	Min int
	Max int
	Ch  string
}

// Do is the main entry point for the module
func Do() {
	inputs := common.GetInput("day02/input")

	correctCount := 0
	for i := 0; i < len(inputs); i++ {
		policy := parsePasswordPolicy(inputs[i])
		password := parsePassword(inputs[i])

		if policyIsSatisfied(policy, password) {
			correctCount++
		}
	}

	fmt.Println("Correct Count: ", correctCount)
}

func parsePasswordPolicy(line string) *PasswordPolicy {
	input := line

	dashIndex := strings.Index(input, "-")
	min, _ := strconv.Atoi(input[0:dashIndex])
	input = input[dashIndex+1:]

	spaceIndex := strings.Index(input, " ")
	max, _ := strconv.Atoi(input[0:spaceIndex])
	input = input[spaceIndex+1:]

	colonIndex := strings.Index(input, ":")
	ch := input[0:colonIndex]

	return &PasswordPolicy{Min: min, Max: max, Ch: ch}
}

func parsePassword(line string) string {
	spaceIndex := strings.LastIndex(line, " ")
	return line[spaceIndex+1:]
}

func policyIsSatisfied(policy *PasswordPolicy, password string) bool {
	// Part 1
	// count := strings.Count(password, policy.Ch)
	// return count >= policy.Min && count <= policy.Max

	// Part 2
	minMatch := password[policy.Min-1:policy.Min] == policy.Ch
	maxMatch := password[policy.Max-1:policy.Max] == policy.Ch

	return (minMatch && !maxMatch) || (!minMatch && maxMatch)
}
