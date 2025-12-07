d=1.44
p=100
l=50
c=25
b=4
book=p*l*c*b
diskette=d*1024*1024
books_on_diskette = int(diskette//book)
print("Количество книг, помещающихся на дискету:", books_on_diskette)