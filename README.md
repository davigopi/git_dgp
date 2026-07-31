TUTORIAL: CRIAR E CENTRALIZAR A BIBLIOTECA E COMANDO CLI (git_dgp)
===============================================================================
---------------------------------------------------------
## 1. ESTRUTURA DA PASTA DO PROJETO LOCAL
---------------------------------------------------------
Crie uma pasta com o nome git_dgp e coloque os dois arquivos dentro dela:
'''
git_dgp/

├── git.py          <-- O seu código da ferramenta Git

└── pyproject.toml  <-- Arquivo de configuração da biblioteca Python
'''



---------------------------------------------------------
## 2. CONTEÚDO DO ARQUIVO pyproject.toml
---------------------------------------------------------
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

---------------------------------------------------------
## 3. PUBLICAR NO GITHUB
---------------------------------------------------------
Crie o repositório público ou privado no GitHub com o nome git_dgp e suba 
a pasta criada:

URL do repositório: https://github.com/davigopi/git_dgp

---------------------------------------------------------
## 4. INSTALAR A FERRAMENTA NO COMPUTADOR
---------------------------------------------------------
Abra qualquer terminal no seu computador e execute:

pip install git+https://github.com/davigopi/git_dgp.git

---------------------------------------------------------
## 5. COMO USAR NOS SEUS PROJETOS
---------------------------------------------------------
- Via terminal (em qualquer pasta de projeto React Native, Python, etc.):
  Basta abrir o terminal na pasta desejada e digitar:

  git_dgp

- Via importação dentro de scripts Python futuros:
  from git import run_command, create_gitignore_if_missing

---------------------------------------------------------
## 6. ATUALIZAR A FERRAMENTA NO FUTURO
---------------------------------------------------------
Sempre que fizer uma melhoria no script original, suba as alterações para o 
GitHub no repositório git_dgp e execute o comando abaixo no terminal para 
atualizar no seu computador:

pip install --upgrade git+https://github.com/davigopi/git_dgp.git

<br>
<br>

GUIA GIT – ORDEM NATURAL DE EXECUÇÃO (REVISADO)
=========================================================

OBS:
Este arquivo segue a ordem correta de execução.
Comandos substituídos estão comentados apenas para referência.

instalar git: https://git-scm.com/install/windows?utm_source=copilot.com

---------------------------------------------------------
## 1) CRIAR REPOSITÓRIO NO GITHUB
--------------------------------------------------------

➔  Vá até github.com
➔  Clique em "New Repository"
➔  Crie com nome_do_projeto
➔  NÃO marque README se for subir projeto já existente


---------------------------------------------------------
## 2) CRIAR .gitignore (ANTES DO PRIMEIRO COMMIT)
---------------------------------------------------------

➔  Criar arquivo .gitignore na raiz

➔  Exemplo de conteúdo:
➔  venv/
➔  __pycache__/
➔  *.pyc
➔  senha.txt

---------------------------------------------------------
## 3) INICIAR REPOSITÓRIO LOCAL
---------------------------------------------------------

git init
➔  Inicializa repositório Git na pasta atual

git status
➔  Verifica status do repositório

---------------------------------------------------------
## 4) CONFIGURAÇÃO INICIAL DO GIT (Executar uma vez no PC)
---------------------------------------------------------

git --help
➔  Mostra ajuda geral do Git

git config --global user.email "davigopi@gmail.com"
➔  Define o email global

git config --global user.name "davigopi"
➔  Define o nome global

git config --global init.defaultBranch main
➔  Define 'main' como branch padrão ao usar git init


---------------------------------------------------------
## 5) ADICIONAR ARQUIVOS
---------------------------------------------------------

git add .
➔  Adiciona todos os arquivos

git add "nome do arquivo completo.txt"
➔  Adiciona arquivo específico

git rm --cached -r nome_pasta
➔  Remove pasta do controle de versão caso já tenha sido adicionada


---------------------------------------------------------
## 6) FAZER COMMIT INICIAL
---------------------------------------------------------

git commit -m "Initial commit"
➔  Cria o primeiro commit


---------------------------------------------------------
## 7) CONFIGURAR REPOSITÓRIO REMOTO (ORIGIN)
---------------------------------------------------------

git remote -v
➔  Verifica se já existe remoto configurado

git remote add origin https://github.com/davigopi/nome_do_projeto.git
➔  Se não existe remoto. Adiciona repositório remoto.

git remote set-url origin https://github.com/davigopi/nome_do_projeto.git
➔  Se já existe remoto. Altera repositório remoto.

git remote remove origin
➔  Remove remoto existente

git remote rename origin old-origin
➔  Renomeia remoto


---------------------------------------------------------
## 8) GARANTIR BRANCH PRINCIPAL
---------------------------------------------------------

git branch
➔  Verifica branches locais

git branch -M main
➔  Renomeia branch atual para main (garantia)

➔  git checkout -b main
➔  NÃO necessário se init.defaultBranch já estiver como main


---------------------------------------------------------
## 9) ENVIAR PARA O GITHUB
---------------------------------------------------------

git push -u origin main
➔  Envia branch pela primeira vez e define upstream

➔  git push --set-upstream origin main
➔  Substituído por: git push -u origin main (faz a mesma função)

git push
➔  Envia commits futuros


---------------------------------------------------------
## 10) CLONAR REPOSITÓRIO EXISTENTE (ALTERNATIVA)
---------------------------------------------------------

git clone https://github.com/davigopi/agenda_django.git
➔  Clona repositório remoto existente

git clone
➔  se utilizar não precisa rodar git init nem git remote add origin, porque o clone já traz tudo configurado.


---------------------------------------------------------
## 11) COMANDOS DE VERIFICAÇÃO
---------------------------------------------------------

git status
➔  Mostra estado atual

git branch
➔  Lista branches

git remote -v
➔  Lista remotos

git log
➔  Histórico completo

git log --oneline
➔  Histórico resumido

git reflog
➔  Histórico detalhado (inclusive commits apagados)


---------------------------------------------------------
## 12) TRABALHANDO COM BRANCHES
---------------------------------------------------------

git branch nome_da_branch
➔  Cria nova branch

git checkout nome_da_branch
➔  Muda para branch existente

git checkout -b nova_branch
➔  Cria e já muda para nova branch

git merge nome_da_branch
➔  Mescla branch especificada na branch atual


---------------------------------------------------------
## 13) RESETAR COMMITS
---------------------------------------------------------

git reset --hard HASH
➔  Volta para commit específico e descarta alterações

git reset --hard HEAD
➔  Volta para último commit

git reset --soft HEAD~2
➔  Remove últimos 2 commits mantendo alterações nos arquivos


---------------------------------------------------------
## 14) REVERTER COMMITS (MANTENDO HISTÓRICO)
---------------------------------------------------------

git revert HEAD
➔  Reverte último commit

git revert HASH
➔  Reverte commit específico

git revert --abort
➔  Cancela processo de revert


---------------------------------------------------------
## 15) PROBLEMAS COM PUSH
---------------------------------------------------------

git status
➔  Verifica arquivos pendentes

git branch -M main
➔  Garante que está na branch main

git remote -v
➔  Confirma se o remoto está correto

git push -u origin main
➔  Faz push inicial se necessário


---------------------------------------------------------
## 16) SITUAÇÕES ESPECIAIS (CUIDADO)
---------------------------------------------------------

git push -u origin main --force
➔  Força envio ignorando histórico remoto (CUIDADO)

git pull origin main --allow-unrelated-histories
➔  Junta históricos diferentes quando há conflito inicial


---------------------------------------------------------
## FIM DO DOCUMENTO
---------------------------------------------------------
