import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def open_file(file_path):
    try:
        os.startfile(file_path)
    except Exception as e:
        print(f"Error opening file: {e}")

def Opening():
    while True:
        print("Fajny launcher GTA SA, mojej ukochanej gierki")
        print("SAMP = 1")
        print("GTA SA = 2")
        print("MTA = 3")
        print("GTA SA UNDERGROUND = 4")
        print("NEED FOR SPEED UNDERGROUND = 5")
        user_input = input("Wybierz: ")
        try:
            choice = int(user_input)
            if choice == 1:
                open_file("D:\\Pobrane\\GTA San Andreas\\gta-sa.exe")
            elif choice == 2:
                open_file("D:\\Pobrane\\GTA San Andreas\\gta_sa.lnk")
            elif choice == 3:
                open_file("D:\\Globalny folder gier dysk D\\MTA SA 1.6\\Multi Theft Auto.exe")
            elif choice == 4:
                open_file("D:\\Pobrane\\GTA SA UNDERGROUND\\gta_sa.exe.lnk")
            elif choice == 5:
                open_file("C:\\Users\\fulek\\Desktop\\speed.exe.lnk")
            else:
                print("Nie ma takiej opcji")
        except ValueError:
            print("Proszę wpisać poprawny numer.")
        
        input("Press Enter to continue...")  # To pause before clearing the console
        clear_console()

if __name__ == "__main__":
    Opening()
