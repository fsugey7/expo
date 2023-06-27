import random 
import time 

option = 0
total_user = 0
total_computer = 0
plays = 0
dices = { 1:["┌─────────┐","│         │","│    ●    │", "│         │", "└─────────┘"],
    2: ["┌─────────┐","│  ●      │", "│         │","│      ●  │", "└─────────┘"],
    3: ["┌─────────┐","│  ●      │", "│    ●    │", "│      ●  │", "└─────────┘"],
    4: ["┌─────────┐", "│  ●   ●  │", "│         │", "│  ●   ●  │", "└─────────┘"],
    5: ["┌─────────┐","│  ●   ●  │", "│    ●    │", "│  ●   ●  │", "└─────────┘"],
    6: ["┌─────────┐","│  ●   ●  │","│  ●   ●  │","│  ●   ●  │", "└─────────┘"],
}

    
while option != "3":
    print(f"----- El juego de los dados -----\n"
          f"1. Quiero Jugar\n"
          f"2. Quiero saber los resultados\n"
          f"3. Salir.\n")
    
    
    option = input()
    if option == "1":
            print ("¡Vamos a jugar!")
            print ("Lanzando los dados ...")
            time.sleep(1)
            #Dados del usuario
            user_dice_one = random.randint(1,6)
            user_dice_two = random.randint(1,6)
            #Suma de la partida del usuario
            user_sum = user_dice_one + user_dice_two
            total_user += user_sum
            time.sleep(1.5)
            print("Usuario 👥 :")
            for line1, line2 in zip(dices[user_dice_one],dices[user_dice_two]):
                 print(line1, line2)

            #Dados del computador
            computer_dice_one = random.randint(1,6)
            computer_dice_two = random.randint(1,6)
            #Suma de la partida del computador 
            computer_sum = computer_dice_one + computer_dice_two
            total_computer += computer_sum
        
            print("Computadora 💻 :")
            for line1, line2 in zip(dices[computer_dice_one],dices[computer_dice_two]):
                 print(line1, line2)


            print(f"Tus dados fueron : {user_dice_one} y {user_dice_two}")
            print(f"Los dados del computador fueron : {computer_dice_one} y {computer_dice_two}")
            
            plays += 1
            if user_sum > computer_sum:
                    time.sleep(1)
                    print("Ganaste 🎉")
            elif user_sum < computer_sum:
                    time.sleep(1)
                    print("Perdiste ☹️ 👎")
            else:
                    time.sleep(1)
                    print("Empate 🤝")     
    elif option == "2":
     print("Cargando resultados...💣")
     time.sleep(1.5)
     print("3...2...1...")
     time.sleep(0.5)
     print("💥💥💥💥💥💥")
     print(f"Cantidad de partidas jugadas: {plays}")
     time.sleep(1)
     print(f"Puntaje total usuario: {total_user}") 
     time.sleep(1)
     print(f"Puntaje total computadora: {total_computer}")
     time.sleep(1)
    
    elif option == "3":
     print("¡Gracias por jugar!")
     print("✨🌟💖💎🦄💎💖🌟✨🌟💖💎🦄💎💖🌟✨")
    else:
        print("¡¡¡TE EQUIVOCASTE MALDITO INSECTO!!!🦗")
        print(" ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜")
        print(" ⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜")
        print(" ⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜")
        print(" ⬜⬜⬜⬜⬜⬜⬜⬛⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜")
        print(" ⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜")
        print(" ⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜")
        print(" ⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬛")
        print(" ⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
        print(" ⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
        print(" ⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛")
        print(" ⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜")
        print(" ⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛🏻🏻⬛⬛⬛⬛⬛⬛⬛⬛⬜")
        print(" ⬜⬜⬛🏻⬛⬛⬛⬛🏻🏻🏻🏻🏻⬛⬛⬛⬛⬛⬛⬜⬜")
        print(" ⬜⬜⬛🏻⬛⬛⬛🏻🏻🏻🏻🏻🏻⬛⬛⬛⬛⬛⬛⬛⬛")
        print(" ⬜⬜⬛🏻🏻⬛🏻🏻🏻🏻🏻🏻🏻⬛⬛⬛⬛⬛⬛⬛⬜")
        print(" ⬜⬜🟥🏻🏻🏻🏻🏻🏻🏻🏻🏻🏻⬛⬛⬛⬛⬛⬛⬜⬜")
        print(" ⬜⬜🌫️🟥🏻🏻🏻🏻🏻⬛⬛⬛🏻⬛🏽⬛⬛⬛⬜⬜⬜")
        print(" ⬜⬜🌫️🟥🟥🏻🏻🏻⬛⬜⬜⬛🏻🏻🏻⬛⬜⬜⬜⬜⬜")
        print(" ⬜⬜⬜🌫️🟥🏻🏻⬛⬛⬜⬜🏻🏻🏻🏽⬛⬛⬛⬜⬜⬜")
        print(" ⬜⬜⬜⬛🏻🏻🏻🏻🏻🏻🏻🏻🏻⬛⬛⬛🟨🏽⬛⬜⬜")
        print(" ⬜⬛⬛⬛⬛🏻⬛⬛⬛🏻🏻🏻⬛🏽🟨🟨🟨🏽⬛⬜⬜")
        print(" ⬜⬛🟪🏽⬛⬛🏻🏻🏻🏻⬛⬛🏽🟨🟨🏽⬜⬛⬜⬜⬜")
        print(" ⬜⬜⬛🟪🟪🟦⬛⬛⬛⬛🟦🌫️⬜🏽🏽⬜⬛⬛⬜⬜⬜")
        print(" ⬜⬜⬜⬛⬜🟦⬛⬛🟦🟦⬜⬜🟪⬜⬜⬛🟦⬛⬜⬜⬜")
        print(" ⬜⬜⬛⬜⬜⬜🌫️⬜⬜⬜⬜🟪🟪⬛⬛🟦⬛🟦⬛⬜⬜")
        print(" ⬜⬜⬜⬛🌫️⬛⬛⬛🟪🟪🟪🟪⬛⬛🟦🟦🟦🟦⬛⬜⬜")
        print(" ⬜⬜⬜⬛⬛🟨🟨🟨🏽⬛⬛⬛🟪⬛⬛🟦🟦⬛⬛⬜⬜")
        print(" ⬜⬜⬛🟦⬛🏽🏽🏽🏽🏽⬛⬜🟪⬛⬜⬛🟦🟦🟦⬛⬜")
        print(" ⬜⬜⬛🟦⬛🟨🟨🟨🟨🏽⬜🟪⬛⬜⬜⬛🟦🟦🟦⬛⬜")
        print(" ⬜⬜⬛⬛⬛🏽🏽🏽🏽🏽🟪⬛⬜⬜⬜⬜⬛⬛⬛⬛⬛")
        print(" ⬜⬛🟪🟪🏿🏿🏿🏿🏿🏿🏿🏿⬛⬜⬜⬜⬛⬜⬜🟪⬛")
        print(" ⬜⬛⬛🟪⬛🏿🏿🏿🏿🏿🏿🟨🏽⬛⬜⬛⬛⬛🟪🟪⬛")
        print(" ⬛🟪⬛⬜⬛⬜🟨🟨🏽⬜⬛⬜🟨🏽⬛⬜🟪⬜🟪⬜⬛")
        print(" ⬛🟪⬛🌫️⬛⬜🏽🏽🏽🌫️⬛⬛⬜🌫️⬛⬜⬛⬜⬜⬜⬛")
        print(" ⬛🟪🟪⬛⬛🌫️🟨🟨🏽🌫️⬛🟦⬛⬛🟦⬛⬛⬜🟪⬜⬛")
        print(" ⬜⬛⬛⬛⬛⬛⬜⬜🌫️⬛🟦🟦🟦🟦⬛⬛⬛🟪⬛⬛⬜")
        print(" ⬜⬜⬜⬛🟦🟦⬛⬛⬛⬛🟦🟦🟦🟦🟦⬛⬛⬛⬜⬜⬜")
        print(" ⬜⬜⬜⬛🟦⬛🟦🟦⬛⬛⬛🟦⬛🟦🟦⬛⬛⬜⬜⬜⬜")
        print(" ⬜⬜⬜⬛⬛🟦🟦🟦⬛⬜⬛🟦🟦🟦⬛🟦⬛⬜⬜⬜⬜")
        print(" ⬜⬜⬜⬛🟦🟦🟦🟦⬛⬜⬜⬛🟦🟦🟦🟦🟦⬛⬜⬜⬜")
        print(" ⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛🟦🟦🟦🟦⬛⬛⬜⬜⬜")
        print(" ⬜⬜⬜⬛⬜⬜⬜🟪⬛⬜⬜⬜⬛⬛⬛⬜⬜⬛⬜⬜⬜")
        print(" ⬜⬜⬜⬛⬜⬜⬜🟪⬛⬜⬜⬜⬛⬜⬜⬜🟪🟪⬛⬜⬜")
        print(" ⬜⬜⬛⬜⬜🟪🟪🟪⬛⬜⬜⬜⬜⬛🟪⬜⬜🟪⬛⬜⬜")
        print(" ⬜⬛🏽🟨🏽⬜🟪⬛⬜⬜⬜⬜⬜⬛⬜🏽🟨🏽⬛⬜⬜")
        print(" ⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜")




















