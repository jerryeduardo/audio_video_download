import yt_dlp

def download_youtube_playlist_video(playlist_url, output_path='.'):
    ydl_opts = {
        'format': 'bestvideo[height<=2160]+bestaudio/best',  # Baixa o melhor formato disponível
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',  # Modelo de nome do arquivo
	    'merge_output_format': 'mp4',  # Mescla o vídeo e o áudio no formato mp4
    }
    
    try:
        print("Iniciando o download da playlist...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(playlist_url, download=True)
        titles = [entry['title'] for entry in info_dict['entries']]
        # Adiciona a extensão .mp4 ao final de cada título
        titles_with_extension = [f"{title}.mp4" for title in titles]
        print(f"Playlist baixada e salva com sucesso. \nTítulos dos arquivos MP4 baixados: ")
        for title in titles_with_extension:
            print(f"{title}")
        return titles_with_extension
    except Exception as e:
            print("Ocorreu um erro ao baixar a playlist do YouTube.")
            return []
    
def download_playlist_video():
    url = input("\nDigite a URL da playlist do YouTube: ")
    download_youtube_playlist_video(url)

if __name__ == "__main__":
    download_playlist_video()