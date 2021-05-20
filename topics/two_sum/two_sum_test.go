import(
    "testing"
    "github.com/stretchr/testify/assert"
)

type Parameters struct {
    nums []int
    target int
    expected []int
}

var test_parameters = []Parameters{
    { []int{2, 7, 11, 15}, 9, []int{0,1} },
    { []int{3, 2, 4}, 6, []int{1,2}},
}

func TestTwoSum(t *testing.T) {
    for _, parameters := range test_parameters {
        result := twoSum(parameters.nums, parameters.target)

        assert.Equal(t, result, parameters.expected, "Two slices should be equal")
    }
}

func twoSum(nums []int, target int) []int {
    numsHash := make(map[int]int)
    result := []int{0, 0}

    for i, value := range nums {
        subtraction := target - value

        _, ok := numsHash[subtraction]

        if ok {
            result[0] = numsHash[subtraction]
            result[1] = i            
            
        } else {
            numsHash[value] = i
        }
    }

    return result
}
