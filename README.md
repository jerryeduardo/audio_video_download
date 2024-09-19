# youdzer
<img align="right" src="https://github.com/jerryeduardo/youdzer/blob/main/screenshot/preview.png" alt="image" />
O <b>YouDzer</b> é uma ferramenta que simplifica o download de músicas e vídeos do YouTube. Além disso, oferece verificação da qualidade dos arquivos baixados e permite a atualização dos metadados das músicas utilizando informações do Deezer.

## Installation
Primeiramente, se o pacote Git não estiver instalado, inicie o processo de instalação:
```
sudo apt install git
```
Agora clone este repositório:
```
cd ~/Downloads
git clone https://github.com/jerryeduardo/youdzer
```
Então vá para o diretório youdzer:
```
cd ~/Downloads/youdzer/
```
Instale o Python 3 e suas dependências (pip e venv) com:
```
./install_python3_ffmpeg.sh
```
Em seguida, crie o ambiente virtual do Python 3, instale as bibliotecas necessárias e adicione os arquivos com:
```
./install_venv_libs_files.sh
```
Se desejar remover o YouDzer, você pode fazê-lo executando o arquivo remove_venv_libs_files.sh com:
```
./remove_venv_libs_files.sh
```
Agora você pode usar o YouDzer em seu sistema acessando o menu de aplicativos e clicando no ícone do YouDzer.
```