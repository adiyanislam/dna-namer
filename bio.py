"""
bio

Description:
"""
import ran
import tsapp


file = open("memory.txt", "r")
mem = file.read()
file.close()



dna = {"T":"A",
       "A":"T",
       "G":"C",
       "C":"G",
            }


mrna = {"A":"U",
        "T":"A",
        "G":"C",
        "C":"G",
                }
reverse_mrna = {"U":"A",
                "A":"T",
                "C":"G",
                "G":"C",
                        }

window = tsapp.GraphicsWindow()
asteroid = tsapp.Sprite("SkyMountains.jpg", 0, 0,)
window.add_object(asteroid)


running = True

while window.is_running:
    
    
    while running:
        
        window.finish_frame()
        print("1. Find other DNA strand 2. Translate DNA to mRNA 3. Find Amino acid sequence 4. Create random mRNA strand 5. Translate mRNA to DNA 6. Settings 7. END")
        choice = input().strip().upper()
        if choice == "1":
            print("Enter the DNA sequence")
            choice = ran.inp(mem)
            while ran.check(choice) == 0:
                print("Please enter a valid input")
                choice = ran.inp(mem)
            mem = ran.dna_check(choice)
            print(mem)
        elif choice == "2":
            print("Enter the DNA sequence")
            choice = ran.inp(mem)
            while ran.check(choice) == 0:
                print("Please enter a valid input")
                choice = ran.inp(mem)
            mem = ran.mRNA(choice)
            print(mem)
        elif choice == "3":
            print("Enter the mRNA sequence.")
            choice = ran.inp(mem)
            mem = ran.prot(choice)
            print(mem)
        elif choice == "4":
            print("How many codons will there be?(Excluding start and end codons)") 
            choice = int(input())
            mem = ran.random(choice)
            print(mem)
        elif choice == "5":
            print("Enter the mRNA sequence.")
            choice = ran.inp(mem)
            mem = ran.dna(choice)
            print(mem)
        elif choice == "6":
            print("1. Read Memory 2. Clear memory ")
            choice = input().strip().upper()
            if choice == "1":
                print(mem)
            else:
                mem = ""
        elif choice == "7":
            running = False
            
            
    window.finish_frame()


file = open("memory.txt", "w")
file.write(mem)
file.close()
