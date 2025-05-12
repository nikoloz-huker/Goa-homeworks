# ცვლადში შეინახეთ თქვენი გვარი. ინდექსინგის საშუალებით გამოიტანეთ თქვენი გვარის პირველი, ბოლო და შუა ასოები.
sourname = ("edisherashvili")
print(sourname[0], sourname[6], sourname[-1])

                                                    #2
# შეინახე ცვლადში "Hello, World!". Slicing-ის საშუალებით ამ სტრინგიდან  ამოიღეთ ცალკე სიტყვა "Hello" და ცალკე სიტყვა "World!". შეინახეთ ისინი ცვლადებში და გამოიტანეთ ეკრანზე.
text = "Hello, World!"
hello = text[:5]
world = text[7:]
print(hello)
print(world)
                                                 #3
# ცვლადში შეინახეთ წინადადება - "Practice makes perfect". შექმენით ახალი ცვლადი, სადაც ამ წინადადების შებრუნებულ ვერსიას შეინახავთ. საბოლოოდ, ამ წინადადების თავდაპირველი და შებრუნებული ვერსიები დაბეჭდეთ ტერმინალში.
text = "Practice makes perfect"
reversed_text = text[::-1]
print(text)
print(reversed_text)
