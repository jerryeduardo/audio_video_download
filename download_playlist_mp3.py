import yt_dlp

def download_youtube_playlist_audio(playlist_url, output_path='.'):
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
        'noplaylist': False,
    }
    
    try:
        print("Iniciando o download da playlist...")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(playlist_url, download=True)
        titles = [entry['title'] for entry in info_dict['entries']]
        # Adiciona a extensão .mp3 ao final de cada título
        titles_with_extension = [f"{title}.mp3" for title in titles]
        print(f"Playlist baixada e salva com sucesso. \nTítulos dos arquivos MP3 baixados: ")
        for title in titles_with_extension:
            print(f"{title}")
        return titles_with_extension
    except Exception as e:
            print("Ocorreu um erro ao baixar a playlist do YouTube.")
            return []
    
def download_playlist_audio():
    url = input("\nDigite a URL da playlist do YouTube: ")
    download_youtube_playlist_audio(url)

if __name__ == "__main__":
    download_playlist_audio()