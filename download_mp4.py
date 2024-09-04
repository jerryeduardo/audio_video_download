import yt_dlp

def download_youtube_video(url, output_path='.'):
    ydl_opts = {
        'format': 'bestvideo[height<=2160]+bestaudio/best',  # Baixa o melhor formato disponível
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Modelo de nome do arquivo
	'merge_output_format': 'mp4',  # Mescla o vídeo e o áudio no formato mp4
    }

    try:
        print("Iniciando o download do vídeo...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            # Obtemos o título da música do dicionário de informações
            title = info_dict.get('title', 'unknown')
            # Adiciona a extensão .mp4 ao final do título
            file_name = f"{title}.mp4"
            print(f"Vídeo baixado e salvo com sucesso. \nTítulo do arquivo MP4 baixado: \n{file_name}")
            return file_name
    except Exception as e:
            print("Ocorreu um erro ao baixar o vídeo do YouTube.")
            return None

def download_video():
    url = input("\nDigite a URL do vídeo do YouTube: ")
    download_youtube_video(url)

if __name__ == "__main__":
    download_video()