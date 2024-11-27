```markdown
# Criptografia Simétrica com AES em Python

Este projeto implementa um algoritmo de cifragem e decifragem de mensagens utilizando o AES (Advanced Encryption Standard), um padrão amplamente utilizado para criptografia simétrica. O programa recebe uma mensagem diretamente do usuário, cifra utilizando uma chave gerada aleatoriamente e, em seguida, decifra a mensagem para demonstrar o funcionamento do algoritmo.

## 📋 Requisitos

Certifique-se de ter o Python instalado em sua máquina. Além disso, instale a biblioteca `pycryptodome`, que é utilizada para a implementação do AES. Para instalá-la, execute:

```bash
pip install pycryptodome
```

## 🛠️ Funcionamento

O código utiliza o algoritmo AES no modo CBC (Cipher Block Chaining) para garantir maior segurança. A chave é gerada automaticamente, e o texto é ajustado para múltiplos de 16 bytes utilizando preenchimento (padding).

### Principais funções

1. **`encrypt_message(key, plaintext)`**
   - Recebe uma chave secreta e um texto a ser cifrado.
   - Gera o texto cifrado e o vetor de inicialização (IV) para o processo de decifragem.

2. **`decrypt_message(key, iv, ciphertext)`**
   - Recebe a chave secreta, o IV e o texto cifrado.
   - Retorna o texto original decifrado.

### Entrada do usuário

O programa solicita ao usuário que digite a mensagem a ser cifrada por meio do prompt. A mensagem pode ter qualquer comprimento, mas será ajustada automaticamente para um múltiplo do tamanho do bloco (16 bytes).

### Exemplo de execução

1. O programa gera uma chave aleatória de 256 bits.
2. Solicita ao usuário a mensagem que deseja cifrar.
3. Exibe:
   - A chave secreta gerada.
   - O texto cifrado (em formato hexadecimal).
   - O vetor de inicialização (IV) usado.
   - A mensagem original decifrada.

## 🚀 Como Executar

1. Salve o código no arquivo `aes_encryption.py`.
2. Execute o programa no terminal:

```bash
python aes_encryption.py
```

3. Digite a mensagem que deseja cifrar quando solicitado.

Exemplo de saída:

```
Chave secreta (hex): aabbccddeeff00112233445566778899aabbccddeeff00112233445566778899
Digite a mensagem que deseja cifrar: Mensagem de teste.
Mensagem original: Mensagem de teste.
Texto cifrado (hex): 89a8e982b6f4c3e0b5e93b8e9a1f1f6e489ba78abcf50ff2d15e56789a6b3c4f
IV (hex): aabbccddeeff00112233445566778899
Texto decifrado: Mensagem de teste.
```
![image](https://github.com/user-attachments/assets/faf538f8-2db4-42b4-98c4-39cd9df60140)


## 🛡️ Segurança

- **Chave:** A chave utilizada tem 256 bits. A chave e o vetor de inicialização (IV) devem ser armazenados com segurança, pois são necessários para decifrar o texto.
- **Preenchimento (Padding):** Mensagens que não são múltiplos de 16 bytes são automaticamente ajustadas para atender ao tamanho do bloco AES.

## 📂 Estrutura do Código

O código está organizado da seguinte forma:

- **Geração da chave:** Chave secreta gerada automaticamente utilizando `get_random_bytes`.
- **Criptografia:** Utiliza o AES no modo CBC com preenchimento.
- **Decifragem:** Remove o preenchimento e retorna o texto original.

## 🔗 Recursos

- Documentação do PyCryptodome: [https://www.pycryptodome.org/](https://www.pycryptodome.org/)

## 📝 Licença

Este projeto é livre para uso e modificação. Sinta-se à vontade para adaptá-lo às suas necessidades!
```
