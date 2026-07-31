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

def print_header(title):
    print("\n" + "=" * 65)
    print(f"  {title.upper()}")
    print("=" * 65)


def run_command(command, show_output=True, capture=False, verbose=True, time_seep=0):
    """
    Executa um comando no terminal com suporte a feedback visual.
    """
    if verbose and show_output:
        text = f"⛏️  {command}"
        text = text.ljust(80)      
        for i in range(2, 0, -1):
            text_print = text +  '| ⏳ ' + str(i) + ' seg.'
            print(f'\r{text_print}', end='')
            time.sleep(1)
        print(f'\r{text}', end=' | ')

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
        print("    👉 https://git-scm.com/install/windows")
        sys.exit(1)

def check_gh_installed():
    """Verifica se o GitHub CLI (gh) está instalado."""
    res = run_command("gh --version", show_output=False, capture=True, verbose=False)
    return bool(res)

def check_gh_authenticated():
    """Verifica se o usuário está autenticado no GitHub CLI."""
    res = run_command("gh auth status", show_output=False, capture=True, verbose=False)
    return bool(res)

def confirm_working_directory():
    """Exibe e confirma/altera o diretório de trabalho local do projeto com validação."""
    while True:
        current_dir = os.getcwd()
        
        opcao = input(f"Deseja executar a ação na pasta {current_dir}? [S/n]: ").strip().lower()
        
        if opcao not in ['n', 'nao', 'não']:
            print(f"✅ Usando diretório: {current_dir}")
            break
            
        novo_caminho = input("\n👉 Digite ou cole o caminho completo da pasta desejada: ").strip().strip('"')
        
        if os.path.exists(novo_caminho) and os.path.isdir(novo_caminho):
            os.chdir(novo_caminho)
            print(f"✅ Diretório alterado com sucesso para: {os.getcwd()}")
            break
        else:
            print("\n❌ ERRO: Caminho inválido ou pasta não encontrada!")
            print("Por favor, tente novamente digitando o caminho correto ou confirme a pasta atual.")

def configure_git_global(username):
    """Configura o usuário e branch padrão se necessário."""
    print_header("Configuração Global do Git")
    
    current_user = run_command("git config --global user.name", show_output=False, capture=True, verbose=False)
    current_email = run_command("git config --global user.email", show_output=False, capture=True, verbose=False)
    
    print(f"Nome global atual : {current_user if current_user else 'Não configurado'}")
    print(f"Email global atual: {current_email if current_email else 'Não configurado'}")
    
    if not current_user or not current_email:
        print("\nConfigurando credenciais globais do Git...")
        email = input(f"Informe o seu e-mail do GitHub (ex: {username}@gmail.com): ").strip()
        run_command(f'git config --global user.name "{username}"')
        run_command(f'git config --global user.email "{email}"')
        run_command('git config --global init.defaultBranch main')
        print("✅ Configuração global salva com sucesso!")
    else:
        opcao = input("Deseja atualizar suas configurações globais (Nome/Email)? (s/N): ").strip().lower()
        if opcao == 's':
            novo_nome = input(f"Novo user.name [{current_user}]: ").strip() or current_user
            novo_email = input(f"Novo user.email [{current_email}]: ").strip() or current_email
            run_command(f'git config --global user.name "{novo_nome}"')
            run_command(f'git config --global user.email "{novo_email}"')
            run_command('git config --global init.defaultBranch main')
            print("✅ Configuração global atualizada!")

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
    
    print("O que você deseja remover do rastreamento do Git?")
    print("1. node_modules (React Native / Node)")
    print("2. venv (Python)")
    print("3. Outro arquivo/pasta personalizado")
    
    opcao = input("\nEscolha uma opção (1-3) [padrão 1]: ").strip()
    
    if opcao == '2':
        target = "venv"
    elif opcao == '3':
        target = input("Digite o nome exato da pasta ou arquivo: ").strip()
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
            print(f"\n✅ SUCESSO: '{target}' foi removido do site do GitHub e continuará salvo no seu computador!")
        else:
            print(f"\n⚠️ O push falhou. Execute 'git push' manualmente após verificar seu repositório.")
    else:
        print(f"\n⚠️ Não foi possível remover '{target}'. Verifique se o nome está correto ou se já não foi removido.")

def create_github_repo_online(repo_name, github_user, is_private=False):
    """Cria o repositório diretamente no GitHub usando o GitHub CLI se disponível."""
    if check_gh_installed():
        if check_gh_authenticated():
            visibility = "--private" if is_private else "--public"
            print(f"\n✅ Tentando criar repositório '{repo_name}' diretamente no GitHub via GitHub CLI (gh)...")
            cmd = f"gh repo create {repo_name} {visibility} --source=. --remote=origin"
            if run_command(cmd):
                print(f"✅ Repositório '{repo_name}' criado no GitHub com sucesso!")
                return True
        else:
            print("\nℹ️ GitHub CLI detectado, mas você não está logado.")
            print("   Dica: Rode 'gh auth login' no terminal para criar repositórios automaticamente no futuro.")
    
    print("\n" + "="*60)
    print("📌 INSTRUÇÕES PARA CRIAR O REPOSITÓRIO NO SITE DO GITHUB")
    print("="*60)
    print("Como criar o repositório manualmente no site:")
    print(f"1. Acesse: https://github.com/{github_user}")
    print(f"2. Em 'Repository name', crie NEW repositório com nome: {repo_name}")
    print("3. Escolha Public ou Private.")
    print("4. ATENÇÃO: NÃO marque 'Add a README file', NÃO adicione .gitignore e nem Licença.")
    print("   (Como já temos arquivos locais, o repositório deve ser criado VAZIO).")
    print("5. Clique no botão verde 'Create repository'.")
    print("="*60)
    input("\nPressione ENTER assim que tiver criado o repositório no site...")
    return False

