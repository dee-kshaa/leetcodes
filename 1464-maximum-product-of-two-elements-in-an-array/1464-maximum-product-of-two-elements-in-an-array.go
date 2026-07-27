func maxProduct(nums []int) int {

    first := 0

    second := 0

    for _, num := range nums {

        if num >= first {

            second = first

            first = num

        } else if num > second {
            second = num
        }
    }

    return (first - 1) * (second - 1)
}