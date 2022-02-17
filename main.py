#Binary Encoder/Decoder made by Floating_Around
#import binasciiencod
choice = input("Encode or Decode?")
if choice == "Encode" or choice == "encode":
    textToEncode = input("Text to encode: ")
    #encode
    byte_array = textToEncode.encode()
    binary_int = int.from_bytes(byte_array, "big")
    binary_string = bin(binary_int)
    # Getting the converted binary characters
    print(binary_string)
elif choice == "Decode" or choice == "decode":
    binary = input("Binary to decode: ")
    #binary to ascii (decode)
    #binary to convert
    binary_int = int(binary, 2)
    byte_number = binary_int.bit_length() + 7 // 8
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    print(ascii_text)
print("Done!")