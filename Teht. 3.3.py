sukupuoli=input("Biologinen sukupuoli:")
hemoglob=float(input("Hemoglobiinin arvo:"))

if sukupuoli == "nainen" :
    if hemoglob < 117:
        print("Hemoglobiini on alhainen.")
    elif 117<=hemoglob<=175:
        print("Hemoglobiini on normaalin rajoissa.")
    elif hemoglob>175:
        print("Hemoglobiini on korkea.")

if sukupuoli == "mies" :
    if hemoglob < 134:
        print("Hemoglobiini on alhainen.")
    elif 134<=hemoglob<=195:
        print("Hemoglobiini on normaalin rajoissa.")
    elif hemoglob>195:
        print("Hemoglobiini on korkea.")