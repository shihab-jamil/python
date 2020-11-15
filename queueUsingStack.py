books = []
books.append("SPL")
books.append("APL")
books.append("TOC")
books.append("DLD")
books.append("CA")

sample = []

bsize = books.index(books[-1])

for i in range(0,bsize,1):
    sample.append(books.pop())


books.pop()

for i in range(0,bsize - 1 , 1):
    books.append(sample.pop())

print(books)    