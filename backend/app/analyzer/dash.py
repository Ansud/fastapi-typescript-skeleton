from core.settings import settings
from dash import Dash, html


class Application(Dash):
    def __init__(self):
        super().__init__("Triary", requests_pathname_prefix=f"{settings.DASH_PREFIX}/")
        self.init_layout()

    def init_layout(self) -> None:
        self.layout = html.Div(
            [
                html.H1(children="Trader analysys", style={"textAlign": "center"}),
            ]
        )


app = Application()
