import csv

def add_todo(file_name):
    todo_name = input("Enter a todo item: ")
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        writer.writerow([todo_name, "False"])

def remove_todo():
    print("Remove todo")

def mark_todo():
    print("Mark todo")

def view_todo(file_name):
    try:
        with open(file_name, "r") as f:
            reader = csv.reader(f)
            # [
            #   [title,completed],
            #   [do grocery,False],
            #   [do laundry,False],
            #   [complete assignment,False]
            # ]
            reader.__next__()
            for row in reader:
                if (row[1] == "True"):
                    print(f"{row[0]} is complete.")
                else:
                    print(f"{row[0]} is not complete.")
    except FileNotFoundError:
        print("The todo file doesn't exist.")