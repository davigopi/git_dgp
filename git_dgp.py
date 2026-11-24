# -*- coding: utf-8 -*-
"""
===============================================================================
  GIT AUTO HELPER - Assistente Interativo de Git e GitHub (Python & React Native)
===============================================================================
  Desenvolvido para automatizar e simplificar o uso do Git e GitHub.
  Inclui suporte para criação de repositórios via GitHub CLI (gh),
  commits automáticos com data/hora completa, clonagem, push/pull e utilitários.
===============================================================================
"""

import subprocess
import os
import sys
import time
from datetime import datetime
from pathlib import Path
import shutil



def print_header(title):
    os.system('cls')
    print("=" * 60)
    print(f"  {title.upper()}")
    print("_" * 60)
    print(' ' * 52 + "Sair [x]")


def run_command(command, show_output=True, capture=False, verbose=True, time_seep=0):
    """
    Executa um comando no terminal com suporte a feedback visual.
    """
    if verbose and show_output:
        text = f"⛏️  {command}"
        text = text.ljust(70)
        for i in range(1, 0, -1):
            text_print = text +  '| ⏳ ' + str(i) + ' seg.'
            print(f'\r{text_print}', end='')
            time.sleep(1)
        print(f'\r{text}', end='| ')

    try:
        if capture:
            result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            return result.stdout.strip()
        else:
            result = subprocess.run(command, shell=True, check=True)
            time.sleep(time_seep)
            return True
    except subprocess.CalledProcessError as e:
        if show_output and e.stderr:
            print(f"\n[ERRO] Falha ao executar: {command}")
            print(f"Detalhes do erro:\n{e.stderr.strip()}")
        time.sleep(5)
        return False

def check_git_installed():
    """Verifica se o Git está instalado no sistema."""
    if not run_command("git --version", show_output=False, capture=True, verbose=False):
        print("\n[X] ERRO CRÍTICO: O Git não está instalado ou não está no PATH do sistema.")
        print("    Por favor, instale o Git antes de continuar:")
        print("    https://git-scm.com/install/windows")
        sys.exit(1)

def check_gh_installed():
    """Verifica se o GitHub CLI (gh) está instalado."""
    res = run_command("gh --version", show_output=False, capture=True, verbose=False)
    return bool(res)

def check_gh_authenticated():
    """Verifica se o usuário está autenticado no GitHub CLI."""
    res = run_command("gh auth status", show_output=False, capture=True, verbose=False)
    return bool(res)





def create_gitignore_if_missing():
    """Cria ou atualiza o .gitignore para suportar tanto Python quanto React Native/Node."""
    need_write = False

    if not os.path.exists(".gitignore") or os.path.getsize(".gitignore") == 0:
        need_write = True
    else:
        with open(".gitignore", "r", encoding="utf-8") as f:
            content = f.read()
            # Se não tiver a regra do Python OU a do React Native, atualiza
            if "venv" not in content or "node_modules" not in content:
                need_write = True

    if need_write:
        print("\n📄 Atualizando/Criando arquivo .gitignore (Suporte a Python & React Native)...")
        gitignore_content = """# ==========================================
# REGRAS DE PYTHON
# ==========================================
venv/
env/
.env
__pycache__/
*.pyc
*.pyo
senha.txt

# ==========================================
# REGRAS DE REACT NATIVE / NODE / JAVASCRIPT
# ==========================================
node_modules/
.expo/
dist/
web-build/
.bundle/
vendor/bundle/
*.metro-health-check*

# Builds e Nativos (se gerados localmente)
android/app/build/
android/.gradle/
ios/Pods/
ios/build/

# ==========================================
# SISTEMA E IDEs
# ==========================================
.DS_Store
Thumbs.db
.vscode/
.idea/
"""
        with open(".gitignore", "w", encoding="utf-8") as f:
            f.write(gitignore_content)
        print("✅ .gitignore configurado com sucesso para Python e React Native!")

