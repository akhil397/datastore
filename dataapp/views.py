from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q
from .models import CodeModels, Language, Types
from .forms import CodeForm

def details(request):#this for listing
    code_models = CodeModels.objects.all()
    return render(request, 'detail.html', {'code_models': code_models})

def about(request, pk):#this for detailing
    code_detail = get_object_or_404(CodeModels, id=pk)
    return render(request, 'about.html', {'code_detail': code_detail})

def adddata(request):
    all_lang = Language.objects.all()
    types_code = Types.objects.all()
    context = {
        'all_langs': all_lang,
        'type_codes': types_code,
        'codeform': CodeForm(),
    }
    
    if request.method == 'POST':
        codeformsave = CodeForm(request.POST, request.FILES)
        if codeformsave.is_valid():
            codeformsave.save()
            return redirect('details')  # Redirect to the 'details' view after saving

    return render(request, 'add_data.html', context)

def update_code_model(request, pk):
    code_model = get_object_or_404(CodeModels, id=pk)
    all_lang = Language.objects.all()
    types_code = Types.objects.all()
    
    if request.method == 'POST':
        form = CodeForm(request.POST, request.FILES, instance=code_model)
        context = {
            'all_langs': all_lang,
            'type_codes': types_code,
            'form': form
        }
        if form.is_valid():
            form.save()
            messages.success(request, 'Code model updated successfully!')
            return redirect('about', pk=code_model.pk)
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = CodeForm(instance=code_model)
        context = {
            'all_langs': all_lang,
            'type_codes': types_code,
            'form': form
        }
    return render(request, 'update.html', context)
def delete_data(request, pk):
    code = get_object_or_404(CodeModels, id=pk)
    code.delete()
    return redirect('details')


def search_btn(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        if searched:
            posts = CodeModels.objects.filter(
                Q(title__icontains=searched) |
                Q(code_lang__name__icontains=searched) |  # Assuming code_lang is a ForeignKey
                Q(codes__icontains=searched) |
                Q(type_code__name__icontains=searched)  # Assuming type_code is a ForeignKey
            )
            if posts.exists():
                messages.success(request, f'Results for "{searched}" found.')
            else:
                messages.error(request, f'No results found for "{searched}".')
            return render(request, 'search.html', {'searched': searched, 'posts': posts})
        else:
            messages.error(request, 'Please enter a search term.')
            return render(request, 'search.html')
    else:
        return render(request, 'search.html')

        
