package main

import (
    "testing"
    "github.com/stretchr/testify/assert"
)

type Parameters struct {
    n int
    expected int
}

var test_params = []Parameters{
    {4, 4},
    {5, 7},
    {25, 1389537},
}

func TestBottomUp(t *testing.T) {
    for _, p := range test_params {
        result := bottomUp(p.n)

        assert.Equal(t, p.expected, result)
    }
}

func bottomUp(n int) int {
    // base case
    if n == 0 {
        return 0
    } else if n == 1 || n == 2 {
        return 1
    }

    memo := make([]int, n+1)
    memo[1] = 1
    memo[2] = 1

    for i := 3; i <= n; i++ {
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    }

    return memo[n]
}