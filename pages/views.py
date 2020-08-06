from django.shortcuts import render
from django.views.generic import View
from pages.forms import FeedbackForm
from django.core.mail import BadHeaderError, mail_admins, send_mail
from django.shortcuts import redirect
from pages.models import Feedback
from django.contrib import messages


class AboutUsView(View):
    def get(self, *args, **kwargs):
        return render(self.request, template_name="pages/about_us.html")


class ContactUsView(View):
    def get(self, *args, **kwargs):
        form = FeedbackForm()
        context = {
            'form': form
        }
        return render(self.request, template_name="pages/contact_us.html", context=context)

    def post(self, *args, **kwargs):
        form = FeedbackForm(self.request.POST)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            phone = form.cleaned_data.get("phone")
            message = form.cleaned_data.get("message")
            
            feedback = Feedback.objects.create(
                name=name,
                email=email,
                telephone=phone,
                message=message,
            )
            header = f"You have a feedback from {name} {email}"
            mail_admins(header, message)

            customer_subject = "Thank You For Contacting Us"
            customer_message = f"Dear {name}, \n\n Thank you so much for contacting us. We have recieved Your Email. Our Agents will take an action as soon as possible. \n\n\n Thank You, \n VishMedi Care "
            try:
                send_mail(
                    customer_subject,
                    customer_message,
                    "vishmedicare@gmail.com",
                    [email],
                    fail_silently=True
                )
            except BadHeaderError:
                return redirect('pages:feedback')
            messages.success(self.request, "Your Message has been recieved")
            print(name, email, phone, message)
        return redirect("pages:contact-us")