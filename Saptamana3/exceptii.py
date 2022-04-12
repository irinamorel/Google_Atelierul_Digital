variabila = input("Introdu un numar:")
my_int = None
try:
     este_intreg = int(variabila)
     print("Nu exista exceptii intalnite")
     if my_int is None:
         raise ValueError
except ValueError as e:
    print('eroare de valoare', e)
except Exception as e:
    print('a aparut o eroare', e)
finally:
    print("se ruleaza oricum")
