from django.contrib.auth import get_user_model, login
from django.shortcuts import redirect, reverse
from django.views.generic import CreateView
from .forms import MyUserCreationForm


User=get_user_model()

class RegisterView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'account/register.html'
    model = User

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('todo:projects')
        return next_url