subjects = ["math", "history", "pe", "chemistry", "biology", "literature"]
choice = input(f"Which of these subjects you don't like?\n{subjects}\n~ ").lower()
if choice in subjects:
    subjects.remove(choice)
print(subjects)
