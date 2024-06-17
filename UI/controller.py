import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.s=""
        self.min=0
        self.Max=0

    def handle_graph(self, e):
        self._model.creaGrafo()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente,con {self._model.getNumNodes()} nodi e {self._model.getNumEdges()} archi."))
        min,MAX=self._model.MinMaxValues()
        self.min=min
        self.MAX=MAX
        self._view.txt_result.controls.append(ft.Text(f"Valore minimo:{min}, valore massimo:{MAX}."))
        self._view.update_page()
        pass

    def handle_countedges(self, e):
        self._view.txt_result2.controls.clear()

        self.s=self._view.txt_name.value
        if self.s=="" or self._model.getNumNodes()==0:
            self._view.create_alert("Prima crea il grafo e inserisci una soglia")
            self._view.update_page()
            return
        try:
            self.s=float(self.s)
            if self.s <self.min or self.s>self.MAX:
                self._view.create_alert("La soglia deve almeno essere tra massimo e minimo")
                self._view.update_page()
                return
            sotto,sopra=self._model.countEdges(self.s)
            self._view.txt_result2.controls.append(ft.Text(
                f"Numero di archi con valore inferiore alla soglia:{sotto}, superiore:{sopra}"))


        except ValueError:
            self._view.create_alert("Prima crea il grafo e inserisci una soglia")
            self._view.update_page()
            return
        self._view.update_page()
    def handle_search(self, e):
        if self.s=="":
           self._view.create_alert("Prima creare il grafo e selezionare una soglia valida")
           self._view.update_page()
           return
        self._model.getBP(self.s)
        self._view.txt_result3.controls.append(ft.Text(f"Peso massimo con archi con valore > soglia: {self._model.pesoMax}"))
        tt=self._model.tuplePrint()
        for x in tt:
            self._view.txt_result3.controls.append(ft.Text(f"{x[0].chromosome}--->{x[1].chromosome}: {x[2]}"))
        self._view.update_page()
