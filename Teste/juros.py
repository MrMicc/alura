class Juros():

    def __init__(self, capital=None, taxa=None, n_periodo=None ):
        self.__capital = capital
        self.__taxa = taxa
        self.__n_periodo = n_periodo

    @property
    def capital(self):
        return self.__capital

    @property
    def taxa(self):
        return self.__taxa

    @property
    def n_periodo(self):
        return self.__n_periodo

    def set_capital(self, capital):
        self.__capital = capital

    def set_taxa(self, taxa):
        self.__taxa = taxa

    def set_n_periodo(self, n_periodo):
        self.__n_periodo = n_periodo

    def simples(self):
        total_juros = (self.capital * self.taxa) * self.n_periodo
        return total_juros