def remove_cached_files():
    """Remove pastas/arquivos pesados (como node_modules ou venv) do GitHub sem apagar do computador."""
    confirm_working_directory()
    print_header("Remover pasta/arquivo do GitHub (Manter no PC)")

    print("O que você deseja remover do rastreamento do Git ?")
    print("[1] node_modules (React Native / Node)")
    print("[2] venv (Python)")
    print("[3] Outro arquivo/pasta personalizado")
    print("\nEscolha uma opção (0-3) [padrão 1]: ")
    opcao = input("➔  ").strip()

    if opcao == '2':
        target = "venv"
    elif opcao == '3':
        print("Digite o nome exato da pasta ou arquivo: ")
        target = input("➔  ").strip()
    elif opcao == 'x':
        return False
    else:
        target = "node_modules"

    if not target:
        target = "node_modules"

    print(f"\n➔ Removendo '{target}' do rastreamento do Git...")
    if run_command(f"git rm -r --cached {target}"):
        create_gitignore_if_missing()

        commit_msg = f"fix: remove {target} do rastreamento do remoto"
        print(f"➔ Criando commit de remoção: '{commit_msg}'")
        run_command(f'git commit -m "{commit_msg}"')

        print("➔ Enviando atualização para o GitHub...")
        if run_command("git push"):
            print(f"\n✅  SUCESSO: '{target}' foi removido do site do GitHub e continuará salvo no seu computador!")
        else:
            print(f"\n⚠️  O push falhou. Execute 'git push' manualmente após verificar seu repositório.")
    else:
        print(f"\n⚠️  Não foi possível remover '{target}'. Verifique se o nome está correto ou se já não foi removido.")

def create_github_repo_online(name_repositoring, github_user, is_private=False):
    """Cria o repositório diretamente no GitHub usando o GitHub CLI se disponível."""
    if check_gh_installed():
        if check_gh_authenticated():
            visibility = "--private" if is_private else "--public"
            print(f"\n✅  Tentando criar repositório '{name_repositoring}' diretamente no GitHub via GitHub CLI (gh)...")
            cmd = f"gh repo create {name_repositoring} {visibility} --source=. --remote=origin"
            if run_command(cmd):
                print(f"✅  Repositório '{name_repositoring}' criado no GitHub com sucesso!")
                return True
        else:
            print("\n⛔ GitHub CLI detectado, mas você não está logado.")
            print("   Dica: Rode 'gh auth login' no terminal para criar repositórios automaticamente no futuro.")

    print("\n" + "="*60)
    print("📌 INSTRUÇÕES PARA CRIAR O REPOSITÓRIO NO SITE DO GITHUB")
    print("="*60)
    print("Como criar o repositório manualmente no site:")
    print(f"1. Acesse: https://github.com/{github_user}")
    print(f"2. Em 'Repository name', crie NEW repositório com nome: {name_repositoring}")
    print("3. Escolha Public ou Private.")
    print("4. ATENÇÃO: NÃO marque 'Add a README file', NÃO adicione .gitignore e nem Licença.")
    print("   (Como já temos arquivos locais, o repositório deve ser criado VAZIO).")
    print("5. Clique no botão verde 'Create repository'.")
    print("="*60)
    print("\nPressione ENTER assim que tiver criado o repositório no site...")
    input("➔  ")
    return False

