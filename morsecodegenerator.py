def playmorse(inp):
    morse_data={" ":" ","A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","Ä":".-.-","Á":".--.-","Å":".--.-","Ch":"----","É":"..-..","Ñ":"--.--","Ö":"---.","Ü":"..--","?":"..--..",",":"--..--",".":".-.-.-"}
    import subprocess
    def playsound(sound):
        if sound=="dit":
            subprocess.call(["afplay","sounds/dit.wav"])
        elif sound=="dash":
            subprocess.call(["afplay","sounds/dash.wav"])
        elif sound=="space":
            subprocess.call(["afplay","sounds/space.wav"])
        else: print("Wrong sound.")
    a=[]
    charlist=[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.', ',', '?', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'Ä', 'Á', 'Å', 'É', 'Ñ', 'Ö', 'Ü']
    for letter in inp:
        if set([letter]).issubset(set(charlist)):
             a.append(letter)
    for letter in a:
        morc=[]
        dt=morse_data.get(letter)
        for r in dt:morc.append(r)
        for r in morc:
            if r=="-":playsound("dash")
            elif r==".":playsound("dit")
            elif r==" ":
                for i in range(0,3):playsound("space")
            else: blank=blank
            playsound("space")
if __name__ == "__main__":
    inp=input("Enter the TEXT that has to be converted to MORSE CODE : ")
    inp=inp.upper()            
    playmorse(inp)