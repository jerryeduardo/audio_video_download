import yt_dlp

def download_youtube_audio(url, output_path='.'):
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
    url = input("\nDigite a URL do vídeo do YouTube: ")
    download_youtube_audio(url)

if __name__ == "__main__":
    download_audio()