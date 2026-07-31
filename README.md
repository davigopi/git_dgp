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



