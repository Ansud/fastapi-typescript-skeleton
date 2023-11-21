from dash import Dash, html


class Application(Dash):
    def __init__(self):
        super().__init__("Triary")
        self.init_layout()

    def init_layout(self) -> None:
        self.layout = html.Div(
            [
                html.H1(children="Trader diary", style={"textAlign": "center"}),
            ]
        )
