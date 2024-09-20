import requests
import re
import os
from update_tags_artist_tracktitle import add_cover_art_audio, update_mp3_tags_audio, rename_file_audio, subtract_string, is_valid_directory
from output_dir import output_dir_create

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
        album_id = track_detail['album']['id']
        album = track_detail['album']['title']
        genre = track_detail['album'].get('genre', {}).get('name', '')
        release_date = track_detail['album'].get('release_date', '').split('-')[0]
        cover_url = track_detail['album'].get('cover_xl', '')

        # Buscar todas as faixas do álbum
        album_tracks_url = f'{DEEZER_API_BASE_URL}/album/{album_id}/tracks'
        response = requests.get(album_tracks_url)

        if response.status_code != 200:
            print(f"Erro ao buscar faixas do álbum: {response.status_code}")
            return {}

        album_tracks = response.json()['data']
        
        # Encontrar o número da faixa
        track_number = next((i + 1 for i, t in enumerate(album_tracks) if str(t['id']) == track_id), None)
        
        return {
            'album': album,
            'artist': track_detail['artist']['name'],
            'title': track_detail['title'],
            'genre': genre,
            'year': release_date,
            'cover_url': cover_url,
            'track_number': track_number
        }
    except (KeyError, IndexError):
        print("Informações não encontradas.")
        return {}

def update_tags_for_downloaded_file_url_audio(output_path, file_name_with_extension):
        # Faz a junção do caminho do diretório com o nome do arquivo acrescido da extensão, 
        # incluindo uma barra no meio das variáveis para acertar o caminho
        file_path = os.path.join(output_path, file_name_with_extension)

        if not os.path.exists(file_path):
            print(f"\nO arquivo {subtract_string(file_path)} não existe.")
            return
        
        print(f"\nPara o arquivo {subtract_string(file_path)}")
        track_url = input("Digite a URL da música no Deezer (exemplo: https://api.deezer.com/track/2478544551 ou track/2478544551): ")
        info = get_deezer_track_info_url_audio(track_url)

        if info:
            update_mp3_tags_audio(file_path, info)
            add_cover_art_audio(file_path, info.get('cover_url'))
            new_file_name = rename_file_audio(file_path, info.get('artist', ''), info.get('title', ''))
            print(f"Arquivo renomeado para {subtract_string(new_file_name)}")
        else:
            print("Não foi possível obter informações sobre a música.")

def update_tags_url_audio():
    choice = input("\nVocê deseja atualizar os metatados de um arquivo MP3 do diretório padrão? (Responda com 'S' para Sim ou 'N' para Não): ").upper()
    if choice == 'S':
        output_path = output_dir_create('mp3') # Diretório onde os arquivos serão salvos e pesquisados
        file_name_with_extension = input("\nDigite o título do arquivo com a extensão .mp3: ")
        update_tags_for_downloaded_file_url_audio(output_path, file_name_with_extension)
    elif choice == 'N':
        output_path= input("\nInforme o caminho do diretório onde está o arquivo MP3 (exemplo: /home/seuusuario/Downloads/): ")
        if not is_valid_directory(output_path):
            print(f"\nO caminho informado para o diretório é inválido.")
            while not is_valid_directory(output_path):
                output_path = input(f"Por favor, informe o caminho válido para o diretório: ")
                if not is_valid_directory(output_path):
                    print(f"\nO diretório informado ainda é inválido.")  
        file_name_with_extension = input("\nDigite o título do arquivo com a extensão .mp3: ")
        update_tags_for_downloaded_file_url_audio(output_path, file_name_with_extension)
    else: 
        print("\nVocê inseriu uma informação incorreta. Por favor, acesse a opção 8 do menu e tente novamente.")

if __name__ == "__main__":
    update_tags_url_audio()