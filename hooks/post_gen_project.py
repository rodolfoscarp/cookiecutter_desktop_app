import subprocess
import sys
import os

# O diretório de trabalho atual do hook é a raiz do projeto gerado.
project_slug = "{{ cookiecutter.project_slug }}"

print(f"DEBUG: Iniciando script post_gen_project.py para '{project_slug}'")
print(f"DEBUG: Current Working Directory: {os.getcwd()}")  # Verifique o CWD

print(f"Iniciando configuração do projeto '{project_slug}' com Poetry e Git...")

try:
    # --- Parte 1: Instalar dependências do projeto com poetry install ---
    print("Executando 'poetry install' para configurar as dependências do projeto...")
    result_install = subprocess.run(
        ["poetry", "install"], check=True, capture_output=True, text=True
    )
    print("Dependências do projeto instaladas com sucesso usando Poetry.")

    # --- Parte 2: Adicionar o plugin poetry-plugin-export à instalação do Poetry ---
    print(
        "Adicionando 'poetry-plugin-export' à sua instalação do Poetry (se ainda não estiver presente)..."
    )
    result_plugin = subprocess.run(
        ["poetry", "self", "add", "poetry-plugin-export"],
        check=False,
        capture_output=True,
        text=True,
    )

    if result_plugin.returncode == 0:
        print("Plugin 'poetry-plugin-export' adicionado com sucesso.")
    elif (
        "already installed" in result_plugin.stderr
        or "already installed" in result_plugin.stdout
    ):
        print(
            "Plugin 'poetry-plugin-export' já estava instalado. Nenhuma ação necessária."
        )
    else:
        print(
            f"Aviso: Não foi possível adicionar o plugin 'poetry-plugin-export'.",
            file=sys.stderr,
        )
        print(f"Stdout (plugin): {result_plugin.stdout}", file=sys.stderr)
        print(f"Stderr (plugin): {result_plugin.stderr}", file=sys.stderr)
        print(
            "O usuário precisará instalá-lo manualmente se quiser usar 'poetry export'."
        )

    # --- Parte 3: Inicializar um repositório Git e renomear o branch principal ---
    print("Inicializando repositório Git...")
    subprocess.run(["git", "init"], check=True, capture_output=False)
    subprocess.run(["git", "add", "."], check=True, capture_output=False)
    subprocess.run(
        ["git", "commit", "-m", "Initial commit from Cookiecutter template."],
        check=True,
        capture_output=False,
    )

    # Renomear o branch 'master' (padrão do git init) para 'main'
    print("Renomeando o branch 'master' para 'main'...")
    subprocess.run(
        ["git", "branch", "-M", "main"], check=True, capture_output=False
    )  # -M força a renomeação
    print("Repositório Git inicializado e branch principal definido como 'main'.")

except FileNotFoundError:
    print(
        "Erro: 'poetry' ou 'git' não encontrado. Certifique-se de que estão instalados e no PATH.",
        file=sys.stderr,
    )
    print("Não foi possível configurar o projeto automaticamente.", file=sys.stderr)
    sys.exit(1)
except subprocess.CalledProcessError as e:
    print(f"Erro ao executar comando: {e}", file=sys.stderr)
    print(f"Detalhes do erro:", file=sys.stderr)
    print(f"Stdout: {e.stdout}", file=sys.stderr)
    print(f"Stderr: {e.stderr}", file=sys.stderr)
    print(
        "A configuração do projeto falhou. Verifique as mensagens de erro acima.",
        file=sys.stderr,
    )
    sys.exit(1)
except Exception as e:
    print(
        f"Ocorreu um erro inesperado durante a configuração do projeto: {e}",
        file=sys.stderr,
    )
    sys.exit(1)

# --- PASSO 4: Instalar os hooks pre-commit ---
print("\n--- PASSO 4: Instalação dos Hooks Pre-Commit ---")
print("DEBUG: Executando 'poetry run pre-commit install'...")
try:
    result_precommit_install = subprocess.run(
        ["poetry", "run", "pre-commit", "install"],
        check=True,  # Mantenha check=True para falhar se a instalação falhar
        capture_output=True,
        text=True,
    )
    print("DEBUG: 'pre-commit install' concluído.")
    print("DEBUG: Stdout 'pre-commit install':\n" + result_precommit_install.stdout)
    if result_precommit_install.stderr:
        print("DEBUG: Stderr 'pre-commit install':\n" + result_precommit_install.stderr)
    print("Hooks pre-commit instalados com sucesso.")
except subprocess.CalledProcessError as e:
    print(f"ERRO: Falha ao instalar hooks pre-commit: {e.cmd}", file=sys.stderr)
    print(f"Stdout: {e.stdout}", file=sys.stderr)
    print(f"Stderr: {e.stderr}", file=sys.stderr)
    sys.exit(1)  # Saia com erro se a instalação do hook falhar

print(f"Configuração automática do projeto '{project_slug}' concluída.")
print("Para começar, você pode ativar o ambiente virtual com 'poetry shell'")
print("ou executar comandos diretamente com 'poetry run <comando>'.")
