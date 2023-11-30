import functions *

#All the functions imported from functions.py


def menu():
    while True:
        print("Menu:")
        print("1. Search all post titles on Sam Altman's blog")
        print("2. Show the titles of Sam Altman's blog posts")
        print("3. Download Sam Altman's posts in sam-altman directory")
        print("4. Analyse de Sentiment of certain Sam Altman's post")
        print("5. Option 5 (BUILDING)")
        print("6. Exit")
        opcion = input("Select yout option number ")
        if opcion == "1":
                print("=======================")
                titles=get_titles(url)
                df_titles=pd.DataFrame(titles)
                df_titles.to_csv('san_titles.csv', index=False)
                print("=======================")
        elif opcion == "2":
                print("=======================")
                df_titles= pd.read_csv('san_titles.csv')
                print(df_titles)
                print("=======================")
        elif opcion == "3":
                PostInDir(url, dir_name)
        elif opcion == "4":
                b=input("Type the post's title to analyse: ")
                print("=======================")
                Sentiment(url, b)
                print("=======================")
        elif opcion == "5":
            fun()
        elif opcion == "6":
            return
        else:
            print(" Invalid option. Try again.")


def fun():
    print("BUILDING")


menu()
