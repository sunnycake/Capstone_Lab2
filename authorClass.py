class Author:
    def __init__(self, name):
        self.author_name = name
        self.books = []

    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        titles = ", ".join(self.books) or "No published books"
        return f"Name: {self.author_name}. Books: {titles}"
        # if self.books:
        #     titles = ", ".join(self.books)
        # else:
        #     titles = "No published books"
        # return f"Name: {self.author_name}. Books: {titles}"


def main():
    sanderson = Author("Brandon Sanderson")
    sanderson.publish("Mistborn: The Final Empire")
    sanderson.publish("The Way of Kings")

    meyer = Author("Marissa Meyer")
    meyer.publish("Cinder")

    june = Author("June")

    print(sanderson)
    print(meyer)
    print(june)


main()
