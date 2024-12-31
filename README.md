# Trabalho-Final-Intelig-ncia-Computacional

Este repositório contém o código-fonte, documentação e recursos relacionados ao Trabalho Final de Inteligência Computacional. 

# Guia de Instalação do Python e Configuração de Ambiente Virtual

Este guia explica como instalar o Python, criar um ambiente virtual e instalar dependências a partir de um arquivo `requirements.txt`.

---

## 1. Instalar o Python

### Linux:
1. No terminal, use o gerenciador de pacotes da sua distribuição para instalar o Python. Por exemplo:
   - Para distribuições baseadas em Debian/Ubuntu:
     ```bash
     sudo apt update
     sudo apt install python3 python3-pip
     ```
   - Para distribuições baseadas em Fedora:
     ```bash
     sudo dnf install python3 python3-pip
     ```

2. Certifique-se de que o Python está instalado verificando a versão:
   ```bash
   python3 --version
   ```

---

## 2. Criar um Ambiente Virtual

Um ambiente virtual é usado para isolar dependências de projetos Python.
0. clone o repositório:
```bash
   git clone https://github.com/alguiguilo098/Trabalho-Final-Inteligencia-Computacional.git
```
1. No terminal, navegue até a pasta do seu projeto:
   ```bash
   cd /caminho/para/seu/projeto
   ```

2. Crie o ambiente virtual:
   ```bash
   python3 -m venv env
   ```
   Aqui, `env` é o nome do ambiente virtual. Você pode substituí-lo por outro nome, se preferir.

3. Ative o ambiente virtual:
   ```bash
   source env/bin/activate
   ```

4. Certifique-se de que o ambiente virtual está ativo. Você verá o nome do ambiente virtual no início da linha do terminal:
   ```
   (env) $
   ```

---

## 3. Instalar Dependências do `requirements.txt`

1. Com o ambiente virtual ativo, instale as dependências listadas no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

2. Verifique se as dependências foram instaladas corretamente:
   ```bash
   pip list
   ```

---

## 4. Desativar o Ambiente Virtual

Quando terminar de trabalhar no seu projeto, desative o ambiente virtual com:
```bash
 deactivate
```

