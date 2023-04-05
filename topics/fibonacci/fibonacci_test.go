package main

import (
    "testing"
    "github.com/stretchr/testify/assert"
)

type Parameters struct {
    n int
    expected int
}

var test_parameters = []Parameters{
    {2, 1},
    {3, 2},
    {4, 3},
    {5, 5},
    {6, 8},
}

func TestRecursion(t *testing.T) {
    for _, parameters := range test_parameters {
        result := fibRecursion(parameters.n)

        assert.Equal(t, parameters.expected, result)
    }
}

func TestBottomUp(t *testing.T) {
    for _, parameters := range test_parameters {
        result := fibBottomUp(parameters.n)

        assert.Equal(t, parameters.expected, result)
    }
}

func TestTopDown(t *testing.T) {
    for _, parameters := range test_parameters {
        result := fibTopDown(parameters.n)

        assert.Equal(t, parameters.expected, result)
    }
}

func fibRecursion(N int) int {
    if N <= 1 {
        return N
    }

    return fibRecursion(N-1) + fibRecursion(N-2)
}

func fibBottomUp(N int) int {
    if N <= 1 {
        return N
    }

    cache := make([]int, N + 1)
    cache[1] = 1

    for i := 2; i <= N; i++ {
        cache[i] = cache[i-1] + cache[i-2]
    }

    return cache[N]
}

var cache = map[int]int{0:0, 1:1}
func fibTopDown(N int) int {
    if _, ok := cache[N]; ok {
        return cache[N]
    }

    cache[N] = fibTopDown(N-1) + fibTopDown(N-2)

    return cache[N]
}