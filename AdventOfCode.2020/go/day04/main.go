package day04

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"

	"github.com/willoughbyb/adventofcode.2020/common"
)

// Validator ...
type Validator func(input string) bool

// Rule ...
type Rule struct {
	Code      string
	Strict    bool
	Validator Validator
}

// IsValid ...
func (rule Rule) IsValid(input string) bool {
	index := strings.Index(input, rule.Code)

	if index == -1 && rule.Strict {
		return false
	}

	if rule.Validator != nil {
		value := input[index:]
		colonIndex := strings.Index(value, ":")
		spaceIndex := strings.Index(value, " ")

		if spaceIndex == -1 {
			value = value[colonIndex+1:]
		} else {
			value = value[colonIndex+1 : spaceIndex]
		}

		return rule.Validator(value)
	}

	return true
}

// Engine ...
type Engine struct {
	Rules []Rule
}

// Satisfies ...
func (engine Engine) Satisfies(input string) bool {
	for i := 0; i < len(engine.Rules); i++ {
		isValid := engine.Rules[i].IsValid(input)
		if isValid == false {
			fmt.Println("Match fails", engine.Rules[i].Code)
			return false
		}
	}

	return true
}

// Do is the entry point
func Do() {
	input := common.GetInput("day04/input")
	passports := parsePassports(input)

	between := func(val int, min int, max int) bool {
		return val >= min && val <= max
	}

	regex := func(r string, s string) bool {
		matched, err := regexp.MatchString(r, s)
		if err != nil {
			return false
		}

		return matched
	}

	height := func(s string) bool {
		var unitIndex int

		unitIndex = strings.Index(s, "cm")
		if unitIndex > -1 {
			centimeters, _ := strconv.Atoi(s[:unitIndex])
			return between(centimeters, 150, 193)
		}

		unitIndex = strings.Index(s, "in")
		if unitIndex > -1 {
			inches, _ := strconv.Atoi(s[:unitIndex])
			return between(inches, 59, 76)
		}

		return false
	}

	inArray := func(arr []string, val string) bool {
		for i := 0; i < len(arr); i++ {
			if arr[i] == val {
				return true
			}
		}
		return false
	}

	validColors := []string{
		"amb", "blu", "brn", "gry", "grn", "hzl", "oth",
	}

	rules := []Rule{
		Rule{Code: "byr", Strict: true, Validator: func(s string) bool {
			val, _ := strconv.Atoi(s)
			return between(val, 1920, 2002)
		}},
		Rule{Code: "iyr", Strict: true, Validator: func(s string) bool {
			val, _ := strconv.Atoi(s)
			return between(val, 2010, 2020)
		}},
		Rule{Code: "eyr", Strict: true, Validator: func(s string) bool {
			val, _ := strconv.Atoi(s)
			return between(val, 2020, 2030)
		}},
		Rule{Code: "hgt", Strict: true, Validator: height},
		Rule{Code: "hcl", Strict: true, Validator: func(s string) bool {
			return regex(`^#[a-fA-F0-9]{6}$`, s)
		}},
		Rule{Code: "ecl", Strict: true, Validator: func(s string) bool {
			return inArray(validColors, s)
		}},
		Rule{Code: "pid", Strict: true, Validator: func(s string) bool {
			return regex(`^[0-9]{9}$`, s)
		}},
		Rule{Code: "cid", Strict: false},
	}

	engine := Engine{Rules: rules}

	totalSatisfies := 0
	for i := 0; i < len(passports); i++ {
		fmt.Println("Checking ", passports[i])
		if engine.Satisfies(passports[i]) {
			// fmt.Println("Yes")
			totalSatisfies++
			// } else {
			// 	fmt.Println("No")
		}
	}

	fmt.Println("Total Satisfies:", totalSatisfies)
}

func parsePassports(input []string) []string {
	var passports []string

	passport := ""
	for i := 0; i < len(input); i++ {
		line := input[i]
		if line == "" {
			passports = append(passports, strings.Trim(passport, " "))
			passport = ""
		}
		passport += line + " "
	}
	passports = append(passports, strings.Trim(passport, " "))

	return passports
}
