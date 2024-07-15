from datetime import datetime

class Tarefa:
    def __init__(self,id, titulo, descricao, prazo, prioridade):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.data_de_criacao = datetime.now()
        self.prazo = prazo
        self.prioridade = prioridade
        self.status = "Pendente"
    
    def marcar_como_concluida(self):
        self.status = "Concluída"

    def __str__(self):
        return f"\nId: {self.id}\nTítulo: {self.titulo}\nDescrição: {self.descricao}\nPrazo: {self.prazo}\nPrioridade: {self.prioridade}\nStatus: {self.status}"

class TarefaPessoal(Tarefa):
    def __init__(self, id, titulo, descricao, prazo, prioridade, categoria_pessoal):
        super().__init__(id, titulo, descricao, prazo, prioridade)
        self.categoria_pessoal = categoria_pessoal

    def __str__(self):
        return super().__str__() + f"\nCategoria Pessoal: {self.categoria_pessoal}"

class TarefaTrabalho(Tarefa):
    def __init__(self, id, titulo, descricao, prazo, prioridade, projeto):
        super().__init__(id, titulo, descricao, prazo, prioridade)
        self.projeto = projeto

    def __str__(self):
        return super().__str__() + f"\nProjeto: {self.projeto}"

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.lista_de_tarefas = []
    
    def adicionar_tarefa(self, tarefa):
        self.lista_de_tarefas.append(tarefa)
    
    def remover_tarefa(self, id):
        tamanho_atual = len(self.lista_de_tarefas)
        self.lista_de_tarefas = [tarefa for tarefa in self.lista_de_tarefas if tarefa.id != id]
        if(len(self.lista_de_tarefas)== tamanho_atual):
            raise Exception("")
    def marcar_tarefa_como_concluida(self, id):
        tarefa = [tarefa for tarefa in self.lista_de_tarefas if tarefa.id == id]
        tarefa[0].marcar_como_concluida()
    

    def listar_tarefas(self):
        if(len(self.lista_de_tarefas) == 0):
            print("\nLista está vazia\n")
            return 
        for tarefa in self.lista_de_tarefas:
            print(tarefa)
            print('-' * 20)

    def __str__(self):
        return f"\nNome: {self.nome} email: {self.email}\n"


class UsuarioRepository:
    lista_de_usuarios = []

    @staticmethod
    def adicionarNaLista(usuario: Usuario):
        UsuarioRepository.lista_de_usuarios.append(usuario)
   
    @staticmethod
    def acessarUsuário(nome = "", email = ""):
      try:
            if(nome != ""):
                return [usuario for usuario in UsuarioRepository.lista_de_usuarios if usuario.nome == nome][0]
            if(email != ""):
                return [usuario for usuario in UsuarioRepository.lista_de_usuarios if usuario.email == email][0]
            raise Exception("")
      except:
          print("\nusuario não encontrado\n")
    
## Apresentação:

class UsuarioFactory:
    @staticmethod
    def criarUsuário():
        nome = input('Digite o nome: ')
        email = input('Digite o email: ')
        usuario = Usuario(nome, email)
        UsuarioRepository.adicionarNaLista(usuario)
        print('Usuário ' + usuario.nome + ' criado')
        return usuario

class TarefaFactory:
    id = 0
    @staticmethod
    def criarTarefaPessoal():
        titulo = input('Digite o titulo: ')
        descricao = input('Digite a descricao: ')
        prazo = input('Digite o prazo: ')
        prioridade = input('Digite a prioridade: ')
        categoria_pessoal = input('Digite a categoria pessoal: ')
        TarefaFactory.id += 1
        return TarefaPessoal(TarefaFactory.id, titulo, descricao, prazo, prioridade, categoria_pessoal)

    @staticmethod
    def criarTarefaTrabalho():
        titulo = input('Digite o titulo: ')
        descricao = input('Digite a descricao: ')
        prazo = input('Digite o prazo: ')
        prioridade = input('Digite a prioridade: ')
        projeto = input('Digite o projeto: ')
        TarefaFactory.id += 1
        return TarefaTrabalho(TarefaFactory.id, titulo, descricao, prazo, prioridade, projeto)

        
