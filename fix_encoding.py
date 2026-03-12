import os
import glob

# Map of corrupted => correct
fixes = {
    'marÃ§o': 'março',
    'MissÃ£o': 'Missão',
    'NotÃ­cias': 'Notícias',
    'Ãºltimas': 'últimas',
    'atualizaÃ§Ãµes': 'atualizações',
    'capacitaÃ§Ã£o': 'capacitação',
    'polÃ­tica': 'política',
    'lÃ­deres': 'líderes',
    'prÃ³ximas': 'próximas',
    'eleiÃ§Ãµes': 'eleições',
    'diretÃ³rio': 'diretório',
    'lanÃ§amento': 'lançamento',
    'formaÃ§Ã£o': 'formação',
    'Ã©tica': 'ética',
    'reÃºne': 'reúne',
    'estratÃ©gias': 'estratégias',
    'Ãndice': 'Índice',
    'aprovaÃ§Ã£o': 'aprovação',
    'ConheÃ§a': 'Conheça',
    'sustentÃ¡vel': 'sustentável',
    'transformaÃ§Ã£o': 'transformação',
    'responsÃ¡vel': 'responsável',
    'trÃªs': 'três',
    'teÃ³rica': 'teórica',
    'ciÃªncia': 'ciência',
    'comunicaÃ§Ã£o': 'comunicação',
    'lideranÃ§a': 'liderança',
    'lideranÃ§as': 'lideranças',
    'renovaÃ§Ã£o': 'renovação',
    'eficiÃªncia': 'eficiência',
}

files = glob.glob(r'C:\Users\vinic\Documents\Projetos\missaoto\**\*.html', recursive=True)
count = 0

for fpath in files:
    try:
        content = open(fpath, 'r', encoding='utf-8').read()
        orig = content
        for bad, good in fixes.items():
            if bad in content:
                content = content.replace(bad, good)
        
        if content != orig:
            count += 1
            open(fpath, 'w', encoding='utf-8').write(content)
            print('Fixed: ' + os.path.basename(fpath))
    except Exception as e:
        print('Error in ' + fpath + ': ' + str(e))

print('Total files fixed: ' + str(count))
