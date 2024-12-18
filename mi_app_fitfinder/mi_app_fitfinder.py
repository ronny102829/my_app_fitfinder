import reflex as rx
from .screens.autentication_screen import autentication
from .screens.camera_screen import camera
from .screens.details_screen import details
from .screens.options_screen import options
from .screens.splash_screen import splash
from .screens.umboarding_screen import umboarding
from rxconfig import config

def index() -> rx.Component:
    return rx.mobile_and_tablet(
        splash()
    )
app = rx.App()
app.add_page(index)