class Option:
    def __init__(self, id, titulo, acao):
        self.id = id
        self.titulo = titulo
        self.acao = acao

class Menu:
    def __init__(self, options: list[Option]):
        self.options = options

    def oferecer_opçoes(self):
        texto_de_input = "\nEscolha uma opção:\n"
        for option in self.options:
            texto_de_input += option.titulo + "\n"
        resultado = input(texto_de_input)
        opcao = self.selecionar_opcao(resultado)
        try:
            opcao.acao()
        except: 
            print("\nescolha uma opção válida.\n")
        return opcao
    
    def selecionar_opcao(self, optionId: str):
        try:
            index = int(optionId) - 1
            if(index < len(self.options)):
                return self.options[index]
        except:
            return None


class LoopUtils:
    def __init__(self) -> None:
        self.deveManterOLoop = True

    def setDeveManterOLoop(self,value):
        self.deveManterOLoop = value
    
    def getDeveManterOLoop(self):
        return self.deveManterOLoop

# Demonstração do funcionamento do sistema

if __name__ == "__main__":
    
    while(True):
        def menu_de_usuario(usuario: Usuario):
            loopUtils = LoopUtils()
            def voltar():
                loopUtils.setDeveManterOLoop(False)

            def criarTarefaPessoal():
                tarefa = TarefaFactory.criarTarefaPessoal()
                usuario.adicionar_tarefa(tarefa)
                print("\nTarefa pessoal criada!\n")
            def criarTarefaTrabalho():
                tarefa = TarefaFactory.criarTarefaTrabalho()
                usuario.adicionar_tarefa(tarefa)
                print("\nTarefa de trabalho criada!\n")
            
            def remover_tarefa():
                id = input('Digite o Id da tarefa: ')
                try: 
                    usuario.remover_tarefa(int(id))
                    print("\ntarefa removida\n")
                except:
                    print("\nerro: insira um id válido! \n")
            
            def marcar_tarefa_como_concluida():
                id = input('Digite o Id da tarefa a ser concuida: ')
                try:
                    usuario.marcar_tarefa_como_concluida(int(id))
                    print("\ntarefa concluida\n")

                except:
                    print("\nDigite um id válido\n")

            menu_criar_tarefas = Menu([
                Option(0, "1 - Criar tarefa pessoal", criarTarefaPessoal),
                Option(1, "2 - Criar tarefa de trabalho", criarTarefaTrabalho),
                Option(2, "3 - Voltar ao menu inicial", voltar),
            ])

            menu_usuario = Menu([
                Option(0, "1 - Criar tarefa", menu_criar_tarefas.oferecer_opçoes),
                Option(1, "2 - Listar tarefas", usuario.listar_tarefas),
                Option(2, "3 - Remover tarefa", remover_tarefa),
                Option(3, "4 - Marcar tarefa como concluida", marcar_tarefa_como_concluida),
                Option(4, "5 - Voltar ao menu inicial", voltar),
            ])
            while(loopUtils.getDeveManterOLoop()):
                menu_usuario.oferecer_opçoes()

        def encontrarUsuarioPorNome():
            nome = input('digite o nome: ')
            usuario = UsuarioRepository.acessarUsuário(nome=nome)
            print(usuario)
            menu_de_usuario(usuario=usuario)
        def encontrarUsuarioPorEmail():
            email = input('digite o email: ')
            usuario = UsuarioRepository.acessarUsuário(email=email)
            print(usuario)
            menu_de_usuario(usuario=usuario)

        menu_procurar_usuario = Menu([
            Option(0, "1 - Procurar por nome", encontrarUsuarioPorNome),
            Option(1, "2 - Procurar por email", encontrarUsuarioPorEmail),
        ])

        menu_principal = Menu([
            Option(0, "1 - Cadastrar usuário", UsuarioFactory.criarUsuário), 
            Option(1, "2 - Acessar usuário", menu_procurar_usuario.oferecer_opçoes),
            Option(3, "3 - Sair", quit),
        ])
        
        
        submenu = menu_principal.oferecer_opçoes()