def show_git_utilities():
    """Submenu de ferramentas utilitárias do Git com suporte a --no-pager."""
    while True:
        print_header("Menu de Utilitários e Verificação Git")
        print("[1] Ver Status atual (git status)")
        print("[2] Ver Histórico resumido (git log --oneline)")
        print("[3] Ver Histórico completo (git log)")
        print("[4] Ver Histórico detalhado (git reflog)")
        print("[5] Ver Branches locais (git branch)")
        print("[6] Ver Remotos configurados (git remote -v)")
        print("[7] Criar/Alternar para nova Branch")
        print("[8] Desfazer/Resetar alterações (git reset)")
        print("[9] Apagar pasta do GitHub sem apagar do PC (ex: node_modules ou venv)")
        print("[10] Excluir commits remotos")
        print("[V] Voltar ao menu principal")

        print("\nEscolha uma opção (0-10): ")

        escolha = input("➔  ").strip()

        if escolha == '1':
            run_command("git status", time_seep=2)
        elif escolha == '2':
            run_command("git --no-pager log --oneline -n 10", time_seep=2)
        elif escolha == '3':
            run_command("git --no-pager log -n 5", time_seep=2)
        elif escolha == '4':
            run_command("git --no-pager reflog -n 10", time_seep=2)
        elif escolha == '5':
            run_command("git branch", time_seep=2)
        elif escolha == '6':
            run_command("git remote -v", time_seep=2)
        elif escolha == '7':
            branch_name = input("Digite o nome da branch: ").strip()
            if branch_name:
                run_command(f"git checkout -b {branch_name}")
        elif escolha == '8':
            print("\nOpções de Reset:")
            print("[a] Reset leve (reverte commits mantendo arquivos) ➔ git reset --soft HEAD~1")
            print("[b] Reset HARD (descarta TODAS as alterações não salvas) ➔ git reset --hard HEAD")
            print("\nEscolha (a/b) ou ENTER para cancelar: ")
            sub = input("➔  ").strip().lower()
            if sub == 'a':
                run_command("git reset --soft HEAD~1")
            elif sub == 'b':
                print("TEM CERTEZA? Isso apaga mudanças não salvas. (s/N): ")
                conf = input("➔  ").strip().lower()
                if conf == 's':
                    run_command("git reset --hard HEAD")
        elif escolha == '9':
            if not remove_cached_files():
                return False
        elif escolha == '10':
            print("\n⚠️  Isso vai apagar todo o histórico remoto e manter apenas os arquivos atuais.")
            confirm = input("Tem certeza? (s/N): ").strip().lower()
            if confirm == 's':
                # Reescreve o histórico local
                run_command("git checkout --orphan temp_branch")
                run_command("git add .")
                run_command('git commit -m "Histórico zerado"')
                run_command("git branch -M main")
                # Força o push para sobrescrever no GitHub
                run_command("git push origin main --force")
                print("✅ Histórico remoto zerado com sucesso!")
        elif escolha == 'v':
            return True
        elif escolha == 'x':
            return False
        else:
            print("Opção inválida.")

def get_name_user():
    while True:
        print_header("Assistente Automatizado de Git & GitHub")
        github_user = run_command("git config --global user.name", show_output=False, capture=True, verbose=False)
        print(f"{10*'#'} Usuário ➔  {(github_user if github_user else 'Não configurado'):<20} {10*'#'}")
        print("O nome do usuário do github esta correto ? (S/n)")
        opcao = input("➔  ").strip().lower()
        if opcao == 'n':
            print("Qual o nome do usuário do github ?")
            github_user = input("➔  ").strip().lower()
        elif opcao == 'x':
            return False
        if not github_user:
            input(f"\r➔  Usuário não pode ser nulo! (Enter para continuar) ", end='')
            continue
        return github_user

