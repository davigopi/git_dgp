<<<<<<< HEAD
# 📖 Guia Completo de README.md (Markdown)

## 1. Títulos

### Usando `#`

```md
# Título 1
## Título 2
### Título 3
#### Título 4
##### Título 5
###### Título 6
```

Quanto mais `#`, menor o título.

# Título 1
## Título 2
### Título 3

---

### Usando `===`

```md
Título Principal
================
```
Título Principal
================

Equivale a:

```md
# Título Principal
```
# Título Principal

---

### Usando `---`

```md
Subtítulo
----------
```

Equivale a:

```md
## Subtítulo
```
Subtítulo
----------
---

## 2. Negrito

```md
**Texto em negrito**
```

ou

```md
__Texto em negrito__
```
**Texto em negrito**
---

## 3. Itálico

```md
*Texto em itálico*
```

ou

```md
_Texto em itálico_
```
*Texto em itálico*
---

## 4. Negrito + Itálico

```md
***Texto em negrito e itálico***
```
***Texto em negrito e itálico***


---

## 5. Texto Riscado

```md
~~Texto removido~~
```
~~Texto removido~~

---

# 6. Linha Separadora

```md
---
```

ou

```md
***
```

ou

```md
___
```

---

# 7. Listas

## Lista com marcadores

```md
- Item 1
- Item 2
- Item 3
```

Também funciona:

```md
* Item 4
+ Item 5
```
- Item 1
- Item 2
- Item 3
* Item 4
+ Item 5
---

## Lista numerada

```md
1. Primeiro
2. Segundo
3. Terceiro
```

---

## Sublista

```md
- Python
  - Selenium
  - Flask
  - Django
```

---

# 8. Checkbox (Lista de tarefas)

```md
- [x] Concluído
- [ ] Pendente
```

---

# 9. Código

## Código em uma linha

```md
Use o comando `git pull`.
```

---

## Bloco de código

````md
```python
print("Olá Mundo")
```
````

Outras linguagens:

````md
```bash
git pull
```

```javascript
console.log("Olá");
```

```json
{
    "nome": "Davi"
}
```

```xml
<nome>Davi</nome>
```

```sql
SELECT * FROM usuarios;
```
````

---

# 10. Links

```md
https://github.com
```

ou

```md
[GitHub](https://github.com)
```

---

# 11. Imagens

Imagem local:

```md
![Logo](logo.png)
```

Imagem da internet:

```md
![Logo](https://site.com/logo.png)
```

---

# 12. Tabelas

```md
| Nome | Idade | Cidade |
|------|------:|:------:|
| João | 20 | Fortaleza |
| Maria | 25 | São Paulo |
```

Alinhamento:

```text
:----   Alinha à esquerda
----:   Alinha à direita
:---:   Centraliza
```

---

# 13. Citações

```md
> Este é um aviso.
```

Aninhado:

```md
> Primeiro nível
>> Segundo nível
>>> Terceiro nível
```

---

# 14. Comentários (não aparecem no README)

```html
<!-- Este comentário não aparece -->
```

---

# 15. HTML

Negrito

```html
<b>Texto</b>
```

Itálico

```html
<i>Texto</i>
```

Quebra de linha

```html
<br>
```

Parágrafo

```html
<p>Texto</p>
```

Centralizar

```html
<p align="center">Texto</p>
```

Imagem centralizada

```html
<p align="center">
    <img src="logo.png">
</p>
```

---

# 16. Conteúdo Recolhível

```html
<details>
<summary>Clique aqui</summary>

Texto escondido.

</details>
```

---

# 17. Emojis

Pode usar diretamente:

```md
🚀 Projeto
```

Ou códigos do GitHub:

```text
:rocket:
:fire:
:star:
:warning:
:bug:
:white_check_mark:
:computer:
:gear:
:wrench:
:package:
:books:
:pushpin:
:zap:
```

---

# 18. Escapar Caracteres

```md
\#
\*
\`
\_
```

---

# 19. Quebra de Linha

Markdown ignora um Enter simples.

Para quebrar linha:

```md
Linha 1<br>
Linha 2
```

