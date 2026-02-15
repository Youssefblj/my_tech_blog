from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm


# ✅ صفحة التسجيل
class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        # حفظ رسالة النجاح في الـ session
        self.request.session['register_success'] = f'✅ Account successfully created! You can now log in, {user.username}.'
        return redirect('login')

    def form_invalid(self, form):
        from django.contrib import messages
        messages.error(self.request, "⚠️ Please correct the errors below.")
        return self.render_to_response(self.get_context_data(form=form))


# ✅ صفحة تسجيل الدخول
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # نقل الرسالة من الـ session إلى الـ context
        if 'register_success' in self.request.session:
            context['register_success'] = self.request.session.pop('register_success')
        return context
