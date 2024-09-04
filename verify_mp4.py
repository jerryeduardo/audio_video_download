import subprocess

def get_mp4_info(file_path):
    try:
        # Executa o comando ffprobe para obter largura, altura e bitrate do vídeo
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'stream=width,height,bit_rate', '-of', 'default=noprint_wrappers=1:nokey=1', file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        
        # Captura a saída do comando
        output = result.stdout.strip().split('\n')
        
        if len(output) >= 3:
            width = int(output[0])
            height = int(output[1])
            bit_rate = int(output[2])	
            bit_rate_kbps = bit_rate / 1000
            
            # Classifica a resolução
            if width >= 3840 and height >= 2160:
                resolution = "4K (Ultra HD)"
            elif width >= 2560 and height >= 1440:
                resolution = "2K (QHD/WQHD)"
            elif width >= 1920 and height >= 1080:
                resolution = "1080p (Full HD)"
            elif width >= 1280 and height >= 720:
                resolution = "720p (HD)"
            elif width >= 854 and height >= 480:
                resolution = "480p (FWVGA)"
            elif width >= 640 and height >= 360:
                resolution = "360p (nHD)"
            elif width >= 426 and height >= 240:
                resolution = "240p (Low)"
            elif width >= 256 and height >= 144:
                resolution = "144p (Very Low)"
            else:
                resolution = "Resolução abaixo de 144p ou não catalogada no código"
            
            print(f"Resolução do vídeo: {width}x{height} ({resolution})")
            print(f"Taxa de bits: {bit_rate_kbps / 1000:.2f} Mbps")
        else:
            print("Não foi possível obter as informações do arquivo.")
    
    except Exception as e:
        print(f"Erro ao executar o ffprobe: {e}")

def verify_video():
    file_path = input("\nDigite o caminho do arquivo MP4: ")
    get_mp4_info(file_path)

if __name__ == "__main__":
    verify_video()