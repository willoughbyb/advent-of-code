package common

import (
	"io/ioutil"
	"strings"
)

// GetInput returns the contents of the given file split on newline
func GetInput(filename string) []string {
	dat, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(dat), "\n")
	return lines
}

// GetInputDoubleNewline ...
func GetInputDoubleNewline(filename string) []string {
	dat, err := ioutil.ReadFile(filename)
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(dat), "\n\n")
	for i := 0; i < len(lines); i++ {
		lines[i] = strings.ReplaceAll(lines[i], "\n", " ")
	}

	return lines
}

// ContainsInt ...
func ContainsInt(array []int, value int) bool {
	for _, val := range array {
		if val == value {
			return true
		}
	}
	return false
}
