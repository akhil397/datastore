from django.shortcuts import render, get_object_or_404, redirect
from .models import CodeModels
from .forms import CodeForm


def details(request):
    code_models = CodeModels.objects.all()
    return render(request, 'detail.html', {'code_models': code_models})

def about(request, pk):
    code_detail = get_object_or_404(CodeModels, id=pk)
    return render(request, 'about.html', {'code_detail': code_detail})

def adddata(request):
    context = {
        'codeform': CodeForm()
    }
    if request.method == 'POST':
        codeformsave = CodeForm(request.POST)
        if codeformsave.is_valid():
            codeformsave.save()
    return render(request, 'add_data.html',context)

# def update_data(request, pk):
#     code = get_object_or_404(CodeModels, id=pk)
#     context = {
#         'codeform': CodeForm(instance=code)
#     }
#     if request.method == 'POST':
#         codeform = CodeForm(request.POST, instance=code)
#         codeform.save()
#         return redirect('details')
#     return render(request, 'update.html', context)
def update_code_model(request, pk):
    code_model = get_object_or_404(CodeModels, id=pk)
    
    if request.method == 'POST':
        form = CodeForm(request.POST, request.FILES, instance=code_model)
        if form.is_valid():
            form.save()
            return redirect('about', pk=code_model.pk)  # Redirect to a detail view or any other view
    else:
        form = CodeForm(instance=code_model)
    
    return render(request, 'update.html', {'form': form})

def delete_data(request, pk):
    code = get_object_or_404(CodeModels, id=pk)
    code.delete()
    return redirect('details')

def search_btn(request):
    if request.method == 'POST':
        searched= request.POST['searched']
        # Filter your model by the search query
        posts = CodeModels.objects.filter(language__contains=searched)
        return render(request, 'search.html',{'searched':searched,'posts':posts})
    else :
        return render(request, 'search.html')

        
