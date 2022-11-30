import wikipedia

user_input = None
while user_input != "":
    user_input = input("Search Wikipedia:\n>>>")
    page = wikipedia.page(f"{user_input}")
    print(f"{page.title} \n{page.url}")
    print(wikipedia.summary(f"{user_input}"))
    print(" ")

