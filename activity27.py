print("Adding Data to dictionary")
print("============================")
empty_dictionary = {}


def print_anime():
    for i, j in empty_dictionary.items():
        print(f"code = {i}  title = {j}")

def search_anime(ij):
    print("Searching anime in dictionary")
    if ij in empty_dictionary:
        print(f"result shows {empty_dictionary[ij]}")
    else:
        print("Anime not found.")
    

while True:
    keys = input("keys for this anime ---> ")
    value = input("enter the anime title ---> ")

    empty_dictionary[keys] = value

    choice = input("What would you like to do next?\n y = continue adding\n n = exit\n p = print anime list\n s = search anime ---> ").lower()

    if choice == 'y':
        print('Continuing...')
        continue

    elif choice == "n":
        print("Exiting.")
        break

    elif choice == "p":
        print_anime()
        continue

    elif choice == "s":
        search = input("Enter the key to search for: ")
        search_anime(search)
        continue

    else:
        print("Invalid input, please try again.")
    