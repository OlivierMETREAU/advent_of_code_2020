import itertools

def multiply_list(input_list):
   result = 1
   for x in input_list:
      result = result * x
   return result
   
def day1(list_of_expenses, order=2):
   combinations = list(itertools.combinations(list_of_expenses, order))
   sums = [sum(x) for x in combinations]
   for i in range(len(sums)):
      if sums[i] == 2020:
         print(combinations[i])
         return multiply_list(combinations[i])

def main():
   f = open("input_day1.txt", "r")
   lines = f.readlines()
   lines = [int(x.strip()) for x in lines]
   print(day1(lines, order=3))

if __name__ == "__main__":
   main()

