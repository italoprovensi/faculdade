class Tv:
    def __init__(self, estado, canal):
        self.estado = estado
        self.canal = canal


tv1 = Tv("ligada", "4")

print("a tv está ", tv1.estado)
print("no canal ", tv1.canal)
