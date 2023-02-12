package main

import(
    "fmt"
//     "testing"
//     "github.com/stretchr/testify/assert"
)

// type Parameters struct {
//     nums []int
//     expected []int
// }
//
// var parameters = []Parameters{
//     {[]int{5, 4, 3, 2, 1}, {1, 2, 3, 4, 5}},
//     {[]int{5, 5, 3, 2, 3}, {2, 3, 3, 5, 5}},
//     {[]int{1, 2, 3, 4, 5}, {1, 2, 3, 4, 5}},
//     {[]int{5, 9, 3, 4, 8, 2, 9, 8}, {2, 3, 4, 5, 8, 8, 9, 9}},
// }

func quickSort(nums []int) ([]int) {
    fmt.Println(nums)
    if len(nums) <= 1 {
        return nums
    }

    var left []int
    var right []int
    var result []int

    pivot := []int{nums[len(nums) - 1]}
    nums = nums[: len(nums) - 1]

    for _, num := range nums {
        if num > pivot[0] {
            right = append(right, num)
        } else {
            left = append(left, num)
        }
    }

    result = append(result, quickSort(right)...)
    result = append(result, pivot...)
    result = append(result, quickSort(left)...)

    return result
}

func main() {
    nums := []int{5,4,3,1}

    fmt.Println(quickSort(nums))
}
