# From a file containing numbers separated by comma, print the count of even numbers.
count = 0
with open("practice.txt", "r") as f:
  data = f.read()
  print(data)  #since all the data is in string 1. we will take out individual number 2.then we will parse /casting to int
  """ basic way
  num = ""
  for i in range(len(data)):
    if(data[i] == ","):
      print(int(num))
      num =""
    else:
      num += data[i]
          """
  nums = data.split(",")
  for val in nums:
    if(int(val) % 2 == 0):
      count += 1
print(count)

    



