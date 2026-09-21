/*

    43. Multiply Strings

    Given two non-negative integers
    num1 and num2 represented as strings,
    return the product of num1 and num2,
    also represented as a string.

    Note: You must not use any built-in
    BigInteger library or convert the
    inputs to integer directly.

    Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"

    Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"

    Constraints:
    1 <= num1.length, num2.length <= 200
    num1 and num2 consist of digits only.
    Both num1 and num2 do not contain
    any leading zero, except the number
    0 itself.

*/

// Brute Force
func multiply(num1 string, num2 string) string {

    // Multiply
    individualProds := []string{}
    for i := len(num1) - 1; i > -1; i-- {
        carry, row := 0, ""
        for j := len(num2) - 1; j > -1; j-- {
            rowProd := carry + int(num1[i]-'0') * int(num2[j]-'0')
            d := rowProd % 10
            carry = rowProd / 10
            row += string(d + '0')
        }
        if carry > 0 {
            row += string(carry + '0')
        }

        row = reverse(row)
        for cnt := i; cnt < len(num1) - 1; cnt++ {
            row += "0"
        }

        individualProds = append(individualProds, row)
    }

    // Add
    prod := "0"
    for _, p := range individualProds {
        prod = addNumbers(prod, p)
    }

    // Strip leading zeros (but keep at least one digit)
    i := 0
    for i < len(prod)-1 && prod[i] == '0' {
        i++
    }

    return prod[i:]
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }

    return string(runes)
}

func addNumbers(a, b string) string {
    // Make equal lengths
    if len(a) > len(b) {
        b = reverse(b)
        for range len(a) - len(b) {
            b += "0"
        }
        b = reverse(b)
    } else if len(b) > len(a) {
        a = reverse(a)
        for range len(b) - len(a) {
            a += "0"
        }
        a = reverse(a)
    }

    res := ""
    carry := 0
    for i := len(a) - 1; i > -1; i-- {
        sum := carry + int(a[i]-'0') + int(b[i]-'0')
        res += string(sum % 10 + '0')
        carry = sum / 10
    }

    if carry > 0 {
        res += string(carry + '0')
    }

    return reverse(res)
}

