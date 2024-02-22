import customtkinter as ctk
from tkinter import ttk
from PIL import Image
import json, os
import phe
from Pyfhel import Pyfhel

app = ctk.CTk()
app.geometry("600x480+540+280")
app.title('Homomorphic Encryption Framework')
app.resizable(0,0)

# directory_path = 'GUI CODE/Output/'
directory_path = os.getcwd()
side_img_data = Image.open(os.path.join(directory_path, 'images' + "/side-img.png"))
side_img = ctk.CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
ctk.CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

# main frame
main_frame = ctk.CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
main_frame.pack_propagate(0)
main_frame.pack(expand=True, side="right")

heading = ctk.CTkLabel(master=main_frame, text="Operations Interface", text_color="#601E88", justify="left", font=("Arial Bold", 24))
heading.place(x=30, y=50)
side_heading = ctk.CTkLabel(master=main_frame, text="Operate on encrypted data", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12))
side_heading.place(x=30, y=84)

# label 1
label1 = ctk.CTkLabel(main_frame, text='Algorithm', text_color="#601E88", font=("Arial Bold", 14))

# combobox i.e., dependent menus
def menu1_func(e):
    if menu1.get() == 'Paillier':
        menu2.config(values=dependent_options['Paillier'])
        menu2.current(0)
        entry1.configure(placeholder_text='Enter Integer')
        entry2.configure(placeholder_text='Enter Integer')
    if menu1.get() == 'BFV':
        menu2.config(values=dependent_options['BFV'])
        menu2.current(0)
        entry1.configure(placeholder_text='Enter Integer')
        entry2.configure(placeholder_text='Enter Integer')
    if menu1.get() == 'CKKS':
        menu2.config(values=dependent_options['CKKS'])
        menu2.current(0)
        entry1.configure(placeholder_text='Enter Float')
        entry2.configure(placeholder_text='Enter Float')
    if menu1.get() == 'BGV':
        menu2.config(values=dependent_options['BGV'])
        menu2.current(0)
        entry1.configure(placeholder_text='Enter Integer')
        entry2.configure(placeholder_text='Enter Integer')

dependent_options = {
    'Paillier': ['Addition', 'Subtraction', 'Scalar Multiplication'], 
    'BFV': ['Addition', 'Subtraction', 'Multiplication', 'Exponentation'], 
    'CKKS': ['Addition', 'Subtraction', 'Multiplication'], 
    'BGV': ['Addition', 'Subtraction', 'Multiplication', 'Exponentation']
}
algorithms = ['Paillier', 'BFV', 'CKKS', 'BGV']
menu1 = ttk.Combobox(main_frame, values=algorithms, width=23)
menu1.current(0)
menu1.bind('<<ComboboxSelected>>', menu1_func)
menu2 = ttk.Combobox(main_frame, values=['Addition'], width=23)
menu2.current(0)

label1.place(x=30, y=144)
menu1.place(x=30, y=174)
# label2
label2 = ctk.CTkLabel(main_frame, text='Operation', text_color="#601E88", font=("Arial Bold", 14))
label2.place(x=30, y=214)

menu2.place(x=30, y=244)

# label3
label3 = ctk.CTkLabel(main_frame, text='Number 1', text_color="#601E88", font=("Arial Bold", 14))

