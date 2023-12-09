import secrets, mnemonic, base58, hashlib
from tkinter import *

root = Tk()
root.title("Seed Generator")
root.columnconfigure([0, 1, 2, 3, 4], minsize=180)
h = Entry()
w = Entry()
e = Entry()

def generate(number):
    language = 'english'
    seed = secrets.token_bytes(number)
    print(seed)

    h.delete(0, END)
    h.insert(0, seed.hex())

    extended_key = '80' + seed.hex()
    first_hash = hashlib.sha256(bytes.fromhex(extended_key)).digest()
    second_hash = hashlib.sha256(first_hash).digest()
    checksum = second_hash[:4]
    extended_key += checksum.hex()
    wif = base58.b58encode(bytes.fromhex(extended_key)).decode()
    w.delete(0, END)
    w.insert(0, wif)

    mnemonic_words = mnemonic.Mnemonic(language).to_mnemonic(seed)
    mnemonic_word_list = " ".join(mnemonic_words.split())
    print(mnemonic_word_list)
    e.delete(0, END)
    e.insert(0, mnemonic_word_list)

btn_12 = Button(text = "Generate 12-Word Seed", command = lambda: generate(16))
btn_15 = Button(text = "Generate 15-Word Seed", command = lambda: generate(20))
btn_18 = Button(text = "Generate 18-Word Seed", command = lambda: generate(24))
btn_21 = Button(text = "Generate 21-Word Seed", command = lambda: generate(28))
btn_24 = Button(text = "Generate 24-Word Seed", command = lambda: generate(32))

btn_12.grid(row=0, column=0, sticky="nsew")
btn_15.grid(row=0, column=1, sticky="nsew")
btn_18.grid(row=0, column=2, sticky="nsew")
btn_21.grid(row=0, column=3, sticky="nsew")
btn_24.grid(row=0, column=4, sticky="nsew")
h.grid(row=1, columnspan=5, sticky="nsew")
w.grid(row=2, columnspan=5, sticky="nsew")
e.grid(row=3, columnspan=5, sticky="nsew")

root.mainloop()
