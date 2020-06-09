Feature: The calculator

Scenario Outline: Get sum total
  Given a <values> to sum
  When the calculator sums the values
  Then the <total> of sum is correct

  Examples: values
  | values         | total |
  | 5,7            | 12    |
  | 5,3            | 8     |
  | 15,33          | 48    |
  | 33,15          | 48    |
  | 23,10          | 33    |
