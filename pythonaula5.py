alunos =  [
    {"nome": "Rodrigo", "matricula": 1},
    {"nome": "João", "matricula": 2},
    {"nome": "André", "matricula": 3}
]

cursos = [
          {"nome": "Python 1", "professor": "prof 1", "id": 1, "dependencias": []},
          {"nome": "Python 2", "professor": "prof 2", "id": 2, "dependencias": [1, 3]},
          {"nome": "Estatística", "professor": "prof 3", "id": 3, "dependencias": [4]},
          {"nome": "Algebra", "professor": "prof 4", "id": 4, "dependencias": []},
          {"nome": "R", "professor": "prof 3", "id": 5, "dependencias": [1, 3]}
]

turmas = [
      {"id_cursos": 1, "lista_inscritos": [1, 3], "ano": 2019},
      {"id_cursos": 3, "lista_inscritos": [2], "ano": 2018},
      {"id_cursos": 2, "lista_inscritos": [2], "ano": 2019}
]

id_python = [curso for curso in cursos if (curso["nome"] == "Python 1")][0]["id"]
inscritos_python = [turma for turma in turmas
                    if (turma["id_cursos"] == id_python)][0]["lista_inscritos"]
Nomes_alunos = [aluno["nome"] for aluno in alunos if (aluno["matricula"] in inscritos_python)]

print (Nomes_alunos)
