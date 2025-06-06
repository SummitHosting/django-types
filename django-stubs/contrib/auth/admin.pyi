from collections.abc import Callable
from typing import Any, TypeVar

from django.contrib import admin
from django.http.request import HttpRequest
from django.http.response import HttpResponse

_F = TypeVar("_F", bound=Callable[..., Any])

def csrf_protect_m(func: _F) -> _F: ...
def sensitive_post_parameters_m(func: _F) -> _F: ...

class GroupAdmin(admin.ModelAdmin[Any]): ...

class UserAdmin(admin.ModelAdmin[Any]):
    change_user_password_template: Any = ...
    add_fieldsets: Any = ...
    add_form: Any = ...
    change_password_form: Any = ...
    def user_change_password(
        self, request: HttpRequest, id: str, form_url: str = ...
    ) -> HttpResponse: ...
