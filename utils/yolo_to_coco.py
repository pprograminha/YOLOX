import os
import json
import shutil
import random
from pathlib import Path
from PIL import Image
from sklearn.model_selection import train_test_split

# Configurações
data_dir = "data"  # Diretório atual com seus dados
output_dir = "datasets"  # Diretório de saída
coco_dir = os.path.join(output_dir, "COCO")
classes = ["Cracking", "Layer_shifting", "Off_platform", "Stringing", "Warping"]
train_ratio = 0.8  # 80% para treinamento, 20% para validação

# Criar estrutura de diretórios COCO
os.makedirs(os.path.join(coco_dir, "annotations"), exist_ok=True)
os.makedirs(os.path.join(coco_dir, "train2017"), exist_ok=True)
os.makedirs(os.path.join(coco_dir, "val2017"), exist_ok=True)

# Mapeamento de classes para IDs
class_to_id = {cls: idx for idx, cls in enumerate(classes)}

# Coletar todas as imagens e suas classes
all_images = []
for class_name in classes:
    class_dir = os.path.join(data_dir, class_name)
    for img_file in os.listdir(class_dir):
        if img_file.endswith('.jpg'):
            img_path = os.path.join(class_dir, img_file)
            all_images.append((img_path, class_name))

# Embaralhar e dividir os dados
random.shuffle(all_images)
train_images, val_images = train_test_split(all_images, train_size=train_ratio, random_state=42)

print(f"Total de imagens: {len(all_images)}")
print(f"Treinamento: {len(train_images)} imagens")
print(f"Validação: {len(val_images)} imagens")

# Função para criar anotações COCO
def create_coco_annotations(images, output_json):
    images_info = []
    annotations = []
    categories = []
    
    # Criar categorias
    for idx, class_name in enumerate(classes):
        categories.append({
            "id": idx,
            "name": class_name,
            "supercategory": "printer_defect"
        })
    
    annotation_id = 1
    image_id = 1
    
    for img_path, class_name in images:
        # Abrir imagem para obter dimensões
        with Image.open(img_path) as img:
            width, height = img.size
        
        # Adicionar informação da imagem
        img_filename = os.path.basename(img_path)
        images_info.append({
            "id": image_id,
            "file_name": img_filename,
            "width": width,
            "height": height
        })
        
        # Criar anotação (caixa delimitadora cobrindo toda a imagem)
        # Isso é um placeholder - você deve substituir por anotações reais
        annotations.append({
            "id": annotation_id,
            "image_id": image_id,
            "category_id": class_to_id[class_name],
            "bbox": [0, 0, width, height],  # [x, y, width, height]
            "area": width * height,
            "iscrowd": 0
        })
        
        annotation_id += 1
        image_id += 1
    
    # Criar dicionário COCO
    coco_data = {
        "images": images_info,
        "annotations": annotations,
        "categories": categories
    }
    
    # Salvar arquivo JSON
    with open(output_json, 'w') as f:
        json.dump(coco_data, f, indent=2)

# Criar anotações para treinamento
create_coco_annotations(
    train_images, 
    os.path.join(coco_dir, "annotations", "instances_train2017.json")
)

# Criar anotações para validação
create_coco_annotations(
    val_images, 
    os.path.join(coco_dir, "annotations", "instances_val2017.json")
)

# Copiar imagens para os diretórios correspondentes
def copy_images(images, target_dir):
    for img_path, _ in images:
        img_name = os.path.basename(img_path)
        shutil.copy(img_path, os.path.join(target_dir, img_name))

# Copiar imagens de treinamento
copy_images(train_images, os.path.join(coco_dir, "train2017"))

# Copiar imagens de validação
copy_images(val_images, os.path.join(coco_dir, "val2017"))

# Criar arquivo de classes
with open(os.path.join(coco_dir, "classes.txt"), 'w') as f:
    for class_name in classes:
        f.write(f"{class_name}\n")

print("Estrutura COCO criada com sucesso!")
print(f"Estrutura final em: {coco_dir}")
print("\nEstrutura de diretórios:")
for root, dirs, files in os.walk(coco_dir):
    level = root.replace(coco_dir, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for file in files[:5]:  # Mostrar apenas os primeiros 5 arquivos
        print(f"{subindent}{file}")
    if len(files) > 5:
        print(f"{subindent}... e mais {len(files) - 5} arquivos")