package main

import(
    "testing"
    "github.com/stretchr/testify/assert"
)

type Parameters struct {
	numbers []int
	expected int
}

var test_parameters_highest = []Parameters{
	{ []int{1,2,3,4,5}, 5 },
	{ []int{9,8,7,6,5}, 9 },
}

var test_parameters_lowest = []Parameters{
	{ []int{1,2,3,4,5}, 1 },
	{ []int{9,8,7,6,5}, 5 },
}

func TestHighestNumber(t *testing.T) {
	for _, parameters := range test_parameters_highest {
		result := highestNumber(parameters.numbers)

		assert.Equal(t, parameters.expected, result)
	}
}

func TestLowestNumber(t *testing.T) {
	for _, parameters := range test_parameters_lowest {
		result := lowestNumber(parameters.numbers)

		assert.Equal(t, parameters.expected, result)
	}
}


func highestNumber(numbers []int) int {
	var highest int
	highest = numbers[0]

	for _, number := range numbers {
		if number > highest {
			highest = number
		}
	}

	return highest
}

func lowestNumber(numbers []int) int {
	var lowest int
	lowest = numbers[0]

	for _, number := range numbers {
		if number < lowest {
			lowest = number
		}
	}

	return lowest
}