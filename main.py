from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Função para cifrar a mensagem
def encrypt_message(key, plaintext):
    # Inicializa o cifrador AES no modo CBC
    cipher = AES.new(key, AES.MODE_CBC)
    # Gera o texto cifrado com preenchimento
    ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
    # Retorna o texto cifrado e o vetor de inicialização (IV)
    return cipher.iv, ciphertext

# Função para decifrar a mensagem
def decrypt_message(key, iv, ciphertext):
    # Inicializa o decifrador AES com o mesmo IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # Remove o preenchimento e retorna o texto decifrado
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode('utf-8')

# Exemplo de uso
def main():
    # Chave de 256 bits (32 bytes)
    key = get_random_bytes(32)
    print(f"Chave secreta (hex): {key.hex()}")
    
    # Lê a mensagem do usuário
    plaintext = input("Digite a mensagem que deseja cifrar: ")
    print(f"Mensagem original: {plaintext}")
    
    # Cifrar a mensagem
    iv, ciphertext = encrypt_message(key, plaintext)
    print(f"Texto cifrado (hex): {ciphertext.hex()}")
    print(f"IV (hex): {iv.hex()}")
    
    # Decifrar a mensagem
    decrypted_text = decrypt_message(key, iv, ciphertext)
    print(f"Texto decifrado: {decrypted_text}")

if __name__ == "__main__":
    main()
