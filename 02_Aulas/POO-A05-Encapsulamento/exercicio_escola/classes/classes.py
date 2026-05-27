#classes
class Escola:
  def __init__(self,nome_escola):
    self.nome_escola=nome_escola
    # self.nome_aluno='Desconhecido'
    # self.turma='Sem_turma'
    self.dicionario={}
    self.lista=[]

  def show(self):
    for k,v in enumerate(self.lista):
      print(f'chave: {k}, valor {v}')
     
  def cadastrar_aluno(self):
    nome=input('Nome do Aluno: ')
    turma=input('Nome da Turma: ')
    self.dicionario={
      'nome':nome,
      'turma':turma
    }
     
    # ['nome']=nome
    # self.dicionario['turma']=turma
    self.lista.append(self.dicionario)
    print(self.lista)
    


  def menu(self):
    while True:
      print("0-Saida\n1-Cadastrar Aluno\n2- Mostrar lista de Alunos")
      menu = input('Opção Escolhida: ')
      if menu =='0':
        break
      elif menu =='1':
        self.cadastrar_aluno()
      elif menu =='2':
        print(f'{self.show()}')
      else:
        print('ERRO, entrada invalida')