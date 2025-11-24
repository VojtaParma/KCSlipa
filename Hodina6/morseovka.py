morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.'}

text = input("Zadej text: ").upper()
morse_code = ""
for i in text:
    code = morse.get(i.upper(), "")
    morse_code += code + " "

print("Morse:", morse_code)
