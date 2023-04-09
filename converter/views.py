from django.shortcuts import render
from .forms import SvgFileForm
from .models import SvgFile
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST' and request.FILES.getlist('file'):
        form = SvgFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

        files = request.FILES.getlist('file')
        fs = FileSystemStorage()
        url_files = []
        for file in files:
            filename = fs.save(file.name, file)
            uploaded_file_url = fs.url(filename)
            url_files.append(uploaded_file_url)
        return render(request, 'main/main.html', {
        'form': form,
        'uploaded_file_urls': url_files
    })
    else:
        form = SvgFileForm()

    return render(request, 'main/main.html', {
        'form': form
    })
