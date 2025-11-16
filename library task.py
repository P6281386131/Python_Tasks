library = {} 

library["B1"] = {"title": "Python Basics", "author": "John", "year": 2020}
library["B2"] = {"title": "AI Guide", "author": "Smith", "year": 2018}
library.update({"B3": {"title": "Cyber Security", "author": "Alex", "year": 2022}})
library.setdefault("B4", {"title": "Networking Essentials", "author": "David", "year": 2015})
library.setdefault("B5", {"title": "Machine Learning Intro", "author": "Emily", "year": 2021})


print("All Books in Library:")
for key, value in library.items():
    print(key, ":", value)
add_more = input("\nDo you want to add a new book? (yes/no): ").lower()

while add_more == "yes":
    new_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    year = int(input("Enter Published Year: "))

    library[new_id] = {"title": title, "author": author, "year": year}

    print("\nBook Added Successfully!")
    print(new_id, ":", library[new_id])

    add_more = input("\nAdd another book? (yes/no): ").lower()

template = dict.fromkeys(["title", "author", "year"], "N/A")
template.clear()  

library.pop("B3")

search_key = "author"
search_value = "Smith"
found = "Not found"

for book_id, info in library.items():
    if info.get(search_key) == search_value:
        found = {book_id: info.copy()}  
        break

if "B1" in library:
    library["B1"].update({"title": "Python Fundamentals"})

library["B1"].setdefault("genre", "Education")

removed_last = library.popitem()   

report = library.copy() 

total_books = len(library)

earliest_year = None
for _, info in library.items():
    year = info["year"]
    if earliest_year is None or year < earliest_year:
        earliest_year = year

print("\n--- Search Result ---")
print(found)

print("\n--- Last Removed Book (popitem) ---")
print(removed_last)

print("\n--- Report (All Books) ---")
print(report)

print("\n--- Statistics ---")
print("Total Books:", total_books)
print("Earliest Year in Collection:", earliest_year)

print("\n--- Dictionary Keys ---")
print(library.keys())

print("\n--- Dictionary Values ---")
print(library.values())

print("\n--- User Search Option ---")
search_field = input("Search by (title/author/year): ").lower()
search_value = input("Enter value to search: ")

found_search = "No matching book found"

for book_id, info in library.items():
    if str(info.get(search_field)).lower() == search_value.lower():
        found_search = {book_id: info}
        break

print("\nSearch Result:", found_search)

print("\n--- User Update Option ---")
update_id = input("Enter Book ID to update: ")

if update_id in library:
    print("Current Book Data:", library[update_id])
    field = input("What do you want to update? (title/author/year): ").lower()
    new_val = input("Enter new value: ")

    if field == "year":
        new_val = int(new_val)

    library[update_id][field] = new_val

    print("\nBook Updated Successfully!")
    print(update_id, ":", library[update_id])
else:
    print("\nBook ID not found!")


