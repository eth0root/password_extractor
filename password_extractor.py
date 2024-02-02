import re
import os
import sys

class PasswordExtractor:
    def __init__(self):
        self.captured_passwords = set()
        self.excluded_passwords = set()

    @staticmethod
    def clear_terminal():
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def display_banner():
        PasswordExtractor.clear_terminal()
        banner = '''
\033[1;32m
+==================================================+
| Autor: Marcio Cruz                               |
| Sobre: EXTRATOR DE SENHAS DE DB EMAIL|SENHA      |
|                                                  |
| Linkedin: linkedin.com/in/marciosecurity         |
| Telegram: @eth0root                              |
+==================================================+

\033[1;m
        '''
        print(banner)

    @staticmethod
    def is_md5_or_sha(password):
        return re.match(r'^[a-fA-F0-9]{32}$|^[a-fA-F0-9]{40}$', password)

    def extract_unique_passwords(self, input_filename, output_filename):
        passwords = set()
        excluded_count = 0
        print()

        try:
            with open(input_filename, 'r', encoding="latin-1") as file:
                total_lines = sum(1 for _ in file)
                file.seek(0)  # Reiniciar o cursor para o início do arquivo

                for idx, line in enumerate(file, start=1):
                    combo = re.split(r'\||:', line.strip())
                    if len(combo) >= 2:
                        email = combo[0].strip()
                        password = combo[1].strip()

                        cleaned_password = password.strip()
                        if cleaned_password and not PasswordExtractor.is_md5_or_sha(cleaned_password):
                            if len(cleaned_password) <= 20:
                                passwords.add(cleaned_password)
                            else:
                                self.excluded_passwords.add(cleaned_password)
                                excluded_count += 1

                    # Atualizar a barra de progresso
                    self.print_progress_bar(idx, total_lines)

            with open(output_filename, 'w', encoding="utf-8") as file:
                file.write('\n'.join(passwords))
            print()
            print(f'\nSenhas capturadas: {len(passwords)}')
            print(f'Senhas excluídas (MD5 ou SHA): {excluded_count}')
            print(f"Senhas únicas (excluindo MD5 e SHA e com até 20 caracteres) salvas no arquivo '{output_filename}'.\n")

        except FileNotFoundError:
            print(f"\nErro Crítico -> Arquivo não encontrado: '{input_filename}'\n")
        except Exception as e:
            print(f"\nErro Crítico -> {e}\n")

    @staticmethod
    def print_progress_bar(iteration, total, length=50):
        percent = int(iteration / total * 100)
        filled_length = int(length * iteration // total)
        bar = f"[{'#' * filled_length}{'-' * (length - filled_length)}] {percent}%\r"
        sys.stdout.write(bar)
        sys.stdout.flush()

    def start_extraction(self):
        try:
            while True:
                # Obter o nome do arquivo de entrada do usuário
                input_filename = input("Digite o nome do arquivo de entrada: ").strip()

                if not input_filename:
                    print("\nErro Crítico -> Nenhum diretório fornecido. Tente novamente.\n")
                    continue

                # Nome do arquivo de saída para as senhas
                output_filename = 'senhas.txt'

                # Extração das senhas únicas
                self.extract_unique_passwords(input_filename, output_filename)

        except KeyboardInterrupt:
            response = input("\nVocê pressionou Ctrl+C. Deseja realmente finalizar o programa? (S/N): ").strip().lower()
            if response == 's':
                print("\nPrograma finalizado pelo usuário.")
                exit()
            else:
                print("\nContinuando a execução do script...\n")
                self.start_extraction()
        except Exception as ee:
            print(f'\n\n      Erro Crítico -> {ee}')
            input()
            exit()

if __name__ == "__main__":
    password_extractor = PasswordExtractor()
    password_extractor.display_banner()
    password_extractor.start_extraction()
