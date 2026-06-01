add_book(book):
    1. Check book is not in 'books'
    2. Assign 'book_id'
    3. Store in 'books'

add_member(member):
    1. Check member is not in 'members'
    2. Assign 'member_id'
    3. Store in 'members'

borrow_book(member_id, book_id):
    1. Find member
    2. Find book
    3. Check book available
    4. Create a loan
    5. Store loan in 'loans'

return_book(member_id, book_id):
    1. Find loan
    2. Assign 'returned_date'
