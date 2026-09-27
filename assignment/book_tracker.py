def dashboard(): 
    print('=' * 40)
    print("📚  YOUR LIBRARY")
    print('=' * 40)


def estimate_reading_time(pages):
    estimate_reading_time = pages / 40
    return round(estimate_reading_time, 1)


def add_book(library):
    title = input("Book title: ").title()
    author = input("Author: ")
    pages = int(input("Page count: "))
    hours =  estimate_reading_time(pages)
   # print(f"The {title} by {author} is approx. {hours} hours to read.")
   
    book = {
       "title": title, 
       "author": author,
       "pages": pages,
       "hours": hours
   }
   
    library.append(book)
    print(f"Book added: The {title} by {author} is approx. {hours} hours to read.")
   
def view_books(library):
    if len(library) == 0:
        print("Your library is empty. Add a book first!")
    else:
        for i in range(len(library)):
            book = library[i]
            print(f"{i +1}) '{book['title']}' - {book['author']} ({book['pages']} pages - approx. {book['hours']} hours to read)")
 
def show_menu():
    print("What would you like to do?")
    print()
    print("1) View books")
    print("2) Add a book")
    print()
    print("q) Quit")  
    
    choice = input(">  ")
    return choice.strip().lower()         

def main():
    dashboard()
    
    library = []
    while True:
        choice = show_menu()
        
        if choice == "1":
            view_books(library)
        elif choice == "2":
            add_book(library)
        elif choice == "q" or "Quit" or "Exit":
            print("Exit")
            break
        else:
            print("Invalid selection.")
    


if __name__ == "__main__":
    main()

