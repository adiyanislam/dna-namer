"""
ran

Description:
"""
import random
from random import randint



dna_sequence = {"T":"A",
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

proteins = {"UUU":"Phe",
            "UUC":"Phe",
            "UUA":"Leu",
            "UUG":"Leu",
            "UCU":"Ser",
            "UCC":"Ser",
            "UCA":"Ser",
            "UCG":"Ser",
            "UAU":"Tyr",
            "UAC":"Tyr",
            "UAA":"Stop",
            "UAG":"Stop",
            "UGU":"Cys",
            "UGC":"Cys",
            "UGA":"Stop",
            "UGG":"Trp",
            "CUU":"Leu",
            "CUC":"Leu",
            "CUA":"Leu",
            "CUG":"Leu",
            "CCU":"Pro",
            "CCC":"Pro",
            "CCA":"Pro",
            "CCG":"Pro",
            "CAU":"His",
            "CAC":"His",
            "CAA":"Gln",
            "CAG":"Gln",
            "CGU":"Arg",
            "CGC":"Arg",
            "CGA":"Arg",
            "CGG":"Arg",
            "AUU":"lle",
            "AUC":"lle",
            "AUA":"lle",
            "AUG":"Met",
            "ACU":"Thr",
            "ACC":"Thr",
            "ACA":"Thr",
            "ACG":"Thr",
            "AAU":"Asn",
            "AAC":"Asn",
            "AAA":"Lys",
            "AAG":"Lys",
            "AGU":"Ser",
            "AGC":"Ser",
            "AGA":"Arg",
            "AGG":"Arg",
            "GUU":"Val",
            "GUC":"Val",
            "GUA":"Val",
            "GUG":"Val",
            "GCU":"Ala",
            "GCC":"Ala",
            "GCA":"Ala",
            "GCG":"Ala",
            "GAU":"Asp",
            "GAC":"Asp",
            "GAA":"Glu",
            "GAG":"Glu",
            "GGU":"Gly",
            "GGC":"Gly",
            "GGA":"Gly",
            "GGG":"Gly"
            
                }


def check(dna):
    for i in dna:
        if i is not "T" and i is not "A" and i is not "G" and i is not "C":
            return(0)
            break
    return(1)
    
def checks(dna):
    x = 0
    for i in dna:
        if i is not "U" and i is not "A" and i is not "G" and i is not "C":
            x += 1
    return(x)
        
def dna_check(DNA):
    word = ""
    for i in DNA:
        letter = dna_sequence[i]
        word += letter
    return word

        
def mRNA(DNA):
    word = ""
    for i in DNA:
        letter = mrna[i]
        word += letter
    return word

def prot(mrna):
    word = ""
    temp = ""
    found = False
    length = len(mrna)
    while length % 3 != 0:
        mrna = mrna[:-1]
        length = len(mrna)
    for i in range(0, length):
        letter = mrna[i]
        if i % 3 != 2:
            temp += letter
        elif i % 3 == 2:
            temp += letter
            protein = proteins[temp]
            if protein == "Met":
                if found:
                    word += "Met"
                elif not found:
                    word += "Start"
                    found = True
            else:
                word += protein
            temp = ""
            word += "-"
    return(word)
        
            
        
        
        
def random(number):
    word = "AUG"
    temp = ""
    for i in range(int(number/2)):
        temp = ""
        for z in range(3):
            num = randint(0, 3)
            if num == 0:
                temp += "G"
            elif num == 1:
                temp += "U"
            elif num == 2:
                temp += "A"
            else:
                temp += "C"
            if temp == "UGA" or temp == "UAA" or temp == "UAG":
                i -= 1
                temp = ""
                continue
            else:
                word += temp
    if num == 1:
        word += "UGA"
    elif num == 2:
        word += "UAA"
    else:
        word += "UAG"
    return word
        
def dna(DNA):
    word = ""
    for i in DNA:
        letter = reverse_mrna[i]
        word += letter
    return word

def inp(mem):
    choice = input().upper().strip()
    choice = choice.replace(" ", "")
    if choice == "MEM":
        return mem
    else:
        return choice
    
