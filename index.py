from download_youdzer_mp3 import download_youdzer_audio
from download_mp3 import download_audio
from download_mp4 import download_video
from download_playlist_mp3 import download_playlist_audio
from download_playlist_mp4 import download_playlist_video
from verify_mp3 import verify_audio
from verify_mp4 import verify_video
from update_tags_url import update_tags_url_audio
from update_tags_artist_tracktitle import update_tags_artist_tracktitle_audio
from update_tags_all_mp3 import update_tags_all_mp3_audio

def main_menu():
    while True:
        print("Menu:")
        print("1. Baixar música ou playlist do YouTube com atualização de metatags com o Deezer")
        print("2. Baixar música do YouTube")
        print("3. Baixar vídeo do YouTube")
        print("4. Baixar playlist de músicas do YouTube")
        print("5. Baixar playlist de vídeos do YouTube")
        print("6. Verificar qualidade da música baixada pelo YouTube")
        print("7. Verificar qualidade do vídeo baixado pelo YouTube")
        print("8. Atualizar metatags com o Deezer pela URL da música")
        print("9. Atualizar metatags com o Deezer pelo nome do artista e título da música")
        print("10. Atualizar metatags de todas os mp3's da pasta com o Deezer")
        print("11. Sair")
        
        choice = input("\nEscolha uma opção (1/2/3/4/5/6/7/8/9/10/11): ")
        
        if choice == '1':
            download_youdzer_audio()

        elif choice == '2':
            download_audio()

        elif choice == '3':
            download_video()

        elif choice == '4':
            download_playlist_audio()

        elif choice == '5':
            download_playlist_video()

        elif choice == '6':
            verify_audio()

        elif choice == '7':
            verify_video()    

        elif choice == '8':
            update_tags_url_audio()

        elif choice == '9':
            update_tags_artist_tracktitle_audio()

        elif choice == '10':
            update_tags_all_mp3_audio()

        elif choice == '11':
            print("Saindo...")
            break

if __name__ == "__main__":
    main_menu()