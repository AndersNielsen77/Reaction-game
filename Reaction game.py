import time
import random
import os
import winsound

#Beskrivelse af spillet.
print("Dette er et reaktions spil, når der står GO!! Tryk på ENTER. -Den hurtigeste vinder.")
input(f"\nTryk ENTER når du har forstået det!")
os.system('cls')

#Hvilken gamemode.
print("1. Hvor der står GO!! på skærmen.")
print("2. Hvor der står GO!! på skærmen og skifter farve.")
print("3. Hvor der står GO!! på skærmen og afspiller en lyd.")
print("4. Hvor alle overstående, GO!!, skifter farve og afspiller en lyd")
gamemode = input("Hvilken gamemode?: ")


#Hvor mange spillere? input
antal_af_spillere = int(input("Antal af spillere: "))

#impotere værdier.
Spillere = [{
            'navn':input(f"Spiller {i+1}: "),
            'points':0
            } for i in range(antal_af_spillere)]

#Antal rundter spllerne vil spille.
runter = int(input("Rundter: "))
os.system('cls')

#Standard med go i terminal.
if gamemode == '1' or 'GO':
    for i in range(0,runter):
        print("-"*20 + f"\nDet er nu rundte {i}!\n" + "-"*20)
        for Spiller in Spillere:
            input(f"Det er nu {Spiller['navn']}'s tur. \nTryk enter når du er klar.")
            time.sleep(0.5)
            print("Klar..")

            #Random tid mellem 1 og 4 sekundter.
            time.sleep(random.randint(0,4))
            then = time.time()
            t = input("GO!!")
            reaktions_tid = time.time()-then
            print(f"{reaktions_tid*1000:.0f} ms")
            Spiller["points"] += reaktions_tid
            time.sleep(0.5)
            print("-"*20)
            #Snyd detector implemitering
            #if reaktions_tid*1000() >= '20':
            #    print("Spiller "f" har snydt")
            #    time.sleep(2)
            #    exit()
    os.system('cls')
    vinder = min(Spillere,key=lambda a: a['points'])['navn']
    print("Vinderen er...")
    time.sleep(0.5)
    print(f"{vinder}!")
    time.sleep(3)
    exit()

#Standard med go og lys.
if gamemode == '2':
    for i in range(0,runter):
        print("-"*20 + f"\nDet er nu rundte {i}!\n" + "-"*20)
        for Spiller in Spillere:
            input(f"Det er nu {Spiller['navn']}'s tur. \nTryk enter når du er klar.")
            time.sleep(0.5)
            print("Klar..")

            #Random tid mellem 1 og 4 sekundter.
            time.sleep(random.randint(1,4))
            then = time.time()
            os.system('color 4')
            t = input("GO!!")
            reaktions_tid = time.time()-then
            print(f"{reaktions_tid*1000:.0f} ms")
            Spiller["points"] += reaktions_tid
            time.sleep(0.5)
            print("-"*20)
            #Snyd detector implemitering
            #if reaktions_tid*1000() >= '20':
            #    print("Spiller "f" har snydt")
            #    time.sleep(2)
            #    exit()
    os.system('cls')
    vinder = min(Spillere,key=lambda a: a['points'])['navn']
    print("Vinderen er...")
    time.sleep(0.5)
    print(f"{vinder}!")
    time.sleep(3)
    exit()

#Standard med go og lyd.
if gamemode == '3':
    for i in range(0,runter):
        print("-"*20 + f"\nDet er nu rundte {i}!\n" + "-"*20)
        for Spiller in Spillere:
            input(f"Det er nu {Spiller['navn']}'s tur. \nTryk enter når du er klar.")
            time.sleep(0.5)
            print("Klar..")
            time.sleep(random.randint(1,4))
            then = time.time()

            #starter musik
            t = input("GO!!")
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)
            reaktions_tid = time.time()-then
            print(f"{reaktions_tid*1000:.0f} ms")
            Spiller["points"] += reaktions_tid
            time.sleep(0.5)
            print("-"*20)
            #Snyd detector implemitering
            #if reaktions_tid*1000() >= '20':
            #    print("Spiller "f" har snydt")
            #    time.sleep(2)
            #    exit()
    os.system('cls')
    vinder = min(Spillere,key=lambda a: a['points'])['navn']
    print("Vinderen er...")
    time.sleep(0.5)
    print(f"{vinder}!")
    time.sleep(3)
    exit()

#Standard med go og skift i farve baggrund i terminal og lyd.
if gamemode == '4':
    for i in range(0,runter):
        print("-"*20 + f"\nDet er nu rundte {i}!\n" + "-"*20)
        for Spiller in Spillere:
            input(f"Det er nu {Spiller['navn']}'s tur. \nTryk enter når du er klar.")
            #
            time.sleep(0.5)
            print("Klar..")

            #Random tid mellem 1 og 4 sekundter.
            time.sleep(random.randint(1,4))
            then = time.time()

            #Skifter farve og spille musik.
            os.system('color 4')
            winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

            t = input("GO!!")
            reaktions_tid = time.time()-then
            print(f"{reaktions_tid*1000:.0f} ms")
            Spiller["points"] += reaktions_tid
            time.sleep(0.5)
            print("-"*20)
            #Snyd detector implemitering
            #if reaktions_tid*1000() >= '20':
            #    print("Spiller "f" har snydt")
            #    time.sleep(2)
            #    exit()
    os.system('cls')
    vinder = min(Spillere,key=lambda a: a['points'])['navn']
    print("Vinderen er...")
    time.sleep(0.5)
    print(f"{vinder}!")
    time.sleep(3)
    exit()
    
