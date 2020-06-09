Feature: Microservicios

Scenario Outline: Get sum total
  Given a <values> to sum
  When the calculator sums the values
  Then the <total> of sum is correct

  Examples: values
  | num1 | num2 | total |
  | 5    | 7    | 12    |
  | 5    | 3    | 8     |
  | 15   | 33   | 48    |
  | 33   | 15   | 48    |
  | 23   | 10   | 33    |

Scenario Outline: Get substraction total
  Given a <values> to substract
  When the calculator substract the values
  Then the <total> of substraction is correct

  Examples: values
  | num1 | num2 | total |
  | 5    | 7    | -2    |
  | 5    | 3    | 2     |
  | 115  | 30   | 85    |

Scenario Outline: Get product total
  Given a <values> to multiply
  When the calculator multiply the values
  Then the <total> of multiply is correct

  Examples: values
  | num1 | num2 | total |
  | 5    | 2    | 10    |
  | 5    | 3    | 15    |
  | 3    | 5    | 15    |

  Scenario Outline: Get division total
    Given a <values> to divide
    When the calculator divide the values
    Then the <total> of divide is correct

    Examples: values
    | num1 | num2 | total |
    | 10   | 2    | 5     |
    | 51   | 3    | 17    |
    | 12   | 6    | 2     |
    | 120  | 5    | 24    |
    | 5    | 2    | 2     |
