===============================================================================
TUTORIAL: CRIAR E CENTRALIZAR A BIBLIOTECA E COMANDO CLI (git_dgp)
===============================================================================

1. ESTRUTURA DA PASTA DO PROJETO LOCAL
-------------------------------------------------------------------------------
Crie uma pasta com o nome git_dgp e coloque os dois arquivos dentro dela:

git_dgp/
├── git.py          <-- O seu código da ferramenta Git
└── pyproject.toml  <-- Arquivo de configuração da biblioteca Python


2. CONTEÚDO DO ARQUIVO pyproject.toml
-------------------------------------------------------------------------------
(Salve o texto abaixo exatamente com o nome pyproject.toml na raiz da pasta)

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "git_dgp"
version = "0.1.0"
description = "Assistente automatizado de Git e GitHub"
authors = [{ name = "Davi" }]
py-modules = ["git"]

[project.scripts]
git_dgp = "git:main"


3. PUBLICAR NO GITHUB
-------------------------------------------------------------------------------
Crie o repositório público ou privado no GitHub com o nome git_dgp e suba 
a pasta criada:

URL do repositório: https://github.com/davigopi/git_dgp


4. INSTALAR A FERRAMENTA NO COMPUTADOR
-------------------------------------------------------------------------------
Abra qualquer terminal no seu computador e execute:

pip install git+https://github.com/davigopi/git_dgp.git


5. COMO USAR NOS SEUS PROJETOS
-------------------------------------------------------------------------------
- Via terminal (em qualquer pasta de projeto React Native, Python, etc.):
  Basta abrir o terminal na pasta desejada e digitar:

  git_dgp

- Via importação dentro de scripts Python futuros:
  from git import run_command, create_gitignore_if_missing


6. ATUALIZAR A FERRAMENTA NO FUTURO
-------------------------------------------------------------------------------
Sempre que fizer uma melhoria no script original, suba as alterações para o 
GitHub no repositório git_dgp e execute o comando abaixo no terminal para 
atualizar no seu computador:

pip install --upgrade git+https://github.com/davigopi/git_dgp.git
===============================================================================