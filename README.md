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

---

### Usando `===`

```md
Título Principal
================
```

Equivale a:

```md
# Título Principal
```

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

---

## 2. Negrito

```md
**Texto em negrito**
```

ou

```md
__Texto em negrito__
```

---

## 3. Itálico

```md
*Texto em itálico*
```

ou

```md
_Texto em itálico_
```

---

## 4. Negrito + Itálico

```md
***Texto em negrito e itálico***
```

---

## 5. Texto Riscado

```md
~~Texto removido~~
```

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
* Item
+ Item
```

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



















# 📖 Guia de Markdown para README.md

> Este arquivo serve como referência rápida de Markdown no GitHub.

## 1. Títulos

### Código

````md
# Título 1
## Título 2
### Título 3
````

### Resultado

# Título 1
## Título 2
### Título 3

---

## 2. Negrito

### Código

```md
**Texto em negrito**
```

### Resultado

**Texto em negrito**

---

## 3. Itálico

### Código

```md
*Texto em itálico*
```

### Resultado

*Texto em itálico*

---

## 4. Negrito + Itálico

### Código

```md
***Texto***
```

### Resultado

***Texto***

---

## 5. Riscado

### Código

```md
~~Texto~~
```

### Resultado

~~Texto~~

---

## 6. Linha horizontal

### Código

```md
---
```

### Resultado

---

## 7. Lista

### Código

```md
- Item A
- Item B
```

### Resultado

- Item A
- Item B

---

## 8. Lista numerada

### Código

```md
1. Um
2. Dois
```

### Resultado

1. Um
2. Dois

---

## 9. Checklist

### Código

```md
- [x] Feito
- [ ] Pendente
```

### Resultado

- [x] Feito
- [ ] Pendente

---

## 10. Código inline

### Código

```md
Use `git status`.
```

### Resultado

Use `git status`.

---

## 11. Bloco de código

````md
```python
print("Olá")
```
````

### Resultado

```python
print("Olá")
```

---

## 12. Link

### Código

```md
[GitHub](https://github.com)
```

### Resultado

[GitHub](https://github.com)

---

## 13. Imagem

### Código

```md
![Logo](logo.png)
```

### Resultado

_Renderizada quando existir a imagem._

---

## 14. Tabela

### Código

```md
| Nome | Idade |
|------|------:|
| João | 20 |
```

### Resultado

| Nome | Idade |
|------|------:|
| João | 20 |

---

## 15. Citação

### Código

```md
> Aviso
```

### Resultado

> Aviso

---

## 16. HTML

### Código

```html
<details>
<summary>Clique aqui</summary>

Texto escondido.

</details>
```

### Resultado

<details>
<summary>Clique aqui</summary>

Texto escondido.

</details>

---

## 17. Emojis

### Código

```md
🚀 Projeto
```

### Resultado

🚀 Projeto

---

## 18. Estrutura recomendada

```text
README.md
├── Descrição
├── Instalação
├── Uso
├── Tecnologias
├── Exemplos
├── Licença
└── Contribuição
```
