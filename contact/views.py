from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage,send_mail
# Create your views here.
# Vista que se encarga del formulario de /contact, esto será a travéz del metodo POST (el cual no muestra datos recaudados
# en el url, de forma que los pasa "escondidos") ademas dentro del try: se hace el envio del formulario atravez 
# del metodo send_mail el cual esta importado arriba

def contact(request):
    contact_form = ContactForm() #CREA PANTILLA POST
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST) #SI SE RELLENA UN FORMULARIO CON EL METHO POST LO MANDARÁ
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            content = request.POST.get('content','')
            #enviamos y redireccionamos
            try:
                email_submit = send_mail (
                    "Neutron Web : Nuevo mensaje de {}".format(name),
                    "De: {} <{}>\n\nMensaje:\n\n{}".format(name,email,content),
                    email,
                    ["leo.kpex@gmail.com"],
                )
                return redirect(reverse('contact')+'?ok')    
            except Exception as e: 
                #fallo, algo no fue bien
                return redirect(reverse('contact')+'?fail')

    return render(request,"contact/contacto.html",{'form':contact_form})