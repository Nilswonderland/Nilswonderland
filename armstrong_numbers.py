number = int(input("Please enter a number: ")) 
check = len(str(number))
sum = 0

if number is float :
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
elif number <= 0 :
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
elif number is str :
  print("It is an invalid entry. Don't use non-numeric, float, or negative values!")


armstrong_number = number 
while armstrong_number > 0 :
  digit = armstrong_number % 10
  sum += digit ** check
  armstrong_number //= 10 

if number == sum:
  print(number, "is an Armstrong number")
else:
  print(number, "is not an Armstrong number")