print("Function Activity\n"
      "Created by: Nikolai Salvador and Nathaniel Rosell Beatisula")
print()

number_one = int(input("Input the first number: "))
number_two = int(input("Input the second number: "))
number_three = int(input("Input the third number: "))
print()


def applicationfunc(wan, too, tree):
       x = 0
       if wan == too and wan == tree:
              x = wan * too * tree
       elif wan == too and wan != tree:
              x = wan * too + tree
       elif wan != too and wan == tree:
              x = wan * tree + too
       elif wan != too and too == tree:
              x = wan + too * tree
       elif wan != too and wan != tree:
              x = wan + too + tree
       print(f"Result is {x}")


applicationfunc(number_one, number_two, number_three)