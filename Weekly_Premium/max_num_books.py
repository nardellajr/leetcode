

def max_num_books(books: list[int]) -> int:
    # get len of books list
    len_books = len(books)

    # get position of min value in books list
    min_index = books.index(min(books))
    max_index = len_books - 1

    i = min_index
    j = max_index
    smallest_book_count = books[min_index]
    checkout_books = 0
    left_book_count = 0

    while i >= 0 or j > min_index:
        # First time through loop, add the smallest value to checkout_books
        if i == min_index:
            checkout_books += smallest_book_count          
            smallest_book_count -= 1
        else:
            # second time thru loop, 1 less than min_index, can only add 1 minus smallest_book_count
            if i >= 0 and smallest_book_count > 0:
                # books on the shelf
                if books[i] >= smallest_book_count:
                    checkout_books += smallest_book_count
                    smallest_book_count -= 1
        # subtract one from i
        i -= 1

        if j == max_index:
            left_book_count = books[max_index]
            checkout_books += left_book_count
            left_book_count -= 1
        else:
            if j > min_index and left_book_count > 0:
                # value of books less than or equal to 1 minus left_book_count
                # take all books on shelf at this position
                if books[j] <= left_book_count:
                    checkout_books += books[j]
                    left_book_count = books[j] - 1
                else:
                    # books on shelf are greater than left_book_count
                    # take left_book_count - 1, minus 1 done above
                    checkout_books += left_book_count
                    left_book_count -= 1
        j -= 1

    return checkout_books


if __name__ == '__main__':

    # len(shelf_of_books) = 5
    shelf_of_books = [8, 5, 2, 7, 9]
    print(max_num_books(shelf_of_books))

    shelf_of_books = [8, 2, 3, 7, 3, 4, 0, 1, 4, 3]
    print(max_num_books(shelf_of_books))



# Better solution
# for _ in range(j, min_index, -1):
#     if books[j] > 0:
#         checkout_books += left_book_count