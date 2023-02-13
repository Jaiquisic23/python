'''
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
'''

def reto1(text):
    
    leet_dict = {"A": "4","a": "4", "B": "I3", "b": "I3", "C": "[","c": "[", "D": ")","d": ")", "E": "3","e": "3", 
                 "F": "|=","f": "|=", "G": "&", "g": "&", "H": "#", "h": "#", "I": "1","i": "1",
            "J": ",_|","j": ",_|", "K": ">|", "k": ">|", "L": "1", "l": "1", "M": "/\/\\","m": "/\/\\",
            "N": " ^/","n": " ^/", "O": "0", "o": "0", "P": " |*","p": " |*", "Q": "(_,)", "q": "(_,)",
            "R": "I2","r": "I2", "S": "5","s": "5", "T": "7", "t": "7", "U": "(_)","u": "(_)", "V": "\/","v": "\/",
            "W": "\/\/","w": "\/\/", "X": "><","x": "><", "Y": "j","y": "j", "Z": "2", "z": "2",
            "1": "L", "2": "R", "3": "E", "4": "A", "5": "S", "6": "b", "7": "T", "8": "B", "9": "g", "0": "o"}
    leet_text = ''
    for char in text:
        if char in leet_dict:
            leet_text += leet_dict[char]
        else:
            leet_text += char
    return leet_text

text = input("Enter a text: ")
leet_text = reto1(text)
print("Leet text: " + leet_text)