def configure_git_global(username):
    """Configura o usuário e branch padrão se necessário."""
    print_header("Configuração Global do Git")

    current_user = run_command("git config --global user.name", show_output=False, capture=True, verbose=False)
    current_email = run_command("git config --global user.email", show_output=False, capture=True, verbose=False)

    print(f"{10*'#'} Nome  ➔  {(current_user if current_user else 'Não configurado'):<20} {10*'#'}")
    print(f"{10*'#'} Email ➔  {(current_email if current_email else 'Não configurado'):<20} {10*'#'}")

    if not current_user or not current_email:
        print("\nConfigurando credenciais globais do Git...")
        print(f"Informe o seu e-mail do GitHub (ex: {username}@gmail.com): ")
        email = input("➔  ").strip()
        if email.strip().lower() == 'x':
            return None
        run_command(f'git config --global user.name "{username}"')
        run_command(f'git config --global user.email "{email}"')
        run_command('git config --global init.defaultBranch main')
        print("✅ Configuração global salva com sucesso!")
        return True
    else:
        print("Configurações globais (Nome ou Email) estão corretas ? (S/n)")
        opcao = input("➔  ").strip().lower()
        if opcao == 'n':
            print(f"\nQual o novo user.name para substituir {current_user} ?")
            novo_nome = input("➔  ").strip() or current_user
            print(f"\nQual o novo user.email para substituir {current_email} ?")
            novo_email = input("➔  ").strip() or current_email
            if novo_nome.strip().lower() == 'x' or novo_email.strip().lower() == 'x':
                return None
            run_command(f'git config --global user.name "{novo_nome}"')
            run_command(f'git config --global user.email "{novo_email}"')
            run_command('git config --global init.defaultBranch main')
            print("✅ Configuração global atualizada!")
            return True
        elif opcao == 'x':
            return None
        return True

def confirm_working_directory():
    """Exibe e confirma/altera o diretório de trabalho local do projeto com validação."""
    while True:
        print_header("Pasta do computador para vinculação")
        current_dir = os.getcwd()

        print(f"{10*'#'} Pasta ➔  {current_dir} {10*'#'}")
        print(f"É a pasta para vincular com o github ? [S/n]: ")
        opcao = input("➔  ").strip().lower()
        if opcao == 'x':
            return None

        elif opcao not in ['n', 'nao', 'não']:
            print(f"✅ Usando diretório: {current_dir}")
            break

        print("\n⌨️  Digite ou cole o caminho completo da pasta desejada: ")
        novo_caminho = input("➔  ").strip().strip('"')
        if novo_caminho == 'x':
            return None

        if os.path.exists(novo_caminho) and os.path.isdir(novo_caminho):
            os.chdir(novo_caminho)
            print(f"✅ Diretório alterado com sucesso para: {os.getcwd()}")
            break
        else:
            print("\n❌ ERRO: Caminho inválido ou pasta não encontrada!")
            print("Por favor, tente novamente digitando o caminho correto ou confirme a pasta atual.")
    return True

def get_name_repositoring(github_user):
    # Pega o nome da pasta atual onde o usuário está executando o comando
    name_repositoring = Path(os.getcwd()).name
    print_header("Nome do repositório")
    print(f"{10*'#'} Repositório ➔  {name_repositoring} {10*'#'}")
    print(f"Confirma o nome repositório em github.com/{github_user}/ ? (S/n):")
    name_response = input("➔  ").strip().lower()
    if name_response in ['n', 'nao', 'não']:
        while True:
            print(f"\nQual o nome do repositório no github.com/{github_user}/ ?")
            name_repositoring = input("➔  ").strip()
            if not name_repositoring:
                print("⚠️  Nome do repositório é obrigatório.")
                continue
            break
    if name_response == 'x':
        return None
    return name_repositoring


# def update_from_github():
#     confirm_working_directory()
#     print_header("Atualizar arquivos do GitHub")
#     # Verifica se existe um repositório Git local
#     if not Path(".git").exists():
#         print("\n❌ Esta pasta não possui um repositório Git.")
#         input("\nPressione ENTER para continuar...")
#         return False
#     # Verifica o repositório remoto
#     remote = run_command("git remote get-url origin", show_output=False, capture=True, verbose=False)
#     if not remote:
#         print("\n❌ Nenhum repositório remoto 'origin' configurado.")
#         input("\nPressione ENTER para continuar...")
#         return False
#     print(f"\nRepositório remoto: {remote}")
#     # Verifica alterações locais
#     status = run_command("git status --porcelain", show_output=False, capture=True, verbose=False)
#     if status is False:
#         print("\n❌ Não foi possível verificar o status do Git.")
#         input("\nPressione ENTER para continuar...")
#         return False
#     if status:
#         print("\n⚠️ Existem alterações locais não salvas em commit.")
#         print("Salve ou faça backup dessas alterações antes de atualizar.")
#         input("\nPressione ENTER para continuar...")
#         return False
#     # Atualiza informações do GitHub
#     print("\n🔎 Verificando atualizações disponíveis no GitHub...")
#     if not run_command("git fetch origin"):
#         print("\n❌ Falha ao consultar o GitHub.")
#         input("\nPressione ENTER para continuar...")
#         return False
#     # Identifica a branch atual
#     branch = run_command("git branch --show-current", show_output=False, capture=True, verbose=False)
#     if not branch:
#         print("\n❌ Não foi possível identificar a branch atual.")
#         input("\nPressione ENTER para continuar...")
#         return False
#     # Verifica se existem atualizações
#     behind = run_command(f"git rev-list --count HEAD..origin/{branch}", show_output=False, capture=True, verbose=False)

