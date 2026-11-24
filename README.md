TUTORIAL: CRIAR E CENTRALIZAR A BIBLIOTECA E COMANDO CLI GIT_DGP
===============================================================================
## 📋 Sumário
1. [ESTRUTURA DA PASTA DO PROJETO LOCAL](#1-ESTRUTURA-DA-PASTA-DO-PROJETO-LOCAL)
2. [PUBLICAR NO GITHUB](#2-PUBLICAR-NO-GITHUB)
3. [INSTALAR E ATUALIZAÇÕES](#3-INSTALAR-E-ATUALIZAÇÕES)
4. [COMO USAR NOS SEUS PROJETOS](#4-COMO-USAR-NOS-SEUS-PROJETOS)
5. [EXEMPLOS DE CÓDIGO DE COMO UTILIZAR](#5-EXEMPLOS-DE-CÓDIGO-DE-COMO-UTILIZAR)
6. [UTILITÁRIOS](#UTILITÁRIOS)
7. [GUIA GIT](#GUIA-GIT)
---------------------------------------------------------
## 1. ESTRUTURA DA PASTA DO PROJETO LOCAL
---------------------------------------------------------
Crie uma pasta com o nome git_dgp e coloque os dois arquivos dentro dela:
```
git_dgp/
    ├── git_dgp.py
    ├── pyproject.toml
    ├── README.md
    ├── LICENSE
    ├── .gitignore
    ├── .editorconfig
    ├── requirements-dev.txt
    └── CHANGELOG.md
```
---------------------------------------------------------
## 2. PUBLICAR NO GITHUB
---------------------------------------------------------
Repositório público ou privado no GitHub com o nome git_dgp.

URL do repositório: https://github.com/davigopi/git_dgp

---------------------------------------------------------
## 3. INSTALAR E ATUALIZAÇÕES
---------------------------------------------------------

Abra o terminal do seu computador, ative o ambiente virtual e, no diretório do repositório git_dgp, execute

### A) INSTALAR A FERRAMENTA NO COMPUTADOR
```bash
pip install git+https://github.com/davigopi/git_dgp.git
```

### B) ATUALIZAR A FERRAMENTA NO FUTURO

Alterado a version em pyproject.toml:
```bash
pip install --upgrade git+https://github.com/davigopi/git_dgp.git
```
Força a atualização:
```bash
pip install --force-reinstall git+https://github.com/davigopi/git_dgp.git
```
```bash
pip install --upgrade --no-cache-dir git+https://github.com/davigopi/git_dgp.git
```

### C) INSTALAR REQUIREMENTS

```bash
pip install -r venv\Lib\site-packages\git_dgp\requirements.txt
```
---------------------------------------------------------

## 4. COMO USAR NOS SEUS PROJETOS
---------------------------------------------------------
- Via importação dentro de scripts Python futuros:
```python
from git_dgp import Git_Dgp
```
```python
import git_dgp
```
- Via terminal (em qualquer pasta de projeto React Native, Python, etc.):
  Basta abrir o terminal na pasta desejada e digitar:
```bash
python -m git_dgp
```
---------------------------------------------------------
## 5. EXEMPLOS DE CÓDIGO DE COMO UTILIZAR
---------------------------------------------------------

### A) Exemplo Básico (Inicialização e Verificação Simples)
``` python
# Verificacao simples de instalacao do Git e execucao de comando isolado
from git_auto_helper import check_git_installed, run_command, create_gitignore_if_missing

# Valida se o Git esta instalado e acessivel no PATH
check_git_installed()

# Garante que o arquivo .gitignore existe para o projeto (Python / Node)
create_gitignore_if_missing()

# Executa um comando simples do Git retornando a saida capturada
versao = run_command("git --version", show_output=False, capture=True)
print("Versao do Git em uso:", versao)
```

### B) Exemplo Avançado (Tratamento de Modais, Loading e Exceções)
``` python
# Uso avancado dos modulos internos do Git Auto Helper
import os
from git_auto_helper import (
check_git_installed,
check_gh_installed,
check_gh_authenticated,
configure_git_global,
create_gitignore_if_missing,
create_github_repo_online,
run_command
)

try:
# Checkpoint 1: Checagem de requisitos do ambiente
check_git_installed()

gh_disponivel = check_gh_installed()
gh_autenticado = check_gh_authenticated() if gh_disponivel else False

print(f"Status do GitHub CLI -> Instalado: {gh_disponivel} | Autenticado: {gh_autenticado}")

# Checkpoint 2: Configuracao das credenciais do usuario
usuario_github = "seu-usuario"
if not configure_git_global(usuario_github):
raise RuntimeError("Falha na configuracao global das credenciais do Git.")

# Checkpoint 3: Preparacao do repositorio local e .gitignore
create_gitignore_if_missing()

if not os.path.exists(".git"):
run_command("git init")
run_command("git branch -M main")

# Checkpoint 4: Criacao automatica remota via CLI ou orientacao manual
nome_repo = "meu-novo-projeto"
criado_via_cli = False

if gh_autenticado:
criado_via_cli = create_github_repo_online(nome_repo, usuario_github, is_private=True)

# Checkpoint 5: Adicao, Commit e Push com tratamento de falhas
run_command("git add .")
commit_status = run_command('git commit -m "feat: configuracao inicial do projeto"')

repo_url = f"https://github.com/{usuario_github}/{nome_repo}.git"
run_command(f"git remote add origin {repo_url}")

success = run_command("git push -u origin main")

if not success:
# Tratamento de divergencia de historico remoto
print("Divergencia detectada. Tentando sincronizacao com pull --allow-unrelated-histories...")
run_command("git pull origin main --allow-unrelated-histories --no-rebase")
run_command("git push -u origin main")

except Exception as erro:
print(f"Ocorreu um erro durante a execucao do assistente: {erro}")
```

### C) Exemplo de Execução CLI / Teste Integrado
``` bash
# Execucao direta do script pelo terminal interativo
python git_auto_helper.py

# Ou verificando via interpretador Python de linha de comando
python -c "import git_auto_helper; git_auto_helper.check_git_installed(); print('Git OK')"
```
---------------------------------------------------------
# UTILITÁRIOS
---------------------------------------------------------

---------------------------------------------------------
## 1. INSTALAR A FERRAMENTA NO COMPUTADOR
---------------------------------------------------------
Abra qualquer terminal no seu computador e execute:
```
pip install git+https://github.com/davigopi/git_dgp.git
```
---------------------------------------------------------
## 2. ATUALIZAR A FERRAMENTA NO FUTURO
---------------------------------------------------------
Sempre que fizer uma melhoria no script original, suba as alterações para o
GitHub no repositório github e execute o comando abaixo no terminal para
atualizar no seu computador:
```
pip install --force-reinstall git+https://github.com/davigopi/git_dgp.git

```
```

pip install --upgrade --no-cache-dir git+https://github.com/davigopi/git_dgp.git

```
---------------------------------------------------------
## 3. EXECUTAR COMANDO NO PROJETO
---------------------------------------------------------
```
python -m git_dgp
```

---------------------------------------------------------
---------------------------------------------------------

GUIA GIT
=========================================================

OBS:
Este arquivo segue a ordem correta de execução.
Comandos substituídos estão comentados apenas para referência.
```
instalar git: https://git-scm.com/install/windows?utm_source=copilot.com
```

---------------------------------------------------------
## 1) CRIAR REPOSITÓRIO NO GITHUB
--------------------------------------------------------

➔  Vá até github.com
➔  Clique em "New Repository"
➔  Crie com github
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
➔  Inicializa repositório Git na pasta atual
```
git init
```
➔  Verifica status do repositóri
```
git status
```
o

---------------------------------------------------------
## 4) CONFIGURAÇÃO INICIAL DO GIT (Executar uma vez no PC)
---------------------------------------------------------
➔  Mostra ajuda geral do Git
```
git --help
```
➔  Define o email global
```
git config --global user.email "user@gmail.com"
```
➔  Define o nome global
```
git config --global user.name "user_github"
```
➔  Define 'main' como branch padrão ao usar git init
```
git config --global init.defaultBranch main
```

---------------------------------------------------------
## 5) ADICIONAR ARQUIVOS
---------------------------------------------------------
➔  Adiciona todos os arquivos
```
git add .
```
➔  Adiciona arquivo específico
```
git add "nome do arquivo completo.txt"
```
➔  Remove pasta do controle de versão caso já tenha sido adicionada
```
git rm --cached -r nome_pasta
```

---------------------------------------------------------
## 6) FAZER COMMIT INICIAL
---------------------------------------------------------
➔  Cria o primeiro commit
```
git commit -m "Initial commit"
```

---------------------------------------------------------
## 7) CONFIGURAR REPOSITÓRIO REMOTO (ORIGIN)
---------------------------------------------------------
➔  Verifica se já existe remoto configurado
```
git remote -v
```
➔  Se não existe remoto. Adiciona repositório remoto.
```
git remote add origin https://github.com/user_github/nome_do_projeto.git
```
➔  Se já existe remoto. Altera repositório remoto.
```
git remote set-url origin https://github.com/user_github/nome_do_projeto.git
```
➔  Remove remoto existente
```
git remote remove origin
```
➔  Renomeia remoto
```
git remote rename origin old-origin
```
➔  Remover repositório remoto.
```
git filter-repo --path administrador/ --invert-paths
```

---------------------------------------------------------
## 8) GARANTIR BRANCH PRINCIPAL
---------------------------------------------------------

➔  Verifica branches locais
```
git branch
```
➔  Renomeia branch atual para main (garantia)
```
git branch -M main
```
➔  NÃO necessário se init.defaultBranch já estiver como main
```
git checkout -b main
```



---------------------------------------------------------
## 9) ENVIAR PARA O GITHUB
---------------------------------------------------------
➔  Envia branch pela primeira vez e define upstream
```
git push -u origin main
```
➔  Substituído por: git push -u origin main (faz a mesma função)
```
git push --set-upstream origin main
```
➔  Envia commits futuros
```
git push

```

---------------------------------------------------------
## 10) CLONAR REPOSITÓRIO EXISTENTE (ALTERNATIVA)
---------------------------------------------------------
➔  Clona repositório remoto existente
```
git clone https://github.com/user_github/nome_do_projeto.git
```
➔  se utilizar não precisa rodar git init nem git remote add origin, porque o clone já traz tudo configurado.
```
git clone
```


---------------------------------------------------------
## 11) COMANDOS DE VERIFICAÇÃO
---------------------------------------------------------
➔  Mostra estado atual
```
git status
```
➔  Lista branches
```
git branch
```
➔  Lista remotos
```
git remote -v
```
➔  Histórico completo
```
git log
```
➔  Histórico resumido
```
git log --oneline
```
➔  Histórico detalhado (inclusive commits apagados)
```
git reflog
```


---------------------------------------------------------
## 12) TRABALHANDO COM BRANCHES
---------------------------------------------------------
➔  Cria nova branch
```
git branch nome_da_branch
```
➔  Muda para branch existente
```
git checkout nome_da_branch
```
➔  Cria e já muda para nova branch
```
git checkout -b nova_branch
```
➔  Mescla branch especificada na branch atual
```
git merge nome_da_branch
```

---------------------------------------------------------
## 13) RESETAR COMMITS
---------------------------------------------------------
➔  Volta para commit específico e descarta alterações
```
git reset --hard HASH
```
➔  Volta para último commit
```
git reset --hard HEAD
```
➔  Remove últimos 2 commits mantendo alterações nos arquivos
```
git reset --soft HEAD~2
```


---------------------------------------------------------
## 14) REVERTER COMMITS (MANTENDO HISTÓRICO)
---------------------------------------------------------
➔  Reverte último commit
```
git revert HEAD
```
➔  Reverte commit específico
```
git revert HASH
```
➔  Cancela processo de revert
```
git revert --abort
```


---------------------------------------------------------
## 15) PROBLEMAS COM PUSH
---------------------------------------------------------
➔  Verifica arquivos pendentes
```
git status
```
➔  Garante que está na branch main
```
git branch -M main
```
➔  Confirma se o remoto está correto
```
git remote -v
```
➔  Faz push inicial se necessário
```
git push -u origin main
```


---------------------------------------------------------
## 16) SITUAÇÕES ESPECIAIS (CUIDADO)
---------------------------------------------------------
➔  Força envio ignorando histórico remoto (CUIDADO)
```
git push -u origin main --force
```
➔  Junta históricos diferentes quando há conflito inicial
```
git pull origin main --allow-unrelated-histories
```


---------------------------------------------------------
---------------------------------------------------------
