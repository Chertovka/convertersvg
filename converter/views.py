from django.shortcuts import render
from .forms import SvgFileForm
from .models import SvgFile
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        form = SvgFileForm(request.POST, request.FILES)

        if form.is_valid():
            files = request.FILES.getlist('file')

            url_files = []

            for file in files:
                newFile = SvgFile(file=file)
                newFile.save()
                url_files.append(file)

            return render(
                None,
            'main/upload.html',
                {
            'form': form,
                'uploaded_file_urls': url_files,
                },
    )
    else:
        form = SvgFileForm()

    return render(
        request,
        'main/index.html',
        {
            'form': form
            },
    )

def upload_file(request):
    print('--->', request.FILES.getlist('file'))

    if request.method == 'POST' and request.FILES.getlist('file'):
        files = request.FILES.getlist('file')
        url_files = []

        for file in files:
            url_files.append(file)

        return render(request, 'main/upload.html', {
        'uploaded_file_urls': url_files
    })

    return render(request, 'main/upload.html')