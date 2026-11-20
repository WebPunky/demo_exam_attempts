from django.contrib.auth.forms import UserCreationForm

from .models import User

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email", "phone")

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for name in ("username", "first_name", "last_name", "email", "phone"):
            self.fields[name].required = True