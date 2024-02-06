""" Flet With Firebase """

# If we already have an account with the necessary data, hey can skip this step, otherwise we need to create a
# project on firebase first.

# Modules
import pyrebase
import flet
from flet import *
import datetime
from functools import partial

# url firebase:https://console.firebase.google.com/?pli=1
config = {
    "apiKey": "AIzaSyDqTc5UfkFe-wXTimq86H-0gxmPAv_Bwkk",
    "authDomain": "flet-firebase2.firebaseapp.com",
    "projectId": "flet-firebase2",
    "storageBucket": "flet-firebase2.appspot.com",
    "messagingSenderId": "389449586296",
    "appId": "1:389449586296:web:fd58986997eb656a88ff8d",
    "databaseURL": "",
}

# Initialize firebase
firebase = pyrebase.initialize_app(config)

# Set up authentication manager
auth = firebase.auth()


# UI class
class UserWidget(UserControl):
    def __init__(
            self,
            title: str,
            sub_title: str,
            btn_name: str,
            func
    ):
        self.title = title
        self.sub_title = sub_title
        self.btn_name = btn_name
        self.func = func
        super().__init__()

    def InputTextField(self, text: str, hide:bool):
        return Container(
            alignment=alignment.center,
            content=TextField(
                height=48,
                width=255,
                bgcolor="#f0f3f6",
                text_size=12,
                color="black",
                border_color="transparent",
                hint_text=text,
                filled=True,
                cursor_color="black",
                hint_style=TextStyle(
                    size=11,
                    color="black",

                ),
                password=hide,
            ),
        )

    def SignInOption(self, path: str, name: str):
        return Container(
            content=ElevatedButton(
                content=Row(
                    alignment='center',
                    spacing=4,
                    controls=[
                        Image(
                            src=path,
                            width=30,
                            height=30,
                        ),
                        Text(
                            name,
                            color='black',
                            size=10,
                            weight="bold",
                        ),
                    ],
                ),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder
                        (radius=8),
                    },
                    bgcolor={
                        "": "#f0f3f6",
                    },
                ),
            ),
        )


    def build(self):
        # this UI will allow us to create a signin.

        self._title = Container(
            alignment=alignment.center,
            content=Text(
                self.title,
                size=15,
                text_align="center",
                weight="bold",
                color="black",
            ),
        )

        self._sub_title = Container(
            alignment=alignment.center,
            content=Text(
                self.sub_title,
                size=10,
                text_align="center",
                color="black",
            ),
        )

        self._sign_in =Container(
            content=ElevatedButton(
                on_click=partial(self.func),
                content=Text(
                    self.btn_name,
                    size=11,
                    weight="bold",

                ),
                style=ButtonStyle(
                    shape={
                        "": RoundedRectangleBorder
                        (radius=8),
                    },
                    color={
                        "": "black",
                    },
                ),
                height=48,
                width=255,
            )
        )

        return Column(
            horizontal_alignment="center",
            controls=[
                Container(padding=10),
                self._title,

                self._sub_title,

                Column(
                    spacing=12,
                    controls=[
                        self.InputTextField("Email",
                                            False),
                        self.InputTextField("Password",
                                            True),
                    ],
                ),
                Container(padding=5),
                self._sign_in,
                Container(padding=5),
                Column(
                    horizontal_alignment="center",
                    controls=[
                        Container(
                            content=Text(
                                "Or continue with",
                                size=10,
                                color="black",
                            )
                        ),
                        self.SignInOption("./assets/"
                                          "facebook.pgn", "Facebook"),
                        self.SignInOption("./assets/"
                                          "google.pgn", "Google"),
                    ],
                ),
            ],
        )


def main(page: Page):
    page.title = "Flet With Firebase"
    page.bgcolor = "#f0f3f6"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def _main_column_():
        return Container(
            width=280,
            height=600,
            bgcolor="#ffffff",
            padding=12,
            border_radius=35,
            content=Column(
                spacing=20,
                horizontal_alignment="center",
            ),
        )

    def _register_user(e):
        try:
            auth.create_user_with_email_and_password(
                _register_.controls[0].controls[3].controls
                [0].content.value,
                _register_.controls[0].controls[3].controls
                [1].content.value
            )
            print("Registration ok!")
        except Exception as e:
            print(e)
    # create sign-in validation
    def _sign_in(e):
        try:
            user = auth.sign_in_with_email_and_password(
                _sign_in.controls[0].controls[3].controls
                [0].content.value,
                _sign_in.controls[0].controls[3].controls
                [1].content.value,
            )

            info = auth.get_account_info(user["idToken"])

            #print(info)

            data = ["createedAt", "lastLoginAt",]

            for key in info:
                if key == 'users':
                    for item in data:
                        print(
                            item
                            + " "
                            +datetime.datetime.fromtimestamp(
                                int(info[key][0][item]) /1000
                            ).strftime("%D - %H:%M %p")

                        )

            _sign_in.controls[0].controls[3].controls[0].content.value = None
            _sign_in.controls[0].controls[3].controls[1].content.value = None
            _sign_in.controls[0].controls[3].update()


        except:
            print("Wrong email or password!")


    # call the class twice ,one for sign in the other for registration

    _sign_in_ = UserWidget(
        "Welcome Back!",
        "Enter your account details below.",
        "Sign In ",
        _sign_in,
    )

    _register_ = UserWidget(
        "Registration",
        "Register your email and password below.",
        "Register ",
        _register_user,

    )
    _sign_in_main = _main_column_()
    _sign_in_main.content.controls.append(Container(padding=15))
    _sign_in_main.content.controls.append(_sign_in_)

    _reg_main = _main_column_()
    _reg_main.content.controls.append(Container(padding=15))
    _reg_main.content.controls.append(_register_)

    page.add(
        Row(
            alignment='center',
            controls=[
                _sign_in_main,
                _reg_main,

            ],

        )
    )


if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")
