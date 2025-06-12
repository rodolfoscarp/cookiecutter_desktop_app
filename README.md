# Template para Criação de aplicativos Desktop

Este projeto é um template para criação de aplicativos desktop utilizando Python e bibliotecas como Poetry, loguru, pyinstaller e ttkbootstrap.

## Objetivo

O objetivo deste projeto é fornecer uma estrutura básica para o desenvolvimento de aplicativos desktop em Python, utilizando as melhores práticas e ferramentas disponíveis.

## Dependências

- `Python >= 3.12`
- Gerenciador de Pacotes: `Poetry`

### Bibliotecas utilizadas

- `loguru`: biblioteca de logging
- `pyinstaller`: ferramenta de empacotamento de aplicativos
- `ttkbootstrap`: biblioteca de interface gráfica

### Dependências de Desenvolvimento

- `pytest`: framework de testes
- `black`: formatação de código
- `isort`: organização de imports
- `taskipy`: gerenciamento de tarefas
- `pre-commit`: executa ações antesde cada commit

## Funcionalidades

- Estrutura básica de aplicativo desktop
- Utilização de Poetry como gerenciador de pacotes
- Teste com Pytest
- Logging com loguru
- Empacotamento com pyinstaller
- Interface gráfica com ttkbootstrap
- Configuração de Git para versionamento
- Configuração de GitHub Actions para Empacotamento com pyinstaller
- Pre-commit formatação do codigo e exportação dos pacote para arquivo requirements.txt

## Instruções de Uso

- Instalar o cookiecutter: `pip install cookiecutter`
- Execute: `cookiecutter https://github.com/rodolfoscarp/cookiecutter_desktop_app.git`
- Preencha as informações.
- Ativar o ambiente virtual: `poetry shell`

### Scripts

Estes scripts são pré configurados utilizando a biblioteca `taskipy`.

- `task pytest`: Executa os testes utilizando `Pytest`
- `task format`: formata o codigo utilizando `black` e `isort`"
- `task freeze`: gera o arquivo `requirements.txt` apenas com as dependencias de produção.
- `task build`: gera o executavel utilizando `pyinstaller`

## Licença

Este projeto é licenciado sob a licença MIT.

## Contribuição

Contribuições são bem-vindas! Se você tiver alguma sugestão ou correção, por favor, abra uma issue ou envie um pull request.
