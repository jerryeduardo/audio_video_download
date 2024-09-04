import subprocess

def get_mp3_info(file_path):
    try:
        # Executa o comando ffprobe
        result = subprocess.run(
            ['ffprobe', '-v', 'error', '-show_entries', 'stream=sample_rate, bit_rate', '-of', 'default=noprint_wrappers=1:nokey=1', file_path],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        
        # Captura a saída do comando
        output = result.stdout.strip().split('\n')
        
        if len(output) == 2:
            sample_rate = int(output[0])
            bit_rate = int(output[1])
            
            print(f"Taxa de amostragem: {sample_rate / 1000} kHz")
            print(f"Taxa de bits: {bit_rate / 1000:.0f} kbps")
        else:
            print("Não foi possível obter as informações do arquivo.")
    
    except Exception as e:
        print(f"Erro ao executar o ffprobe: {e}")

def verify_audio():
    file_path = input("\nDigite o caminho do arquivo MP3: ")
    get_mp3_info(file_path)

if __name__ == "__main__":
    verify_audio()