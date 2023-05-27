# ---------------------------------------------------------------- Debugging

############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
# #   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# range does not include the 20, it should be set to 21, so it could print the expected outcome




# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# # dice_num = randint(0, 5)
# print(dice_imgs[dice_num])


# The randint is set to index but max list index is 5, not 6, and 1 should be 0 in order to get the fist item



# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
# # elif year >= 1994:
#   print("You are a Gen Z.")


# 1994 was never hit as we have a <1994> but never ==





# # Fix the Errors
# age = input("How old are you?")
# # age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")
# # if age > 18:
# #    print(f"You can drive at age {age}.")

# no indentation and the input is str that we check with int later on, and no f string on the print statement


# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# # word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# word_per_page has == input but not = so the word_per_page = 0 which we use for total_words, and we get 0 at the end



# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#     # b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])
#

# wrong indentation of b_list.append(new_item)

