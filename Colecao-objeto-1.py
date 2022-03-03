class Anomed:
    nome = ""


class Flor(Anomed):
    pass


class Cidade(Anomed):
    pass


class Estrela(Anomed):
    pass


rose = Flor()
rose.nome = "Rose"

rome = Cidade()
rome.nome = "Rome"

sirius = Estrela()
sirius.nome = "Sirius"

rows = [rose, rome, sirius]
nomes = ", ".join([r.nome for r in rows])

# nomes is "Rose, Rome, Sirius"
# tente compilador Python
