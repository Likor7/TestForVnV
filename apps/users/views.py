from django.shortcuts import HttpResponseRedirect, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.models import User

from .models import ExtendedGroup
from .forms import UserForm, ExtendedGroupForm


class UserListView(ListView):
    model = User
    template_name = "users/user_list.html"
    context_object_name = "users"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_list"] = True
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user_list")

    def dispatch(self, request, *args, **kwargs):
        if not ExtendedGroup.objects.exists():
            messages.error(
                self.request, "Не можна cтворити користувача, якщо нема групи."
            )
            return redirect("group_create")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_obj"] = False
        return context


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "users/user_form.html"
    success_url = reverse_lazy("user_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_group = self.object.groups.first()
        context["user_obj"] = user_group
        return context


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy("user_list")
    template_name = "users/confirm_delete.html"

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)


class GroupListView(ListView):
    model = ExtendedGroup
    template_name = "users/group_list.html"
    context_object_name = "groups"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["group_list"] = True
        return context


class GroupCreateView(CreateView):
    model = ExtendedGroup
    form_class = ExtendedGroupForm
    template_name = "users/group_form.html"
    success_url = reverse_lazy("group_list")


class GroupUpdateView(UpdateView):
    model = ExtendedGroup
    form_class = ExtendedGroupForm
    template_name = "users/group_form.html"
    success_url = reverse_lazy("group_list")


class GroupDeleteView(DeleteView):
    model = ExtendedGroup
    success_url = reverse_lazy("group_list")
    template_name = "users/confirm_delete.html"

    def form_valid(self, form):
        group = self.get_object()
        if group.user_set.all().exists():
            messages.error(
                self.request,
                "Не можна видалити групу, якщо до неї призначені користувачі.",
            )
            return HttpResponseRedirect(self.get_success_url())
        return super().form_valid(form)
