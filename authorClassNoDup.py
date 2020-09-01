class Author:
    def __init__(self, name):
        self.author_name = name
        self.books = []
        self.dup_books = []

    def publish(self, title):
        if (title) not in self.books:
            self.books.append(title)
        else:
            print(f"Error - Duplicate book title: {title}")

    def __str__(self):
        titles = ", ".join(self.books) or "No published books"
        return f"{self.author_name}. Books: {titles}"


def main():
    sanderson = Author("Brandon Sanderson")
    sanderson.publish("Mistborn - The Final Empire")
    sanderson.publish("Mistborn - The Final Empire")
    sanderson.publish("The Way of Kings")

    meyer = Author("Marissa Meyer")
    meyer.publish("Cinder")
    meyer.publish("Cinder")

    print(sanderson)
    print(meyer)


main()
