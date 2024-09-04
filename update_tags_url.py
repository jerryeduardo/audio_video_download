import requests
import re
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TYER, TCON, APIC
from mutagen.id3 import ID3NoHeaderError
import os
from io import BytesIO
from PIL import Image
from update_tags_artist_tracktitle import add_cover_art_audio, update_mp3_tags_audio, rename_file_audio

DEEZER_API_BASE_URL = 'https://api.deezer.com'

def get_deezer_track_info_url_audio(track_url):
    # Extrai o ID da faixa da URL
    track_id_match = re.search(r'track/(\d+)', track_url)
    if not track_id_match:
        print("URL inválida. Não foi possível extrair o ID da faixa.")
        return {}
    
    try:
        track_id = track_id_match.group(1)
        
        # Buscar detalhes da faixa
        track_detail_url = f'{DEEZER_API_BASE_URL}/track/{track_id}'
        response = requests.get(track_detail_url)

        if response.status_code != 200:
            print(f"Erro ao buscar detalhes da faixa: {response.status_code}")
            return {}

        track_detail = response.json()
        
        # Obter informações detalhadas
        album = track_detail['album']['title']
        genre = track_detail['album'].get('genre', {}).get('name', '')
        release_date = track_detail['album'].get('release_date', '').split('-')[0]
        cover_url = track_detail['album'].get('cover_xl', '')

        return {
            'album': album,
            'artist': track_detail['artist']['name'],
            'title': track_detail['title'],
            'genre': genre,
            'year': release_date,
            'cover_url': cover_url
        }
    except (KeyError, IndexError):
        print("Informações não encontradas.")
        return {}

def update_tags_for_downloaded_file_url_audio(output_path, file_path):
        if not os.path.exists(file_path):
            print(f"\nO arquivo {file_path} não existe.")
            return
        
        print(f"\nPara o arquivo {file_path}:")
        track_url = input("Digite a url da música no Deezer (exemplo: https://api.deezer.com/track/2478544551 ou track/2478544551): ")
        info = get_deezer_track_info_url_audio(track_url)

        if info:
            update_mp3_tags_audio(file_path, info)
            add_cover_art_audio(file_path, info.get('cover_url'))
            new_file_name = rename_file_audio(file_path, info.get('artist', ''), info.get('title', ''))
            print(f"Arquivo renomeado para {new_file_name}")
        else:
            print("Não foi possível obter informações sobre a música.")
            # new_file_name = rename_file_audio(file_path, info.get('artist', ''), info.get('track_title', ''))
            # print(f"Arquivo renomeado para {new_file_name}")

def update_tags_url_audio():
    output_path = '.' # Diretório onde os arquivos serão salvos e pesquisados
    # Cria o diretório se não existir
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    file_path = input("\nDigite o título do arquivo com a extensão .mp3: ")
    update_tags_for_downloaded_file_url_audio(output_path, file_path)

if __name__ == "__main__":
    update_tags_url_audio()