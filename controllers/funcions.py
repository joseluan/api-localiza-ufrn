import re

def get_disciplinas(pdf_raw:str):
    regex = re.compile(r'^\d{4}\.\d+\s+(?P<codigo_displina>[^\s]+)\s*(?P<nome_disciplina>.+)\s+(?P<docentes>.*)', flags=re.MULTILINE|re.IGNORECASE)
    disciplinas = {}
    for disciplina in regex.finditer(pdf_raw):
        disciplinas[disciplina.group('codigo_displina')] = []
        disciplinas[disciplina.group('codigo_displina')].append({
            'codigo': disciplina.group('codigo_displina'),
            'nome_disciplina': disciplina.group('nome_disciplina'),
            'docentes': disciplina.group('docentes')
        })
        
    return disciplinas


def get_horarios(pdf_raw:str):
    regex = re.compile(r'(?P<horario>\d{2}\:\d{2}\s+\-\s+\d{2}\:\d{2})\s+(?P<dom>[^\s]*)\s+(?P<seg>[^\s]*)\s+(?P<ter>[^\s]*)\s+(?P<qua>[^\s]*)\s+(?P<qui>[^\s]*)\s+(?P<sex>[^\s]*)\s+(?P<sab>[^\s]*)')
    horarios = {}
    for horario in regex.finditer(pdf_raw):
        horarios[horario.group('horario')] = []
        semana = ['dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab']
        for dia in semana:
            disciplina = horario.group(dia)
            if '---' not in disciplina:
                horarios[horario.group('horario')].append({
                    'dia': dia,
                    'disciplina': disciplina 
                })
    return horarios