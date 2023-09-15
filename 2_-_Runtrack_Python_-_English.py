#Job2.0
class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def SePresenter(self):
        print("Mon nom est", self.first_name )
        print("Mon prènom est", self.last_name )
    
    def accessorN(self):
        return self.first_name 
    
    def accessorFN(self):
        return self.last_name 
    
    def mutatorN(self,new_first_name):
        self.first_name = new_first_name

    def mutatorFN(self,new_last_name):
        self.last_name = new_last_name
# Driver code
# Object instantiation
# a= Person("ilyas", "elyounoussi")
# b= Person("b", "dsi")
# c= Person("c", "d")

# a.SePresenter()
# b.SePresenter()
# c.SePresenter()

# a.mutatorN("k")
# a.SePresenter()



#job2.1

class Book :

    def __init__(self,title,Author):
        self.title=title
        self.Author=Author

    def print(self):
        print("le tittre du livre est", self.title)

class Author(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name,last_name)

        self.work = []

    def listerWork(self):
        if len(self.work) != 0 :
            print ("voici la liste de livre ecris par l'auteur:" , self.first_name, " ", self.last_name)
            for book in self.work:
                print(book.title)

    def writeABook( self ,title):
        newbook= Book( title, self)
        self.work.append(newbook)
        return newbook
    
#Job 2.2


class Customer(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.book_collection = []

    def inventory (self):
            print(self.book_collection)

class Library:

    def __init__(self, name):
        self.name = name
        self.catalog=[]
        self.quantity=0

    def buyBook (self,author, title, quantity ):

        for books in author.work: 
            if books.title == title:

                newbooks= [Book(title, Author), quantity]
                self.catalog.append(newbooks)

    def inventory (self):
        for b in self.catalog:
            print("the inventory of the librairy :", "(", b[0].title,", quantité :", b[1] , ")")

    def rent(self, client, title):
        for b in self.catalog:
            if b[0].title == title and b[1]>0 :
                client.book_collection.append(b[0].title)
                b[1]-= 1
    def renderbooks(self,client):
        for b in client.book_collection:
            i=0
            for b2 in self.catalog:
                i+=1
                if b2[0].title== b:
                    client.book_collection.remove(b)
                    b2[1]+= 1


#TEST JOB 2.1


    
# a=Author("ilyas","elyounoussi")
# a.writeABook ("The Atomic habbits")
# c=Customer("ilyas","elyounoussi")

#___________________________________________________________

#TEST JOB 2.2


# Larousse=Library("Larousse")
# Larousse.buyBook(a,"The Atomic habbits", 100 )
# Larousse.inventory()
# print(" the client c arrives and want to rent the book 'The Atomic Habits'")
# Larousse.rent(c, "The Atomic habbits")

# Larousse.inventory()

# c.inventory()

# print("3 days later, the client render the books he rented (he obviously didnt read any)")
# Larousse.renderbooks(c)
# print("our inventory after he renders")
# Larousse.inventory()
# print("the client collection after rendering")
# c.inventory()


#Job 2.3
 











            


