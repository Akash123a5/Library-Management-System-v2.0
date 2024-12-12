def return_book(all_books, lend_info):
    book_title = input("Enter book title to return: ")
    borrower_name = input("Enter borrower's name: ")

    for lend in lend_info:
        if lend['book_title'].lower() == book_title.lower() and lend['borrower_name'].lower() == borrower_name.lower():
            for book in all_books:
                if book['title'].lower() == book_title.lower():
                    book['quantity'] += 1  # পরিমাণ বাড়াও
                    lend_info.remove(lend)  # ধার দেওয়া তথ্য মুছে ফেলো
                    print(f"Book '{book_title}' has been returned by {borrower_name}.")
                    return
    print(f"No record found for book '{book_title}' lent to {borrower_name}.")
