#anime listing

# anime_list
#list.append(item)
#for each_language in pl:
#   print(f"I can code using (each_language)")

# name = input("Please enter name: ")

# def greet(name):
#     return f"Hello, {name}!"

# print(greet(name))

# while isODD == True:
#     num = eval(input("Enter number --> "))
#     if num % 2 == 1: 
#         print("ODD number detected")
#         odd += str(num) + ","
#         total_sum += num
#         continue
#     elif num == 0:
#         print("Loop Terminated")
#         isODD = False


def anime_program():
    anime_list = []
    
    while True:
        anime = input("Enter the title of an anime (type 'exit' to finish the list): ")

        if anime.lower() == 'exit':
            print("Program ended.")
            break
        
        anime_list.append(anime)
        print(f"{anime} successfully added to saved.")
        
    print("list of the added anime's: ")
    for anime in anime_list:
        print(anime)

anime_program()
