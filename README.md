# Password Extractor

Este script em Python foi desenvolvido para extrair senhas únicas de arquivos de texto, removendo senhas no formato MD5 ou SHA e excluindo aquelas com mais de 20 caracteres. É útil para extrair senhas de arquivos de dados.

## Funcionalidades

**1. Extração de Senhas Únicas:** O script percorre um arquivo de entrada, extrai senhas únicas, exclui senhas no formato MD5 ou SHA e elimina aquelas com mais de 20 caracteres.

**2. Exclusão de Senhas MD5 e SHA:** Senhas no formato MD5 ou SHA não são incluídas na saída.

**3. Controle de Comprimento:** Senhas com mais de 20 caracteres são excluídas da saída.

**4. Interatividade com o Usuário:** O usuário fornece o nome do arquivo de entrada.

**5. Finalização Controlada:** Ao pressionar Ctrl+C durante a execução, o script pergunta se o usuário deseja finalizar o programa.

## Como Usar

**1. Requisitos:**

- Python 3.x instalado.

**2. Execução:**

- Execute o script no terminal ou prompt de comando.
- O script solicitará o nome do arquivo de entrada.
- As senhas únicas serão extraídas e salvas em um arquivo chamado `senhas.txt`.

**3. Exemplo:**

    ```bash
    $ python password_extractor.py
    Digite o nome do arquivo de entrada: dados.txt
    Senhas capturadas: 120
    Senhas excluídas (MD5 ou SHA): 5
    Senhas únicas (até 20 caracteres) salvas no arquivo 'senhas.txt'.
    ```

**4. Finalização Controlada:**

- Ao pressionar Ctrl+C, o script pergunta se deseja realmente finalizar o programa.

**Notas Importantes**

- Certifique-se de que o arquivo de entrada contém senhas no formato desejado.
- Senhas MD5 ou SHA e com mais de 20 caracteres são excluídas da saída.

Este script é uma ferramenta útil para extrair senhas únicas de arquivos de dados, excluindo aquelas no formato MD5 ou SHA e com comprimento excessivo.
