def bahola(ismalar):
    baholar={}
    while ismalar:
        ism=ismalar.pop()
        baho=input(f"talaba {ism.title()} ning bahosini kiriting: ")
        baholar[ism]=int(baho)
    return baholar
talabalar = ["sherzod","vali","G'ani","G'ulom"]
baholar = bahola(talabalar[:])
print(baholar)
print(talabalar)