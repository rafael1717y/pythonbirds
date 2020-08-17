class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p)) ## Forma nao usual ==>  chamou a classe passou o metodo/funcao da classe e o objeto p
    print(id(p))
    print(p.cumprimentar())