entry1 = ctk.CTkEntry(main_frame, placeholder_text='Enter Integer', width=93, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
label3.place(x=30, y=284)
entry1.place(x=30, y=314)

# label4
label4 = ctk.CTkLabel(main_frame, text='Number 2', text_color="#601E88", font=("Arial Bold", 14))

entry2 = ctk.CTkEntry(main_frame, placeholder_text='Enter Integer', width=93, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
label4.place(x=160, y=284)
entry2.place(x=160, y=314)

# ************ variables declaration ************
toplevel = None

def invalid_input_toplevel(message: str):
    global toplevel
    if toplevel == None or not toplevel.winfo_exists():
        toplevel = ctk.CTkToplevel(app)
        toplevel.title('Error')
        toplevel.geometry('420x210')
        toplevel.resizable(0, 0)
        
        toplevel_img_data = Image.open(os.path.join(directory_path, 'images' + "/error.png"))
        toplevel_img = ctk.CTkImage(dark_image=toplevel_img_data, light_image=toplevel_img_data, size=(90, 90))
        toplevel_img = ctk.CTkLabel(master=toplevel, text="", image=toplevel_img)
        
        # ADD BELOW ATTRIBUTE text + RESULT VARIABLE FROM PROCESSING

        toplevel_heading = ctk.CTkLabel(master=toplevel, text=message, text_color="#601E88", font=("Arial Bold", 24))
        toplevel_side_heading = ctk.CTkLabel(master=toplevel, text="Enter Input According To Instructions!", text_color="#7E7E7E", font=("Arial Bold", 12))
        toplevel_img.place(x=24, y=54)
        toplevel_heading.place(x=140, y=60)
        toplevel_side_heading.place(x=140, y=110)

        toplevel.after(6000, toplevel.destroy)
    else:
        toplevel.focus()

def input_validation(input_algorithm: str, input_operation: str, input_num1: str, input_num2: str):
    if input_algorithm != 'CKKS':
        # expect INTEGER for num1 --> WORKS FOR 'FLOAT, STR' WRONG INPUT
        try:
            input_num1 = int(input_num1)
            # print("You entered:", user_input)
        except ValueError:
            # error window
            invalid_input_toplevel(f'You Entered: {input_num1}')

        # expect INTEGER for num2 --> WORKS FOR 'FLOAT, STR' WRONG INPUT
        try:
            input_num1 = int(input_num2)
            # print("You entered:", user_input)
        except ValueError:
            invalid_input_toplevel(f'You Entered: {input_num2}')
    else:
        # expect FLOAT for num1 --> WORKS FOR 'STR' WRONG INPUT
        try:
            input_num1 = float(input_num1)
            # print("You entered:", user_input)
        except ValueError:
            # error window
            invalid_input_toplevel(f'You Entered: {input_num1}')

        # expect FLOAT for num1 --> WORKS FOR 'STR' WRONG INPUT
        try:
            input_num1 = float(input_num2)
            # print("You entered:", user_input)
        except ValueError:
            invalid_input_toplevel(f'You Entered: {input_num2}')


def clear_output_director():
    path = os.path.join(directory_path, 'Output')
    for filename in os.listdir(path):
        if os.path.isfile(os.path.join(path, filename)):
            os.remove(os.path.join(path, filename))

# main button function
def submit_button(e):
    input_algorithm, input_operation = menu1.get(), menu2.get()
    input_num1, input_num2 = entry1.get(), entry2.get()

    # clear input fields in GUI
    menu1.current(0)
    menu2.current(0)
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    if input_algorithm == "CKKS":
        entry1.configure(placeholder_text='Enter Integer')
        entry2.configure(placeholder_text='Enter Integer')

    # validate user input
    input_validation(input_algorithm, input_operation, input_num1, input_num2)

    if input_algorithm == 'CKKS':
        input_num1, input_num2 = float(input_num1), float(input_num2)
    else:
        input_num1, input_num2 = int(input_num1), int(input_num2)
    result_dictionary = {
        'Algorithm': input_algorithm,
        'Operation': input_operation,
        'Number 1': input_num1,
        'Number 2': input_num2,
        'Result': ''
    }
    # process and store in files HERE
    clear_output_director()

    final_result = ''
    if input_algorithm == 'Paillier':
        final_result = paillier(input_algorithm, input_operation, input_num1, input_num2)
        result_dictionary['Result'] = final_result
    elif input_algorithm == 'BFV':
        final_result = bfv(input_algorithm, input_operation, input_num1, input_num2)
        result_dictionary['Result'] = str(final_result)
    elif input_algorithm == 'CKKS':
        final_result = ckks(input_algorithm, input_operation, input_num1, input_num2)
        final_result = "{:.9f}".format(final_result)
        result_dictionary['Result'] = str(final_result)
    elif input_algorithm == 'BGV':
        final_result = bgv(input_algorithm, input_operation, input_num1, input_num2)
        result_dictionary['Result'] = str(final_result)

    # 6. Finally make a file for result_dictionary
    with open(directory_path + '/Output/' + 'result.json', 'w') as file:
        json.dump(result_dictionary, file, indent=4)


    # 7. open successful top level and show message
    global toplevel
    if toplevel == None or not toplevel.winfo_exists():
        toplevel = ctk.CTkToplevel(app)
        toplevel.title('Output')
        toplevel.geometry('420x210')
        toplevel.resizable(0, 0)

        toplevel_img_data = Image.open(os.path.join(directory_path, 'images' + '/check.png'))
        toplevel_img = ctk.CTkImage(dark_image=toplevel_img_data, light_image=toplevel_img_data, size=(90, 90))
        toplevel_img = ctk.CTkLabel(master=toplevel, text="", image=toplevel_img)

        toplevel_heading = ctk.CTkLabel(master=toplevel, text="Output: " + str(final_result), text_color="#601E88", font=("Arial Bold", 24))
        toplevel_side_heading = ctk.CTkLabel(master=toplevel, text="See Output Folder For More Information", text_color="#7E7E7E", font=("Arial Bold", 12))
        toplevel_img.place(x=24, y=54)
        toplevel_heading.place(x=140, y=60)
        toplevel_side_heading.place(x=140, y=110)

        toplevel.after(6000, toplevel.destroy)
    else:
        toplevel.focus()

def paillier(input_algorithm, input_operation, input_num1, input_num2):
    temp_result, temp_result_cipher = '', ''
    # 1. generate keys
    public_key, private_key = phe.generate_paillier_keypair()
    # 2. encrypt
    input_num1, input_num2 = public_key.encrypt(input_num1), public_key.encrypt(input_num2)
    # 3. operation
    if input_operation == 'Addition':
        temp_result = input_num1 + input_num2
    elif input_operation == 'Subtraction':
        temp_result = input_num1 - input_num2
    elif input_operation == 'Scalar Multiplication':
        # second number is decrypted as it is Scalar Multiplication
        temp_result = input_num1 * private_key.decrypt(input_num2)
    
    # 4. save keys
    keys_dictionary = {
        'Public Key (n)': public_key.n,
        'Private Key (p)': private_key.p,
        'Private Key (q)': private_key.q
    }
    with open(directory_path + '/Output/' + 'keys.json', 'w') as file:
        json.dump(keys_dictionary, file, indent=4)

    # 5. temp_result, temp_result_cipher
    temp_result, temp_result_cipher = private_key.decrypt(temp_result), temp_result.ciphertext()
    # only for Paillier save in file
    with open(directory_path + '/Output/' + 'encrypted_result.txt', 'w') as file:
        file.write(str(temp_result_cipher))
    
    return temp_result

def bfv(input_algorithm, input_operation, input_num1, input_num2):
    temp_result = ''
    # 1. generate keys
    HE = Pyfhel()           # Creating empty Pyfhel object
    bfv_params = {
    'scheme': 'BFV',    # can also be 'bfv'
    'n': 2**13,         # Polynomial modulus degree, the num. of slots per plaintext,
                        #  of elements to be encoded in a single ciphertext in a
                        #  2 by n/2 rectangular matrix (mind this shape for rotations!)
                        #  Typ. 2^D for D in [10, 16]
    't': 65537,         # Plaintext modulus. Encrypted operations happen modulo t
                        #  Must be prime such that t-1 be divisible by 2^N.
    't_bits': 20,       # Number of bits in t. Used to generate a suitable value
                        #  for t. Overrides t if specified.
    'sec': 128,         # Security parameter. The equivalent length of AES key in bits.
                        #  Sets the ciphertext modulus q, can be one of {128, 192, 256}
                        #  More means more security but also slower computation.
    }
    HE.contextGen(**bfv_params)  # Generate context for bfv scheme
    HE.keyGen()             # Key Generation: generates a pair of public/secret keys
    HE.rotateKeyGen()       # Rotate key generation --> Allows rotation/shifting
    HE.relinKeyGen()        # Relinearization key generation
    # 2. encrypt
    input_num1, input_num2 = HE.encrypt(input_num1), HE.encrypt(input_num2)
    # 3. operation
    if input_operation == 'Addition':
        temp_result = input_num1 + input_num2
    elif input_operation == 'Subtraction':
        temp_result = input_num1 - input_num2
    elif input_operation == 'Multiplication':
        temp_result = input_num1 * input_num2
    elif input_operation == 'Exponentation':
        temp_result = input_num1 ** HE.decrypt(input_num2)[0]
    
    # 4. save keys
    HE.save_context(directory_path + '/Output/' + 'context.txt')
    HE.save_public_key(directory_path + '/Output/' + 'public_key.txt')
    HE.save_secret_key(directory_path + '/Output/' + 'secret_key.txt')
    HE.save_relin_key(directory_path + '/Output/' + 'relin_key.txt')
    HE.save_rotate_key(directory_path + '/Output/' + 'rotate_key.txt')
    temp_result.save(directory_path + '/Output/' + 'encrypted_result.txt')

    # 5. temp_result, temp_result_cipher
    temp_result = HE.decrypt(temp_result)[0]
    return temp_result

def ckks(input_algorithm, input_operation, input_num1, input_num2):
    temp_result = ''
    # 1. generate keys
    HE = Pyfhel()           # Creating empty Pyfhel object
    ckks_params = {
        'scheme': 'CKKS',   # can also be 'ckks'
        'n': 2**14,         # Polynomial modulus degree. For CKKS, n/2 values can be
                            #  encoded in a single ciphertext.
                            #  Typ. 2^D for D in [10, 15]
        'scale': 2**30,     # All the encodings will use it for float->fixed point
                            #  conversion: x_fix = round(x_float * scale)
                            #  You can use this as default scale or use a different
                            #  scale on each operation (set in HE.encryptFrac)
        'qi_sizes': [60, 30, 30, 30, 60] # Number of bits of each prime in the chain.
                            # Intermediate values should be  close to log2(scale)
                            # for each operation, to have small rounding errors.
    }
    HE.contextGen(**ckks_params)  # Generate context for ckks scheme
    HE.keyGen()             # Key Generation: generates a pair of public/secret keys
    HE.rotateKeyGen()       # Rotate key generation --> Allows rotation/shifting
    HE.relinKeyGen()        # Relinearization key generation
    # 2. encrypt
    input_num1, input_num2 = HE.encrypt(input_num1), HE.encrypt(input_num2)
    # 3. operation
    if input_operation == 'Addition':
        temp_result = input_num1 + input_num2
    elif input_operation == 'Subtraction':
        temp_result = input_num1 - input_num2
    elif input_operation == 'Multiplication':
        temp_result = input_num1 * input_num2
    
    # 4. save keys
    HE.save_context(directory_path + '/Output/' + 'context.txt')
    HE.save_public_key(directory_path + '/Output/' + 'public_key.txt')
    HE.save_secret_key(directory_path + '/Output/' + 'secret_key.txt')
    HE.save_relin_key(directory_path + '/Output/' + 'relin_key.txt')
    HE.save_rotate_key(directory_path + '/Output/' + 'rotate_key.txt')
    temp_result.save(directory_path + '/Output/' + 'encrypted_result.txt')

    # 5. temp_result, temp_result_cipher
    temp_result = HE.decrypt(temp_result)[0]
    return temp_result

def bgv(input_algorithm, input_operation, input_num1, input_num2):
    temp_result = ''
    # 1. generate keys
    HE = Pyfhel()           # Creating empty Pyfhel object

    # HE.contextGen(scheme='bgv', n=2**14, t_bits=20)  # Generate context for 'bfv'/'bgv'/'ckks' scheme

    bgv_params = {
        'scheme': 'BGV',    # can also be 'bgv'
        'n': 2**13,         # Polynomial modulus degree, the num. of slots per plaintext,
                            #  of elements to be encoded in a single ciphertext in a
                            #  2 by n/2 rectangular matrix (mind this shape for rotations!)
                            #  Typ. 2^D for D in [10, 16]
        't': 65537,         # Plaintext modulus. Encrypted operations happen modulo t
                            #  Must be prime such that t-1 be divisible by 2^N.
        't_bits': 20,       # Number of bits in t. Used to generate a suitable value
                            #  for t. Overrides t if specified.
        'sec': 128,         # Security parameter. The equivalent length of AES key in bits.
                            #  Sets the ciphertext modulus q, can be one of {128, 192, 256}
                            #  More means more security but also slower computation.
    }
    HE.contextGen(**bgv_params)  # Generate context for bgv scheme
    HE.keyGen()             # Key Generation: generates a pair of public/secret keys
    HE.rotateKeyGen()       # Rotate key generation --> Allows rotation/shifting
    HE.relinKeyGen()        # Relinearization key generation
    # 2. encrypt
    input_num1, input_num2 = HE.encrypt(input_num1), HE.encrypt(input_num2)
    # 3. operation
    if input_operation == 'Addition':
        temp_result = input_num1 + input_num2
    elif input_operation == 'Subtraction':
        temp_result = input_num1 - input_num2
    elif input_operation == 'Multiplication':
        temp_result = input_num1 * input_num2
    elif input_operation == 'Exponentation':
        temp_result = input_num1 ** HE.decrypt(input_num2)[0]
    
    # 4. save keys
    HE.save_context(directory_path + '/Output/' + 'context.txt')
    HE.save_public_key(directory_path + '/Output/' + 'public_key.txt')
    HE.save_secret_key(directory_path + '/Output/' + 'secret_key.txt')
    HE.save_relin_key(directory_path + '/Output/' + 'relin_key.txt')
    HE.save_rotate_key(directory_path + '/Output/' + 'rotate_key.txt')
    temp_result.save(directory_path + '/Output/' + 'encrypted_result.txt')

    # 5. temp_result, temp_result_cipher
    temp_result = HE.decrypt(temp_result)[0]
    return temp_result    


btn = ctk.CTkButton(main_frame, text="Perform Operation", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225)
btn.bind('<Button-1>', submit_button)
btn.bind('<Button-2>', submit_button)
btn.bind('<Button-3>', submit_button)
btn.bind('<Return>', submit_button)
btn.place(x=30, y=384)


app.mainloop()