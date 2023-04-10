from django.shortcuts import render
from .forms import SvgFileForm
from .models import SvgFile
from .toSvgConv import toSVGConv

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
                'uploaded_file_urls': toSVGConv(url_files, 'media'),
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