def lend_book(all_books, lend_info):
    borrower_name = input("Enter borrower's name: ")
    borrower_phone = input("Enter borrower's phone number: ")
    book_title = input("Enter book title: ")
    return_due_date = input("Enter return due date (YYYY-MM-DD): ")

    for book in all_books:
        if book['title'].lower() == book_title.lower():
            if book['quantity'] > 0:  
                book['quantity'] -= 1  
                lend_info.append({
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "book_title": book_title,
                    "return_due_date": return_due_date
                })
                print(f"Book '{book_title}' has been lent to {borrower_name}.")
                return
            else:
                print(f"Sorry, the book '{book_title}' is out of stock.")
                return
    
    print(f"Book '{book_title}' not found in the library.")
