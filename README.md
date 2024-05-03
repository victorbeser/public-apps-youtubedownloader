# Youtube Downloader por @victorbeser

Programa simples e básico para downloads utilizando Links do Youtube.

<h2>Módulos para Instalação:</h2>

Rode o comando abaixo para instalar as bibliotecas:

```powershel
pip install -r requirements.txt
```

<h2>Executáveis Windows e MacOS</h2>

Na pasta raíz do projeto você vai encontrar a pasta "executáveis", dentro dela você vai encontrar ambos executáveis para Windows e MacOS (Exec Unix).


<h2>Executáveis</h2>

Se algum dos executáveis não estiver funcionando no seu sistema, faça o download do "app.py" disponível na raíz do projeto e faça o download da biblioteca PyInstaller.

Utilize o seguinte comando em seu terminal (na pasta onde realizou o download do "app.py"): pyinstaller --onefile app.py

Espere terminar e o seu aplicativo executável estará disponível em 'dist/app'.

---

## Atualizar o desgin

A arquivo de design está na pasta inter > design.ui para acessar o mesmo basta abrir o arquivo no aplicativo QT Designer que pode ser baixado pelo link abaixo:

> Pasta inter significa interface.

## Aplicativo: Qt Designer
Após a instalação basta abrir o arquivo e realizar as alterações necessárias. Lembrando de salvar o arquivo na mesma pasta novamente.

## Atualizando o arquivo design.py
Para atualizar o arquivo design.py basta acessar a pasta inter e rodar o comanado abaixo:

```powershell
pyside6-uic inter/design.ui -o inter/design.py
```

## Gerando executável

Precisamos instalar o PyInstaller:

```powershell
pip install pyinstaller
```

## Para gerar um arquivo .exe exwecute o comando:

```powershell
pyinstaller --onefile -w app.py
```

---

## Informações Complementares

### Paleta de cor:

- Background: #2D3250
- Inputs: #424769
- Botão Escolher: #F7B176
- Botão Baixar: #C1D37F
- Outros: #676F9D

### Fonte

- Arial