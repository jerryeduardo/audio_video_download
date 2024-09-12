import os

def output_dir_create(name_dir):
    file_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(file_dir, name_dir)
    # Cria o diretório se não existir
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    return output_path