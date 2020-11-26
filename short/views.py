from django.shortcuts import render, redirect
from django.urls import reverse, exceptions
from secrets import token_urlsafe
from .forms import LinkForm
from .models import Linker
from linkshortener.settings import STATICFILES_DIRS
import qrcode

def main(request):
    
    error = None

    if request.method == 'POST':

        link = request.POST.get('link')
        link_hash = request.POST.get('link_hash') if request.POST.get('link_hash') else token_urlsafe(8)

        try:
            Linker.objects.get(link_hash=link_hash)
        except Linker.DoesNotExist:
            form = LinkForm(data={'link': link, 'link_hash': link_hash})
            if form.is_valid():
                Linker(link=form.cleaned_data['link'], link_hash=form.cleaned_data['link_hash']).save()
                return redirect('link/'+link_hash)
        else:
            error = 'Not unique short link'

    form = LinkForm()

    context = {'form': form, 'error': error}

    return render(request, 'short/main.html', context)


def link(request, link):
    qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

    link = f'http://{request.get_host()}/{link}'

    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(STATICFILES_DIRS[0] + '/temp.png')

    return render(request, 'short/link.html', {'link': link, 'qr': qr})


def redirector(request, link_hash):
    
    if not link_hash:
        return redirect('/')
    
    try:
        linker = Linker.objects.get(link_hash=link_hash)
    except Linker.DoesNotExist:
        linker = None

    if linker:
        linker.visits += 1
        linker.save()
        try:
            return redirect(linker.link)
        except exceptions.NoReverseMatch:
            return redirect('http://' + linker.link) 
    else:
        return redirect('/')