#     if behind is False:
#         print("\n❌ Não foi possível verificar a branch remota.")
#         input("\nPressione ENTER para continuar...")
#         return False

#     if behind == "0":
#         print("\n✅ Seus arquivos já estão atualizados!")
#         input("\nPressione ENTER para continuar...")
#         return True

#     print(f"\n📥 Existem {behind} atualização(ões) no GitHub.")
#     print("As alterações serão integradas aos arquivos locais.")

#     confirmar = input("\nDeseja continuar? (S/n): ").strip().lower()

#     if confirmar != "s":
#         print("\nAtualização cancelada.")
#         return False

#     # Baixa e integra as atualizações
#     if run_command(f"git pull --ff-only origin {branch}"):
#         print("\n✅ Arquivos atualizados com sucesso!")
#         print("Seu computador agora possui as alterações do GitHub.")
#         return True

#     print("\n⚠️ Não foi possível atualizar automaticamente.")
#     print("Pode existir divergência entre os históricos local e remoto.")
#     print("Nenhuma integração automática foi realizada.")

#     input("\nPressione ENTER para continuar...")
#     return False

def update_from_github():
    """Atualiza arquivos locais com o GitHub, oferecendo opções de segurança."""

    if not confirm_working_directory():
        return False

    print_header("Atualizar arquivos do GitHub")

    # 1. Verifica se existe um repositório Git
    if not Path(".git").exists():
        print("\n❌ Esta pasta não possui um repositório Git.")
        input("\nPressione ENTER para continuar...")
        return False

    # 2. Verifica o repositório remoto
    remote = run_command(
        "git remote get-url origin",
        show_output=False,
        capture=True,
        verbose=False
    )

    if not remote:
        print("\n❌ Nenhum repositório remoto 'origin' configurado.")
        input("\nPressione ENTER para continuar...")
        return False

    print(f"\n📡 Repositório remoto: {remote}")

    # 3. Identifica a branch atual
    branch = run_command(
        "git branch --show-current",
        show_output=False,
        capture=True,
        verbose=False
    )

    if not branch:
        print("\n❌ Não foi possível identificar a branch atual.")
        input("\nPressione ENTER para continuar...")
        return False

    print(f"🌿 Branch local: {branch}")

    # 4. Consulta o GitHub
    print("\n🔎 Verificando atualizações no GitHub...")

    if not run_command("git fetch origin"):
        print("\n❌ Falha ao consultar o GitHub.")
        input("\nPressione ENTER para continuar...")
        return False

    # 5. Verifica se a branch remota existe
    remote_branch = run_command(
        f"git rev-parse --verify origin/{branch}",
        show_output=False,
        capture=True,
        verbose=False
    )

    if not remote_branch:
        print(f"\n❌ A branch origin/{branch} não foi encontrada.")
        print("Verifique se o nome da branch local corresponde à remota.")
        input("\nPressione ENTER para continuar...")
        return False

    # 6. Verifica alterações locais
    status = run_command(
        "git status --porcelain",
        show_output=False,
        capture=True,
        verbose=False
    )

    if status is False:
        print("\n❌ Não foi possível verificar os arquivos locais.")
        input("\nPressione ENTER para continuar...")
        return False

    if status:
        print("\n⚠️ Foram encontradas alterações locais não salvas em commit.")
        print("O que você deseja fazer?")
    else:
        print("\n✅ Nenhuma alteração local pendente foi encontrada.")

    # 7. Menu de sincronização
    print("\n" + "=" * 60)
    print(" OPÇÕES DE SINCRONIZAÇÃO")
    print("=" * 60)

    print("[1] ATUALIZAR PRESERVANDO alterações locais")
    print("    Guarda temporariamente suas alterações, atualiza")
    print("    o projeto e tenta reaplicá-las.")

    print("\n[2] FAZER COMMIT antes de atualizar")
    print("    Registra as alterações locais em um commit")
    print("    e depois atualiza o projeto.")

    print("\n[3] SUBSTITUIR TUDO pelo conteúdo do GitHub")
    print("    Descarta alterações locais e arquivos não rastreados")
    print("    para deixar o projeto conforme a versão remota.")

    print("\n[4] CANCELAR")
    print("    Não realiza nenhuma alteração.")

    print("\n" + "=" * 60)

    opcao = input("\nEscolha uma opção (1-4): ").strip().lower()

    # =====================================================
    # OPÇÃO 1 - STASH
    # =====================================================
    if opcao == '1':

        stash_ref = None

        if status:
            print("\n📦 Guardando alterações locais temporariamente...")

            if not run_command(
                'git stash push --include-untracked -m "Backup antes de atualizar GitHub"'
            ):
                print("\n❌ Não foi possível guardar as alterações.")
                return False

            stash_ref = run_command(
                "git rev-parse -q --verify refs/stash",
                show_output=False,
                capture=True,
                verbose=False
            )

            if not stash_ref:
                print("\n❌ Não foi possível identificar o backup criado.")
                print("Verifique o Git antes de continuar.")
                return False

        print("\n📥 Baixando atualizações do GitHub...")

        if not run_command(f"git pull --ff-only origin {branch}"):
            print("\n❌ Não foi possível atualizar o projeto.")

            if stash_ref:
                print("\n♻️ Tentando restaurar suas alterações locais...")
                if not run_command(f"git stash apply {stash_ref}"):
                    print("\n⚠️ Não foi possível restaurar automaticamente.")
                    print("Seu backup continua guardado no Git Stash.")

            input("\nPressione ENTER para continuar...")
            return False

        # Restaura alterações locais
        if stash_ref:
            print("\n♻️ Restaurando suas alterações locais...")

            if run_command(f"git stash apply {stash_ref}"):
                print("\n✅ Alterações locais restauradas!")
                print("📦 O backup também foi mantido no Git Stash.")
            else:
                print("\n⚠️ Ocorreu um conflito ao restaurar alterações.")
                print("Seu backup continua guardado no Git Stash.")
                print("Será necessário resolver os conflitos manualmente.")
                input("\nPressione ENTER para continuar...")
                return False

        print("\n✅ Sincronização concluída com sucesso!")

    # =====================================================
    # OPÇÃO 2 - COMMIT
    # =====================================================
    elif opcao == '2':

        if status:
            print("\n📦 Preparando alterações locais para commit...")

            if not run_command("git add -A"):
                print("\n❌ Falha ao adicionar arquivos.")
                return False

            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            commit_msg = f"Backup local antes de atualizar - {data_hora}"

            if not run_command(f'git commit -m "{commit_msg}"'):
                print("\n❌ Não foi possível criar o commit.")
                return False

            print("\n✅ Alterações locais registradas em commit!")
        else:
            print("\n✅ Não existem alterações locais para registrar.")

        print("\n📥 Atualizando arquivos do GitHub...")

        if run_command(f"git pull --ff-only origin {branch}"):
            print("\n✅ Projeto atualizado com sucesso!")
        else:
            print("\n⚠️ Não foi possível integrar as atualizações.")
            print("Seu commit local foi preservado.")
            input("\nPressione ENTER para continuar...")
            return False

    # =====================================================
    # OPÇÃO 3 - SUBSTITUIR TUDO
    # =====================================================
    elif opcao == '3':

        print("\n" + "!" * 60)
        print("⚠️ ATENÇÃO: SUBSTITUIÇÃO TOTAL DOS ARQUIVOS")
        print("!" * 60)

        print("\nEsta operação irá:")
        print("1. Descartar alterações locais em arquivos rastreados.")
        print("2. Remover arquivos e pastas não rastreados pelo Git.")
        print("3. Atualizar os arquivos conforme o GitHub.")
        print("\nArquivos ignorados pelo .gitignore serão preservados.")
        print("Commits locais que não estão no GitHub não serão apagados,")
        print("mas a branch local será reposicionada para a versão remota.")

        print("\n❌ ESTA OPERAÇÃO PODE APAGAR SEU TRABALHO LOCAL!")

        confirmar = input(
            "\nDigite SUBSTITUIR para confirmar a operação: "
        ).strip()

        if confirmar != "SUBSTITUIR":
            print("\nOperação cancelada.")
            return False

        print("\n🔄 Substituindo arquivos pela versão do GitHub...")

        if not run_command(f"git reset --hard origin/{branch}"):
            print("\n❌ Falha ao substituir os arquivos.")
            input("\nPressione ENTER para continuar...")
            return False

        print("\n🧹 Removendo arquivos locais não rastreados...")

        if not run_command("git clean -fd"):
            print("\n⚠️ Não foi possível remover todos os arquivos.")
            input("\nPressione ENTER para continuar...")
            return False

        print("\n📥 Arquivos sincronizados com o GitHub!")
        print("✅ Seu projeto agora corresponde à versão remota.")

    # =====================================================
    # OPÇÃO 4 - CANCELAR
    # =====================================================
    elif opcao == '4':
        print("\nOperação cancelada pelo usuário.")
        return False

    else:
        print("\n❌ Opção inválida.")
        return False

    # =====================================================
    # FINALIZAÇÃO
    # =====================================================
    print("\n" + "=" * 60)
    print("📊 STATUS FINAL DO PROJETO")
    print("=" * 60)

    run_command("git status")

    input("\nPressione ENTER para continuar...")
    return True


