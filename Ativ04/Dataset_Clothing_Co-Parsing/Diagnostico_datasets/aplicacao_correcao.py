# EXECUTE ESTA CÉLULA PARA APLICAR CORREÇÕES
# ========================================

# 1. Aplicar a correção automaticamente (sem input manual)
def aplicar_correcao_automatica():
    """Aplica a correção ao DataFrame principal automaticamente"""
    global df_metadata
    
    print("🔧 APLICANDO CORREÇÃO AUTOMÁTICA")
    print("=" * 35)
    
    if 'df_metadata_corrigido' not in globals() or df_metadata_corrigido is None:
        print("❌ Correção não foi executada")
        return False
    
    # Filtrar apenas registros com arquivos existentes
    registros_validos = []
    for idx, row in df_metadata_corrigido.iterrows():
        full_path = os.path.join(BASE_DIR, row['label_path'])
        if os.path.exists(full_path):
            registros_validos.append(row)
    
    if registros_validos:
        df_metadata = pd.DataFrame(registros_validos).reset_index(drop=True)
        print(f"✅ DataFrame atualizado com {len(df_metadata)} registros válidos")
        print(f"📊 Redução: {2098 - len(df_metadata)} registros removidos (arquivos não existentes)")
        return True
    else:
        print("❌ Nenhum registro válido encontrado")
        return False

# 2. Atualizar função de extração para filtrar 'nan'
def extrair_classes_da_mascara_v2(mask_path, df_classes, debug=False):
    """
    Versão melhorada que filtra classes inválidas como 'nan'
    """
    # Construir caminho completo
    if not os.path.isabs(mask_path):
        caminho_completo = os.path.join(BASE_DIR, mask_path)
    else:
        caminho_completo = mask_path
    
    # Verificar se arquivo existe
    if not os.path.exists(caminho_completo):
        if debug:
            print(f"⚠️ Arquivo não encontrado: {caminho_completo}")
        return []
    
    try:
        # Carregar imagem com PIL
        with Image.open(caminho_completo) as img:
            # Garantir que está em RGB
            if img.mode != 'RGB':
                img = img.convert('RGB')
            mask_array = np.array(img)
        
        if debug:
            print(f"📏 Dimensões da máscara: {mask_array.shape}")
        
        # Encontrar cores únicas
        pixels = mask_array.reshape(-1, 3)
        unique_colors = np.unique(pixels, axis=0)
        
        if debug:
            print(f"🎨 Cores únicas encontradas: {len(unique_colors)}")
        
        # Mapear cores para classes
        classes_encontradas = []
        classes_invalidas = ['null', 'nan', '', None]  # Classes para filtrar
        
        for color in unique_colors:
            r, g, b = int(color[0]), int(color[1]), int(color[2])
            
            # Buscar classe correspondente
            matches = df_classes[
                (df_classes['r'] == r) & 
                (df_classes['g'] == g) & 
                (df_classes['b'] == b)
            ]
            
            if len(matches) > 0:
                class_name = matches['class_name'].iloc[0]
                
                # Filtrar classes inválidas e duplicatas
                if (class_name not in classes_invalidas and 
                    class_name not in classes_encontradas and
                    pd.notna(class_name)):  # Filtrar NaN do pandas também
                    
                    classes_encontradas.append(class_name)
                    if debug:
                        print(f"  ✅ {class_name} <- RGB({r}, {g}, {b})")
                elif debug and class_name in classes_invalidas:
                    print(f"  🚫 {class_name} (filtrada) <- RGB({r}, {g}, {b})")
            elif debug:
                print(f"  ❓ RGB({r}, {g}, {b}) não mapeada")
        
        return classes_encontradas
        
    except Exception as e:
        if debug:
            print(f"❌ Erro ao processar {caminho_completo}: {e}")
        return []

# 3. Aplicar correções
print("🚀 INICIANDO APLICAÇÃO DE CORREÇÕES")
correcao_aplicada = aplicar_correcao_automatica()

if correcao_aplicada:
    # Atualizar função global
    extrair_classes_da_mascara = extrair_classes_da_mascara_v2
    print("✅ Função de extração atualizada (filtra 'nan')")
    
    # Verificação final
    print(f"\n🔍 VERIFICAÇÃO FINAL")
    print("=" * 25)
    
    # Testar alguns registros
    amostra_teste = df_metadata.sample(n=min(3, len(df_metadata)))
    
    for i, (idx, row) in enumerate(amostra_teste.iterrows()):
        print(f"\n--- TESTE {i+1} ---")
        classes = extrair_classes_da_mascara(row['label_path'], df_classes)
        print(f"Image ID: {row['image_id']}")
        print(f"Classes: {classes} ({len(classes)} classes)")
    
    print(f"\n✅ PIPELINE PRONTO!")
    print(f"📊 Dataset final: {len(df_metadata)} imagens válidas")
    print(f"🎯 Próximo passo: Execute as células de processamento (CÉLULA 7 em diante)")

else:
    print("❌ Não foi possível aplicar as correções")

# ========================================
# CÉLULA DE PROCESSAMENTO RÁPIDO (AMOSTRA MAIOR)
# ========================================

def processar_amostra_grande(n_amostras=200):
    """Processa uma amostra maior para validar o pipeline"""
    print(f"\n⚙️ PROCESSANDO AMOSTRA DE {n_amostras} REGISTROS")
    print("=" * 50)
    
    if 'df_metadata' not in globals() or len(df_metadata) == 0:
        print("❌ DataFrame não está pronto")
        return None
    
    # Selecionar amostra
    n_real = min(n_amostras, len(df_metadata))
    df_amostra = df_metadata.sample(n=n_real).copy()
    
    # Processar
    todas_classes = []
    processados = 0
    com_classes = 0
    
    print("Processando...")
    for idx, row in df_amostra.iterrows():
        classes = extrair_classes_da_mascara(row['label_path'], df_classes)
        todas_classes.append(classes)
        
        processados += 1
        if len(classes) > 0:
            com_classes += 1
        
        # Progress a cada 25
        if processados % 25 == 0:
            print(f"  {processados}/{n_real} processados ({com_classes} com classes)")
    
    # Adicionar ao DataFrame
    df_amostra['classes'] = todas_classes
    df_resultado = df_amostra[df_amostra['classes'].apply(len) > 0].copy()
    
    print(f"\n✅ RESULTADO DA AMOSTRA:")
    print(f"   Processados: {processados}")
    print(f"   Com classes: {len(df_resultado)}")
    print(f"   Taxa de sucesso: {len(df_resultado)/processados*100:.1f}%")
    
    # Mostrar estatísticas das classes
    if len(df_resultado) > 0:
        todas_classes_flat = []
        for classes_list in df_resultado['classes']:
            todas_classes_flat.extend(classes_list)
        
        contador = Counter(todas_classes_flat)
        print(f"\n🏷️ Classes mais comuns na amostra:")
        for classe, count in contador.most_common(10):
            print(f"   {classe}: {count} ocorrências")
    
    return df_resultado

# Executar processamento da amostra grande se correção foi aplicada
if 'correcao_aplicada' in locals() and correcao_aplicada:
    print(f"\n" + "="*60)
    df_amostra_resultado = processar_amostra_grande(200)
    
    if df_amostra_resultado is not None:
        print(f"\n🎉 PIPELINE VALIDADO COM SUCESSO!")
        print(f"✅ Pronto para processar dataset completo")
        print(f"📊 Amostra processada: {len(df_amostra_resultado)} imagens com classes")
else:
    print(f"\n⚠️ Execute a correção primeiro")