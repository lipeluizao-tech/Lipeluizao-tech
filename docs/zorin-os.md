# Ambiente de desenvolvimento no Zorin OS

O Zorin OS é baseado em Ubuntu. Versão, arquitetura e hardware determinam os pacotes e recursos disponíveis. Este guia prepara uma base geral; as ferramentas anteriores ainda precisam ser identificadas no [inventário](ferramentas.md).

Os comandos abaixo são para executar no seu computador. Esta documentação não instala programas nele remotamente.

## 1. Identifique o sistema

```bash
cat /etc/os-release
uname -m
free -h
df -h "$HOME"
```

Registre versão do Zorin, arquitetura, RAM e espaço livre no inventário. Não publique hostname, números de série ou dados pessoais. Consulte a [ajuda oficial do Zorin](https://help.zorin.com/) para instalação de aplicativos e configurações.

## 2. Instale a base

No terminal do Zorin, com acesso de administrador:

```bash
sudo apt update
sudo apt install git curl ca-certificates build-essential python3 python3-venv python3-pip pipx tmux htop ripgrep
```

Essa base cobre Git, Python, compilação e terminal. Confira a saída do APT; a disponibilidade depende da versão e dos repositórios configurados. Mantenha verificação de assinaturas e TLS habilitada.

```bash
git --version
python3 --version
tmux -V
rg --version
```

Configure autoria com seu nome e, se preferir, o endereço privado `noreply` fornecido nas configurações de e-mail do GitHub:

```bash
git config --global user.name "SEU NOME"
git config --global user.email "SEU ENDEREÇO NOREPLY DO GITHUB"
```

Isso configura autoria, não autenticação. Siga a [documentação de autenticação do GitHub](https://docs.github.com/en/authentication) para HTTPS ou SSH; nunca coloque tokens em arquivos versionados.

## 3. Editor e linguagens

**VS Code:** use as [instruções oficiais para Linux](https://code.visualstudio.com/docs/setup/linux). O pacote `.deb` é uma opção no Zorin; após baixar o arquivo oficial, instale o arquivo específico com `sudo apt install ./nome-do-arquivo.deb`. Evite misturar instalações do editor sem necessidade.

**Python:** crie um ambiente por projeto, sem instalar bibliotecas no Python do sistema:

```bash
mkdir -p ~/Projetos/experimento-python
cd ~/Projetos/experimento-python
python3 -m venv .venv
source .venv/bin/activate
python -m pip --version
# Quando o projeto possuir requirements.txt:
# python -m pip install -r requirements.txt
```

**Node.js:** o [nvm](https://github.com/nvm-sh/nvm) permite manter versões por projeto. Siga a instalação oficial, confira a release e leia o script antes de executá-lo. Depois de instalar e carregar o nvm no terminal:

```bash
nvm install --lts
nvm use --lts
node --version
npm --version
```

Em projetos existentes, siga primeiro `.nvmrc`, manifestos e lockfile. Use `npm ci` quando houver `package-lock.json`; outros gerenciadores possuem comandos próprios.

**Docker:** instale quando o projeto exigir containers, seguindo as [instruções para Ubuntu](https://docs.docker.com/engine/install/ubuntu/) e conferindo a base Ubuntu do Zorin. Distribuições derivadas podem exigir ajuste do codinome. Verifique o contexto ativo ao usar Engine ou Desktop. O grupo `docker` concede privilégios equivalentes a root.

## 4. Sessões longas no terminal

O `tmux` permite sair do terminal e retornar à sessão:

```bash
tmux new -s estudos
# Ctrl+b, depois d: desconectar sem encerrar a sessão.
tmux attach -t estudos
```

Ele não mantém o computador acordado nem preserva processos após reinicialização. Para uma tarefa que precisa impedir suspensão enquanto roda:

```bash
systemd-inhibit --what=sleep --mode=block --why="Tarefa de desenvolvimento" bash
# Execute sua tarefa nesse shell; use exit ao terminar.
```

Isso depende do gerenciador de sessão respeitar a inibição. Ajustes ao fechar a tampa variam; confira as configurações de energia do Zorin. Para trabalhos longos, mantenha ventilação, alimentação estável e checkpoints. Observe CPU e RAM com `htop`. Salve resultados em arquivos; uma sessão não substitui backup.

## 5. Migre por projeto

- Copie código e documentos, mantendo backup do computador anterior quando disponível.
- Reinstale dependências pelos manifestos; recrie `.venv` e `node_modules` no Linux.
- Confira diferenças entre maiúsculas e minúsculas, caminhos e permissões de execução.
- Reconfigure extensões, atalhos e credenciais pelos mecanismos oficiais.
- Execute a aplicação e os testes antes de marcar a ferramenta como migrada.

O [catálogo de ferramentas](ferramentas.md) organiza a migração e verificações.
