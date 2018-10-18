# ONLY EDIT FUNCTIONS MARKED CLEARLY FOR EDITING

import numpy as np

# modify this function, and create other functions below
def question01(portfolios):
  # modify and then return the variable below
  answer = 0
  return answer

# example
portfolios = [15,8,6,7]
portfolios[-1]

format(8, "b")

# using list comprehensions
port_bi = [format(x, "b") for x in portfolios]
port_bi

lengths = [len(x) for x in port_bi]
max(lengths)


# leading priority: the first element in the combined portfolio should be 1
# pick out the portfolio pairs that meets this condition to narrow down the candidates
