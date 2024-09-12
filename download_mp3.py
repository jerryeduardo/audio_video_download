import yt_dlp
from output_dir import output_dir_create

def download_youtube_audio(url, output_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'postprocessor_args': [
            '-ar', '44100',
        ],
        'prefer_ffmpeg': True,
    }

    try:
        print("Iniciando o download da música...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            # Obtemos o título da música do dicionário de informações
            title = info_dict.get('title', 'unknown')
            # Adiciona a extensão .mp3 ao final do título
            file_name = f"{title}.mp3"
            print(f"Áudio baixado e salvo com sucesso. \nTítulo do arquivo MP3 baixado: \n{file_name}")
            return file_name
    except Exception as e:
            print("Ocorreu um erro ao baixar o áudio do YouTube.")
            return None

def download_audio():
    output_path = output_dir_create('mp3') # Diretório onde os arquivos serão salvos e pesquisados
    url = input("\nDigite a URL do vídeo do YouTube: ")
    download_youtube_audio(url, output_path)

if __name__ == "__main__":
    download_audio()