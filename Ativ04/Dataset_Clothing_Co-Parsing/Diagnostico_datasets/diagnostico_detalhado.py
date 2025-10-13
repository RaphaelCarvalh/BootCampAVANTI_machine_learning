# ========================================
# CÉLULA DE DIAGNÓSTICO - Execute esta primeiro!
# ========================================

import os
import glob

print("🔍 DIAGNÓSTICO DETALHADO DA ESTRUTURA")
print("=" * 50)

# 1. Verificar estrutura completa do dataset
print("📁 Estrutura completa do dataset:")
for root, dirs, files in os.walk(BASE_DIR):
    level = root.replace(BASE_DIR, '').count(os.sep)
    indent = '  ' * level
    folder_name = os.path.basename(root)
    print(f"{indent}{folder_name}/")
    
    # Mostrar alguns arquivos de cada pasta
    subindent = '  ' * (level + 1)
    for i, file in enumerate(files):
        if i < 3:  # Mostrar apenas os 3 primeiros
            print(f"{subindent}{file}")
        elif i == 3:
            print(f"{subindent}... e mais {len(files)-3} arquivos")
            break

# 2. Procurar por arquivos PNG especificamente
print(f"\n🖼️ Procurando por arquivos PNG:")
png_files = []
for root, dirs, files in os.walk(BASE_DIR):
    for file in files:
        if file.endswith('.png'):
            relative_path = os.path.relpath(os.path.join(root, file), BASE_DIR)
            png_files.append(relative_path)

print(f"Total de arquivos PNG encontrados: {len(png_files)}")
if png_files:
    print("Primeiros 10 arquivos PNG:")
    for i, png_file in enumerate(png_files[:10]):
        print(f"  {png_file}")

# 3. Verificar especificamente por máscaras
print(f"\n🎭 Procurando por máscaras/labels:")
mask_patterns = ['*label*', '*mask*', '*seg*', '*colored*']
found_masks = []

for pattern in mask_patterns:
    pattern_files = glob.glob(os.path.join(BASE_DIR, '**', pattern), recursive=True)
    if pattern_files:
        print(f"Padrão '{pattern}': {len(pattern_files)} arquivos/pastas")
        for file in pattern_files[:3]:
            relative = os.path.relpath(file, BASE_DIR)
            print(f"  {relative}")
            found_masks.append(relative)

# 4. Comparar com caminhos do metadata
print(f"\n📋 Analisando caminhos no metadata:")
if 'df_metadata' in globals() and df_metadata is not None:
    label_paths = df_metadata['label_path'].unique()
    print(f"Caminhos únicos no metadata: {len(label_paths)}")
    
    print("Primeiros 5 caminhos do metadata:")
    for path in label_paths[:5]:
        full_path = os.path.join(BASE_DIR, path)
        exists = "✅" if os.path.exists(full_path) else "❌"
        print(f"  {exists} {path}")
    
    # Verificar quantos existem realmente
    existing_paths = []
    missing_paths = []
    
    for idx, row in df_metadata.iterrows():
        full_path = os.path.join(BASE_DIR, row['label_path'])
        if os.path.exists(full_path):
            existing_paths.append(row['label_path'])
        else:
            missing_paths.append(row['label_path'])
    
    print(f"\n📊 Resumo dos caminhos:")
    print(f"  Existem: {len(existing_paths)}")
    print(f"  Não existem: {len(missing_paths)}")
    print(f"  Taxa de sucesso: {len(existing_paths)/len(df_metadata)*100:.1f}%")

# ========================================
# CÉLULA DE CORREÇÃO AUTOMÁTICA
# ========================================

def encontrar_caminhos_corretos():
    """Tenta encontrar automaticamente os caminhos corretos"""
    print(f"\n🔧 TENTANDO CORREÇÃO AUTOMÁTICA")
    print("=" * 40)
    
    if 'df_metadata' not in globals() or df_metadata is None:
        print("❌ Metadados não carregados")
        return None
    
    # Coletar todos os arquivos PNG
    all_png_files = {}  # filename -> full_path
    
    for root, dirs, files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith('.png'):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, BASE_DIR)
                all_png_files[file] = relative_path
    
    print(f"Total de PNGs encontrados: {len(all_png_files)}")
    
    # Tentar mapear os caminhos do metadata
    df_corrigido = df_metadata.copy()
    caminhos_corrigidos = []
    nao_encontrados = []
    
    for idx, row in df_metadata.iterrows():
        original_path = row['label_path']
        filename = os.path.basename(original_path)
        
        if filename in all_png_files:
            novo_caminho = all_png_files[filename]
            caminhos_corrigidos.append(novo_caminho)
        else:
            caminhos_corrigidos.append(original_path)  # Manter original
            nao_encontrados.append(filename)
    
    # Atualizar DataFrame
    df_corrigido['label_path_original'] = df_metadata['label_path']
    df_corrigido['label_path'] = caminhos_corrigidos
    
    print(f"✅ Caminhos corrigidos: {len(caminhos_corrigidos) - len(nao_encontrados)}")
    print(f"❌ Não encontrados: {len(nao_encontrados)}")
    
    if nao_encontrados:
        print("Arquivos não encontrados:")
        for arquivo in nao_encontrados[:5]:
            print(f"  {arquivo}")
        if len(nao_encontrados) > 5:
            print(f"  ... e mais {len(nao_encontrados)-5}")
    
    return df_corrigido

