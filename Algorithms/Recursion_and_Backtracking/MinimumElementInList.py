def find_min(my_list):
  if len(my_list) == 0:
    return None
  if len(my_list) == 1:
    return my_list[0]
  #compare the first 2 elements
  temp = my_list[0] if my_list[0] < my_list[1] else my_list[1]
  my_list[1] = temp
  return find_min(my_list[1:])

print(find_min([]))
print(find_min([42, 17, 2, -1, 67]))
print(find_min([10, 10, 10, 10]))