ou coloque dois espaços no final da linha.

---

# 20. Destacar Comandos

```md
Pressione `Ctrl + C`
```

---

# 21. Índice

```md
## Índice

- [Instalação](#instalação)
- [Como usar](#como-usar)
- [Tecnologias](#tecnologias)
- [Licença](#licença)
```

---

# 22. Badges (Selos)

```md
![Python](https://img.shields.io/badge/Python-3.13-blue)

![Git](https://img.shields.io/badge/Git-2.50-red)

![License](https://img.shields.io/badge/license-MIT-green)
```

---

# 23. Estrutura Recomendada

```md
# 🚀 Nome do Projeto

Descrição do projeto.

## 📷 Imagens

## ✨ Funcionalidades

## 🛠 Tecnologias

## 📦 Instalação

## 🚀 Como usar

## 📁 Estrutura do Projeto

## 💻 Exemplos

## ⚙️ Configuração

## 📌 Observações

## 🤝 Contribuição

## 📄 Licença
```

---

# 24. Dicas Úteis

| Sintaxe              | Resultado                    |
| -------------------- | ---------------------------- |
| `#`                  | Título grande                |
| `##`                 | Título médio                 |
| `###`                | Título pequeno               |
| `====`               | Equivale a `#`               |
| `----`               | Equivale a `##`              |
| `**texto**`          | Negrito                      |
| `*texto*`            | Itálico                      |
| `***texto***`        | Negrito + Itálico            |
| `~~texto~~`          | Riscado                      |
| `---`                | Linha horizontal             |
| `-`                  | Lista                        |
| `1.`                 | Lista numerada               |
| `- [ ]`              | Checkbox vazio               |
| `- [x]`              | Checkbox marcado             |
| `` `codigo` ``       | Código em linha              |
| ` ``` `              | Bloco de código              |
| `>`                  | Citação                      |
| `[Texto](Link)`      | Link                         |
| `![Alt](Imagem)`     | Imagem                       |
| `<br>`               | Quebra de linha              |
| `<details>`          | Conteúdo recolhível          |
| `<img>`              | Inserir imagem               |
| `<p align="center">` | Centralizar conteúdo         |
| `<!-- -->`           | Comentário oculto            |
| `\`                  | Escapar caracteres especiais |



=======
TUTORIAL: CRIAR E CENTRALIZAR A BIBLIOTECA E COMANDO CLI (git_dgp)
===============================================================================

## 1. ESTRUTURA DA PASTA DO PROJETO LOCAL
-------------------------------------------------------------------------------
Crie uma pasta com o nome git_dgp e coloque os dois arquivos dentro dela:

git_dgp/

├── git.py          <-- O seu código da ferramenta Git

└── pyproject.toml  <-- Arquivo de configuração da biblioteca Python




## 2. CONTEÚDO DO ARQUIVO pyproject.toml
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

## 3. PUBLICAR NO GITHUB
-------------------------------------------------------------------------------
Crie o repositório público ou privado no GitHub com o nome git_dgp e suba 
a pasta criada:

URL do repositório: https://github.com/davigopi/git_dgp

## 4. INSTALAR A FERRAMENTA NO COMPUTADOR
-------------------------------------------------------------------------------
Abra qualquer terminal no seu computador e execute:

pip install git+https://github.com/davigopi/git_dgp.git

## 5. COMO USAR NOS SEUS PROJETOS
-------------------------------------------------------------------------------
- Via terminal (em qualquer pasta de projeto React Native, Python, etc.):
  Basta abrir o terminal na pasta desejada e digitar:

  git_dgp

- Via importação dentro de scripts Python futuros:
  from git import run_command, create_gitignore_if_missing

## 6. ATUALIZAR A FERRAMENTA NO FUTURO
-------------------------------------------------------------------------------
Sempre que fizer uma melhoria no script original, suba as alterações para o 
GitHub no repositório git_dgp e execute o comando abaixo no terminal para 
atualizar no seu computador:

pip install --upgrade git+https://github.com/davigopi/git_dgp.git


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
>>>>>>> 90e92d855ab659a56e402ba4c86c79ba1f82b6b2
