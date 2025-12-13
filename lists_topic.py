

# 1. Content from activity23.py (Core List Methods and Traversal)
def demo_list_methods():
    print("List Demo 1: Core List Methods")
    
    # 1. Initial List and Creation
    months = ['jan','Feb','Mar','Apr','May','Jun','Jul']
    print(f"Initial List: {months}")
    
    # 2. .append()
    months.append('Aug')
    print(f"After .append('Aug'): {months}")
    
    # 3. .pop()
    months.append('Sept')
    print(f"Adding 'Sept' before popping: {months}")
    months.pop()
    print(f"After .pop() (removed Sept): {months}")
    
    # 4. .remove()
    print("Attempting to remove 'Mar'...")
    try:
        months.remove("Mar")
        print(f"After .remove('Mar'): {months}")
    except ValueError:
        print("Error: 'Mar' not found (it might be 'Mar' or 'mar').")
    
    # 5. .insert()
    months.insert(2, "Oct")
    print(f"After .insert(2, 'Oct'): {months}")
    
    # 6. len() function
    len_list = len(months)
    print(f"Length of the list (len()): {len_list}")
    
    # 7. .sort()
    months.sort()
    print(f"After .sort(): {months}")
    
    # 8. Traversal / Iteration
    print("\nTraversing the list using a for loop:")
    for m in months:
        print(f"--> {m}")
        
    # 9. List Slicing (Bonus from activity23)
    dummy_string = 'Dummy name'
    print(f"\nString slicing (reversing '{dummy_string}'): {dummy_string[::-1]}")
    print("=" * 40)

# 2. Content from code_challange15.py (Interactive List Application)
def demo_anime_list_builder():
    print("List Demo 2: Anime List Builder (List + Loop Application)")
    anime_list = []
    
    while True:
        anime = input("Enter an anime title (type 'exit' to finish): ").strip()

        if anime.lower() == 'exit':
            print("Finished adding titles.")
            break
        
        if anime: # Check if input is not empty
            anime_list.append(anime)
            print(f"'{anime}' successfully added.")
        
    print("\n=============================")
    print("Your Final Anime List:")
    print("=============================")
    
    if anime_list:
        for index, title in enumerate(anime_list, 1):
            print(f"{index}. {title}")
    else:
        print("The list is empty.")
    
    print("=" * 40)


# MASTER FUNCTION: Run all demos for the main menu Topic 6 selection
def run_topic_6_all():
    print("\n" + "="*50)
    print("TOPIC 6: LISTS DEMONSTRATION")
    print("="*50)
    
    demo_list_methods()
    demo_anime_list_builder()

    print("\n" + "="*50)
    print("Lists and associated methods demonstrated.")
    print("="*50)
    

def check_item_in_list(search_item, test_list):
    if search_item in test_list:
        return f"'{search_item}' was FOUND in the list."
    else:
        return f"'{search_item}' was NOT FOUND in the list."