def show_git_utilities():
    """Submenu de ferramentas utilitárias do Git com suporte a --no-pager."""
    while True:
        print_header("Menu de Utilitários e Verificação Git")
        print("1. Ver Status atual (git status)")
        print("2. Ver Histórico resumido (git log --oneline)")
        print("3. Ver Histórico completo (git log)")
        print("4. Ver Histórico detalhado (git reflog)")
        print("5. Ver Branches locais (git branch)")
        print("6. Ver Remotos configurados (git remote -v)")
        print("7. Criar/Alternar para nova Branch")
        print("8. Desfazer/Resetar alterações (git reset)")
        print("9. Apagar pasta do GitHub sem apagar do PC (ex: node_modules ou venv)")
        print("0. Voltar ao menu principal")
        
        escolha = input("\nEscolha uma opção (0-9): ").strip()
        
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
            print("a) Reset leve (reverte commits mantendo arquivos) ➔ git reset --soft HEAD~1")
            print("b) Reset HARD (descarta TODAS as alterações não salvas) ➔ git reset --hard HEAD")
            sub = input("Escolha (a/b) ou ENTER para cancelar: ").strip().lower()
            if sub == 'a':
                run_command("git reset --soft HEAD~1")
            elif sub == 'b':
                conf = input("TEM CERTEZA? Isso apaga mudanças não salvas. (s/N): ").strip().lower()
                if conf == 's':
                    run_command("git reset --hard HEAD")
        elif escolha == '9':
            remove_cached_files()
        elif escolha == '0':
            break
        else:
            print("Opção inválida.")

def main():
    check_git_installed()
    
    print_header("Assistente Automatizado de Git & GitHub")
    print("Este script guia e executa todos os passos de Git para você.\n")
    
    github_user = input("Qual o nome do seu github? ").strip()
    if not github_user:
        github_user = "davigopi"
        print(f"➔ Usando usuário padrão: {github_user}")
        
    configure_git_global(github_user)
    
    while True:
        print_header("Menu Principal - Assistente Git")
        print(f"Usuário atual: github.com/{github_user}")
        print("-----------------------------------------------------------------")
        print("Existe repositório em github.com? ")
        print("[S] Sim, repositório já existe")
        print("[N] Não, quero criar um repositório novo")
        print("[U] Abrir menu de Utilitários diretos")
        print("[0] Sair do programa")
        
        existe_repo = input("\nEscolha uma opção (S/N/U/0): ").strip().lower()
        
        if existe_repo in ['s', 'sim']:
            repo_name = input(f"\nQual o nome do repositório que já existe no github.com/{github_user}? ").strip()
            if not repo_name:
                print("⚠️ Nome do repositório é obrigatório.")
                continue

            repo_url = f"https://github.com/{github_user}/{repo_name}.git"
            
            print(f"\nO que você deseja fazer com o repositório '{repo_name}'?")
            print("1. CLONAR o repositório do GitHub para este computador")
            print("2. ENVIAR os arquivos deste computador para o GitHub")
            print("3. Abrir menu de Utilitários / Verificações do Git")
            print("0. Voltar ao menu principal")
            
            acao = input("\nEscolha uma opção (1, 2, 3 ou 0): ").strip()
            
            if acao == '1':
                confirm_working_directory()
                print_header("Clonando Repositório")
                cmd = f"git clone {repo_url}"
                if run_command(cmd):
                    print(f"\n✅ Repositório '{repo_name}' clonado com sucesso!")
                    print(f"   Ele foi baixado em: {os.path.join(os.getcwd(), repo_name)}")
                
            elif acao == '2':
                confirm_working_directory()
                print_header("Enviando Arquivos Locais para Repositório Existente")
                
                create_gitignore_if_missing()
                
                if not os.path.exists(".git"):
                    run_command("git init")
                    print("➔  Repositório Git local.")
                
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
                    
                success = run_command("git push -u origin main")
                print("➔  Enviado arquivos para o GitHub.")
                
                if not success:
                    print("\n⚠️  O push falhou. Tentando resolver divergência de histórico...")
                    
                    run_command("git pull origin main --allow-unrelated-histories --no-rebase")
                    print("➔  Executado git pull com allow-unrelated-histories.")

                    run_command("git push -u origin main")
                    print("➔  Tentado push novamente.")
                    
                print("\n✅  Processo concluído com sucesso!")

            elif acao == '3':
                show_git_utilities()
            elif acao == '0':
                continue

        elif existe_repo in ['n', 'nao', 'não']:
            confirm_working_directory()
            print_header("Criando Novo Repositório")
            repo_name = input(f"Qual o nome do repositório que você quer criar em github.com/{github_user}? ").strip()
            if not repo_name:
                print("⚠️ Nome do repositório é obrigatório.")
                continue

            repo_url = f"https://github.com/{github_user}/{repo_name}.git"
            
            cli_created = create_github_repo_online(repo_name, github_user)
            
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
                print(f"\n✅  Sucesso! Seu novo repositório está publicado em: https://github.com/{github_user}/{repo_name}")
            else:
                print(f"\n⚠️  O push não foi concluído. Verifique se o repositório (https://github.com/{github_user}/{repo_name}) foi criado corretamente no site do GitHub.")

        elif existe_repo in ['u', 'utilitarios', 'utilitários']:
            show_git_utilities()

        elif existe_repo == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()