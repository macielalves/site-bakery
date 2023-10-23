# class Teste:
#     def teste_filho(self):
#         print("Olá mundo!")
#     pass
#
#
# ob = Teste
# a = var_ = ob().teste_filho
#

from ast import match_case


def hello(__f):
    print("Oi")
    return __f()


class Bot:
    def __init__(self, f):
        self.f = f

    def get(self):
        pass

    def print_nome(self, nome):
        print(self.f, nome)

@hello
def oi():
    return "_Oi"


bot = Bot


@bot
class Kame:
    pass


kame = Kame
print(kame.print_nome('Kame'))

def overload(func):
    f = getattr(func, "__func__", func)
    print(f)
    


@overload
def printe(*values, sep: str | None = " ", end: str | None = "\n"):
    """_summary_

    Args:
        sep (str | None, optional): _description_. Defaults to " ".
        end (str | None, optional): _description_. Defaults to "\n".
    """
    pass

