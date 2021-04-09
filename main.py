items = ['In', 'God', 'we', 'trust']
for (index, elem) in enumerate(items):
  items[index] = elem + '!'

print(items)



def find_index(symbol, elements):
  """
  The function returns the index of the first element of the iterated sequence, equal to the given argument
  """
  ind = None
  for (index, elem) in enumerate(elements):
    if symbol == elem:
      ind = index
      break
  return ind


# the 2nd version
  def find_index(value, items):
    for index, item in enumerate(items):
        if item == value:
            return index