# Executar correção
df_metadata_corrigido = encontrar_caminhos_corretos()

# ========================================
# CÉLULA DE TESTE COM CAMINHOS CORRIGIDOS
# ========================================

def testar_caminhos_corrigidos():
    """Testa a extração com os caminhos corrigidos"""
    print(f"\n🧪 TESTANDO COM CAMINHOS CORRIGIDOS")
    print("=" * 45)
    
    if df_metadata_corrigido is None:
        print("❌ Correção não foi executada")
        return
    
    # Filtrar apenas registros com arquivos existentes
    registros_validos = []
    for idx, row in df_metadata_corrigido.iterrows():
        full_path = os.path.join(BASE_DIR, row['label_path'])
        if os.path.exists(full_path):
            registros_validos.append(row)
    
    print(f"Registros com arquivos válidos: {len(registros_validos)}")
    
    if len(registros_validos) == 0:
        print("❌ Nenhum arquivo válido encontrado!")
        return
    
    # Testar os primeiros 3 registros válidos
    num_testes = min(3, len(registros_validos))
    
    for i in range(num_testes):
        row = registros_validos[i]
        print(f"\n--- TESTE {i+1} ---")
        print(f"Image ID: {row['image_id']}")
        print(f"Label Path Original: {row.get('label_path_original', 'N/A')}")
        print(f"Label Path Corrigido: {row['label_path']}")
        
        # Testar extração
        classes = extrair_classes_da_mascara(row['label_path'], df_classes, debug=True)
        print(f"🏷️ Classes encontradas: {classes}")
        print(f"📊 Total de classes: {len(classes)}")

# Executar teste
testar_caminhos_corrigidos()

# ========================================
# FUNÇÃO PARA ATUALIZAR O DATAFRAME GLOBAL
# ========================================

def aplicar_correcao():
    """Aplica a correção ao DataFrame global"""
    global df_metadata
    
    resposta = input(f"\n❓ Aplicar correção ao DataFrame principal? (s/n): ").lower().strip()
    
    if resposta == 's' and df_metadata_corrigido is not None:
        # Filtrar apenas registros com arquivos existentes
        df_filtrado = []
        for idx, row in df_metadata_corrigido.iterrows():
            full_path = os.path.join(BASE_DIR, row['label_path'])
            if os.path.exists(full_path):
                df_filtrado.append(row)
        
        if df_filtrado:
            df_metadata = pd.DataFrame(df_filtrado).reset_index(drop=True)
            print(f"✅ DataFrame atualizado com {len(df_metadata)} registros válidos")
            return True
        else:
            print("❌ Nenhum registro válido para aplicar")
            return False
    else:
        print("❌ Correção não aplicada")
        return False

print(f"\n🎯 PRÓXIMO PASSO:")
print("Execute: aplicar_correcao() para atualizar o DataFrame principal")

# ========================================
# FUNÇÃO PARA VERIFICAÇÃO FINAL
# ========================================

def verificacao_final():
    """Verificação final antes do processamento"""
    print(f"\n✅ VERIFICAÇÃO FINAL")
    print("=" * 25)
    
    if 'df_metadata' not in globals():
        print("❌ DataFrame não está carregado")
        return False
    
    # Testar alguns registros aleatórios
    sample_size = min(5, len(df_metadata))
    amostra = df_metadata.sample(n=sample_size)
    
    sucessos = 0
    for idx, row in amostra.iterrows():
        full_path = os.path.join(BASE_DIR, row['label_path'])
        if os.path.exists(full_path):
            sucessos += 1
    
    taxa_sucesso = sucessos / sample_size * 100
    print(f"Taxa de sucesso na amostra: {taxa_sucesso:.1f}% ({sucessos}/{sample_size})")
    
    if taxa_sucesso >= 80:
        print("✅ Pronto para processamento!")
        return True
    else:
        print("⚠️ Ainda há problemas com os caminhos")
        return False

print(f"\n🏁 Para verificação final, execute: verificacao_final()")