def main():
    check_git_installed()

    github_user = get_name_user()
    if not github_user:
        return False
    if not configure_git_global(github_user):
        return False

    pasta_confirmado = False
    while True:
        print_header(f"Menu Principal - Assistente Git para {github_user}")
        print(f"Existe repositório em github.com/{github_user}/ ? ")
        print("[S] Sim, repositório já existe")
        print("[N] Não, quero criar um repositório novo")
        print("[U] Abrir menu de Utilitários diretos")
        print("\nEscolha uma opção (S, N, U ou X):")
        exist_repositoriong = input("➔  ").strip().lower()

        if exist_repositoriong == 'x':
            return False
        elif exist_repositoriong in ['s', 'sim']:

            name_repositoring = get_name_repositoring(github_user)
            if not name_repositoring:
                return False

            repo_url = f"https://github.com/{github_user}/{name_repositoring}.git"

            print_header("Menu Principal - Assistente Git")
            print(f"O que você deseja fazer com o repositório '{name_repositoring}' ?")
            print("[C] CLONAR repositório do GitHub para o computador (Baixar projeto)")
            print("[E] ENVIAR arquivos locais para o GitHub (RECRIAR histórico e sobrescrever o remoto)")
            print("[A] ATUALIZAR arquivos locais com as alterações do GitHub (Preservar histórico)")
            print("[U] UTILITÁRIOS do Git (Status, histórico, branches e configurações)")
            print("[V] VOLTAR ao menu principal")
            print("\nEscolha uma opção (C, E, A, U, V ou X): ")

            acao = input("➔  ").strip()

            if acao == 'x':
                return False
            elif acao == 'c':
                confirm_working_directory()
                print_header("Clonando Repositório")
                cmd = f"git clone {repo_url}"
                if run_command(cmd):
                    print(f"\n✅ Repositório '{name_repositoring}' clonado com sucesso!")
                    print(f"   Ele foi baixado em: {os.path.join(os.getcwd(), name_repositoring)}")

            elif acao == 'e':
                confirm_working_directory()
                print_header("Enviando Arquivos Locais para Repositório Existente")

                create_gitignore_if_missing()

                git_dir = Path(".git")
                if git_dir.exists():
                    shutil.rmtree(git_dir, ignore_errors=True)
                    print("➔ Remove todo o histórico local anterior, no Windows/Linux/macOS sem erros de permissão.")

                run_command("git init")
                print("➔  Iniciar git")

                run_command("git branch -M main")
                print("➔  Renomeado branch atual para main.")

                run_command("git add .")
                print("➔  Adicionado arquivos.")

                data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                commit_msg = f"{github_user} {data_hora} update"

                run_command(f'git commit -m "{commit_msg}"')
                print(f"➔  Criado commit automático com data e hora: '{commit_msg}'")

                remotes = run_command("git remote -v", show_output=False, capture=True, verbose=False)
                if "origin" in remotes:
                    run_command(f"git remote set-url origin {repo_url}")
                    print("➔  Atualizado URL do repositório remoto.")
                else:
                    run_command(f"git remote add origin {repo_url}")
                    print("➔  Adicionado repositório remoto.")

                success = run_command("git push origin main --force")
                print("➔  Enviado arquivos para o GitHub (forçado, histórico zerado).")

                if not success:
                    print("\n⚠️  O push falhou. Tentando resolver divergência de histórico...")

                    run_command("git pull origin main --allow-unrelated-histories --no-rebase")
                    print("➔  Executado git pull com allow-unrelated-histories.")

                    run_command("git push -u origin main")
                    print("➔  Tentado push novamente.")

                print("\n✅  Processo concluído com sucesso!")

            elif acao == 'a':
                update_from_github()

            elif acao == 'u':
                if not show_git_utilities():
                    return False

            elif acao == 'v':
                continue



        elif exist_repositoriong in ['n', 'nao', 'não']:
            confirm_working_directory()
            print_header("Criando Novo Repositório")
            name_repositoring = get_name_repositoring(github_user)
            if not name_repositoring:
                return False

            repo_url = f"https://github.com/{github_user}/{name_repositoring}.git"


            cli_created = create_github_repo_online(name_repositoring, github_user)

            create_gitignore_if_missing()

            if not os.path.exists(".git"):
                run_command("git init")
                print("➔  Inicializado repositório local.")

            run_command("git add .")
            print("➔  Adicionado todos os arquivos.")

            data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            commit_msg = f"{github_user} {data_hora} Initial"

            run_command(f'git commit -m "{commit_msg}"')
            print(f"➔ Criado commit inicial: '{commit_msg}'")

            run_command("git branch -M main")
            print("➔  Renomeado branch atual para main.")

            if not cli_created:
                remotes = run_command("git remote -v", show_output=False, capture=True, verbose=False)
                if "origin" in remotes:
                    run_command(f"git remote set-url origin {repo_url}")
                    print("➔  Alterado repositório remoto já existente.")
                else:
                    run_command(f"git remote add origin {repo_url}")
                    print("➔  Adicionado repositório remoto novo.")

            success = run_command("git push -u origin main")
            print("➔  Enviano arquivos para o GitHub.")

            if success:
                print(f"\n✅  Sucesso! Seu novo repositório está publicado em: https://github.com/{github_user}/{name_repositoring}")
            else:
                print(f"\n⚠️  O push não foi concluído. Verifique se o repositório (https://github.com/{github_user}/{name_repositoring}) foi criado corretamente no site do GitHub.")

        elif exist_repositoriong in ['u', 'utilitarios', 'utilitários']:
            show_git_utilities()


        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
