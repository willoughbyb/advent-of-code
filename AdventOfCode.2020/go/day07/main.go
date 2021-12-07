package day07

import (
	"fmt"
	"regexp"
	"strconv"

	"github.com/willoughbyb/adventofcode.2020/common"
)

// Rule ...
type Rule struct {
	Name         string
	Dependencies map[string]int
}

// Do ...
func Do() {
	input := common.GetInput("day07/input")

	var rules []*Rule
	for _, line := range input {
		rule := parseRule(line)
		fmt.Println("Parsing Rule:", line, "\n  ", rule)
		rules = append(rules, rule)
	}

	deps := getParents(rules, "shiny gold")

	// get unique dependencies
	depMap := make(map[string]int)
	for _, dep := range deps {
		depMap[dep.Name]++
	}

	fmt.Println("# Dependencies:", len(depMap), depMap)

	childrenCount := getChildrenCount(rules, "shiny gold")
	fmt.Println("# children:", childrenCount)
}

func parseRule(input string) *Rule {
	nameRegex, _ := regexp.Compile(`^([\w\s]+) bags? contain`)
	dependencyRegex, _ := regexp.Compile(`(\d+)\s([\w\s]+) bags?`)

	name := nameRegex.FindStringSubmatch(input)[1]
	dependencies := dependencyRegex.FindAllStringSubmatch(input, -1)

	rule := Rule{Name: name, Dependencies: make(map[string]int)}
	for _, dep := range dependencies {
		dNum, _ := strconv.Atoi(dep[1])
		rule.Dependencies[dep[2]] = dNum
	}

	return &rule
}

func getParents(rules []*Rule, targetRuleName string) []*Rule {
	var parents []*Rule
	for _, rule := range rules {
		if _, ok := rule.Dependencies[targetRuleName]; ok {
			parents = append(parents, rule)
		}
	}

	for _, parent := range parents {
		grandparents := getParents(rules, parent.Name)
		parents = append(parents, grandparents...)
	}

	return parents
}

func getChildrenCount(rules []*Rule, targetRuleName string) int {
	var children []*Rule
	totalCount := 0

	root := getByName(rules, targetRuleName)
	for childName := range root.Dependencies {
		child := getByName(rules, childName)
		children = append(children, child)
	}

	for _, child := range children {
		grandchildrenCount := getChildrenCount(rules, child.Name)

		totalCount += root.Dependencies[child.Name]
		if grandchildrenCount > 0 {
			totalCount += root.Dependencies[child.Name] * grandchildrenCount
		}
	}

	return totalCount
}

func getByName(rules []*Rule, name string) *Rule {
	for _, rule := range rules {
		if rule.Name == name {
			return rule
		}
	}

	return nil
}
