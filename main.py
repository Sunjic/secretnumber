secret = 5

guess = int(input("Pogodite točan broj (od 1 do 10):"))

if guess == secret:
    print("pogodili ste - Čestitamo! Točan broj je 5.")
else:
    print("Žao mi je, Vaš odgovor nije točan...traženi broj nije " +str(guess))