print("Enter borrowed books in the format 'Book Title - Days Borrowed', separated by commas:")
records = input(":")

borrowed_books = {} 
for record in records.split(", "):
    title, days = record.split(" - ") 
    days = int(days) 
    if title in borrowed_books:
        borrowed_books[title] += days 
    else:
        borrowed_books[title] = days

most_borrowed = max(borrowed_books, key=borrowed_books.get)

least_borrowed = min(borrowed_books, key=borrowed_books.get)

average_days = sum(borrowed_books.values()) / len(borrowed_books)

unique_titles = list(borrowed_books.keys())

sorted_books = sorted(borrowed_books.items(), key=lambda x: x[1], reverse=True)

print(f"\nMost Borrowed Book: {most_borrowed} ({borrowed_books[most_borrowed]} days)")
print(f"Least Borrowed Book: {least_borrowed} ({borrowed_books[least_borrowed]} days)")
print(f"Average Borrowing Days: {average_days:.2f}")
print(f"Unique Titles: {', '.join(unique_titles)}")
print("\nBooks sorted by borrowing days")
for book, days in sorted_books:
    print(f"{book}: {days} days")

 