# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}

## Introdução

Este template é um projeto básico para criar aplicativos desktop com Python e Poetry. Ele fornece uma estrutura básica para o desenvolvimento de aplicativos desktop, utilizando as melhores práticas e ferramentas disponíveis.

## Requisitos

- `Python >= 3.12`
- Gerenciador de Pacotes: `Poetry`

### Bibliotecas utilizadas

- `loguru`: biblioteca de logging
- `pyinstaller`: ferramenta de empacotamento de aplicativos
- `ttkbootstrap`: biblioteca de interface gráfica

## Features

- Estrutura básica de aplicativo desktop
- Utilização de `Poetry` como gerenciador de pacotes
- Teste com `Pytest`
- Logging com `loguru`
- Empacotamento com `pyinstaller`
- Interface gráfica com `ttkbootstrap`
- Configuração de Git para versionamento
- Configuração de GitHub Actions para Empacotamento com `pyinstaller`
- `Pre-commit` formatação do código e exportação dos pacote para arquivo requirements.txt

## Estrutura do Projeto

- _src/_: diretório fonte do projeto
  - *__init__.py*: arquivo de inicialização do projeto
  - utils/: diretório de utilitários
    - _logs.py_: arquivo de configuração de logs
    - _loading.py_: arquivo de configuração de loading
    - _resources.py_: arquivo de configuração de recursos
  - _ui/_: diretório de interface gráfica
    - _main.py_: arquivo de interface gráfica principal
- _main.py_: arquivo principal do projeto
- _README.md_: arquivo de documentação do projeto
- _LICENSE.md_: arquivo de licença do projeto

## Testes

- Utilize o framework de testes Pytest para desenvolver testes para o aplicativo.
- Execute os testes utilizando o comando task pytest

## Empacotamento

- Utilize a ferramenta `pyinstaller` para empacotar o aplicativo.
- Execute o comando `task build` para empacotar o aplicativo
