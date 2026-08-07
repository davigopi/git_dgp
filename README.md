TUTORIAL: UTILIZAÇÃO git_dgp (nome_do_projeto)
===============================================================================

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
GitHub no repositório nome_do_projeto e execute o comando abaixo no terminal para 
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

GUIA GIT – ORDEM NATURAL DE EXECUÇÃO (REVISADO)
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
