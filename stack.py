books = []

books.append("SPL")
books.append("APL")
books.append("TOC")
books.append("DLD")
books.append("CA")

print(books)


books.pop()
print("The top element is: ",books[-1])

books.pop()
books.pop()
books.pop()
books.pop()

if not books:                   #check wheather book is empty or not
    print("No books left")

