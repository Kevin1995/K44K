import functions
import time
#import CPU_RAM_Check

# NOTES
# CPU_RAM_Check.main() and import CPU_RAM_Check IS COMMENTED OUT - THE ALGORITHM RUND A LOT FASTER WITHOUT IT
# THAT METHOD IS USED TO CHECK CPU AND RAM USAGE

# PARAMATERS (16, 24 OR 32 CHARACTERS/BITS LONG)
plaintext="ThisIsDemoVidShowingTheAlgorithm"
key="5qCYRLEBe,khnHrZ-Lh13%PF5=z~2+Cw"
ciphertext, rot_cipher_key, decrypted_plaintext, decrypted_rot_key = "", "", "", ""

start_time = time.time()
def encrypt(plaintext, key):
    #print("Resource Usage at start of encryption")
    #CPU_RAM_Check.main()
    
    # Store postions and keys
    orientation, keys_array = [], []

    # Rotation Key
    rot_key = ""
    
    # KEY SCHEDULE WILL MAKE N ROUNDS FOR THE KEY BASED ON THE LENGTH
    # THE KEY IS HEXED FOR THE PURPOSES OF THE KEY SCHEDULE
    # IT IS THEN UNHEXED ONCE THE FUNCTION IS FINISHED
    print("Key Schedule Round Results - Encryption")
    keys_array = functions.key_schedule(key, keys_array)


    # CREATE THE CUBE
    up_face, down_face, left_face, front_face, right_face, back_face = functions.create_cube()

    # NOW THAT WE CAN GENERATE THE VALUES FOR EACH FACE
    # WE DO OUR ROUNDS WITH THE KEYS FROM KEY_SCEHEDULE
    # THEN WE APPLY THE CIPHERTEXT VALUES TO THE FACES
    ciphertext = functions.aes_operation(plaintext, keys_array)

    print("Ciphertext after AES Operation (Array Format)")
    print(ciphertext)
    print("")

    # RANDOM ORIENTATION
    up_face, down_face, left_face, front_face, right_face, back_face, ciphertext, orientation = functions.random_orientation(up_face, down_face, left_face, front_face, right_face, back_face, ciphertext, orientation)

    # SCRAMLE CUBE AND RETURN THE ROTATION KEY
    up_face, down_face, left_face, front_face, right_face, back_face, rot_key, ciphertext = functions.scramble_rot_key(up_face, down_face, left_face, front_face, right_face, back_face, orientation, rot_key, ciphertext)
    
    # XOR THE ROT AND CIPHER KEY TOGETHER
    rot_cipher_key = functions.rot_cipher_key(rot_key, key)

    #print("Resource Usage at end of encryption")
    #CPU_RAM_Check.main()

    return rot_cipher_key, ciphertext

def decrypt(rot_cipher_key, key, ciphertext):
    #print("Resource Usage at start of decryption")
    #CPU_RAM_Check.main()

    # Store movements + postions from ROT key
    movements, position, keys_array = [], [], []

    # Create the Cube
    up_face, down_face, left_face, front_face, right_face, back_face = functions.create_cube()
    
    # Uncover the ROT key from our ROT_Cipher merged key and our normal Cipher key
    decrypted_rot_key = functions.rot_from_rck_c(rot_cipher_key, key)

    print("\nRotation Key after XOR of ROT_CIP_KEY and ORIGINAL KEY")
    print(decrypted_rot_key)
    print("")

    # Now we split the ROT key into the cube movements
    # and how the ciphertext is oriented befoe the scramble
    movements, position = functions.get_move_pos(movements, position, decrypted_rot_key)
    print("Movements and Positions split from Rotation Key\n")
    print("Movements")
    print(f"{movements}\n")
    print("Position")
    print(f"{position}\n")

    # Assign the Ciphertext to the cube - so when we descramble it will show as it started.
    up_face, down_face, left_face, front_face, right_face, back_face = functions.assign_ciphertext_to_cube(up_face, down_face, left_face, front_face, right_face, back_face, position, ciphertext)

    print("4x4 Rubiks Cube after placing the Ciphertext before descrambling")
    print("Up Face")
    print(f"{up_face} \n")
    print("Down Face")
    print(f"{down_face} \n")
    print("Left Face")
    print(f"{left_face} \n")
    print("Front Face")
    print(f"{front_face} \n")
    print("Right Face")
    print(f"{right_face} \n")
    print("Back Face")
    print(f"{back_face} \n")

    # DESCRAMBLE THE CUBE
    up_face, down_face, left_face, front_face, right_face, back_face, ciphertext = functions.key_cube_scramble(up_face, down_face, left_face, front_face, right_face, back_face, movements)
    
    print("Key Schedule Round Results - Decryption")
    # DO KEY SCHEDULE AGAIN
    keys_array = functions.key_schedule(key, keys_array)
    
    # DO INVERSE OF faces_operation function
    decrypted_plaintext = functions.inv_aes_operation(ciphertext, keys_array)

    #print("Resource Usage at end of decryption")
    #CPU_RAM_Check.main()

    return decrypted_plaintext, decrypted_rot_key

print("ENCRYPTION RESULTS")
rot_cipher_key, ciphertext = encrypt(plaintext, key)
print("ROT_CIP_KEY (XORING ROT_KEY AND ORIGINAL KEY):")
print(rot_cipher_key + '\n')
print("ENCRYPTION ENDED" + '\n')

print("DECRYPTION STARTED")
decrypted_plaintext, decrypted_rot_key = decrypt(rot_cipher_key, key, ciphertext)

print(f"Original Plaintext after Decryption: " + decrypted_plaintext + '\n')
# print("ROT_Key (NOT HEXED)(Uncovered by ROT_CIP_KEY and Key): " + decrypted_rot_key + '\n')
print("DECRYPTION ENDED" + '\n')

print("Process finished --- %s seconds ---" % (time.time() - start_time))