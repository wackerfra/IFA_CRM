from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Operator
from .forms import OperatorForm


@login_required
def operator_list(request):
    operators = Operator.objects.all()
    return render(request, 'operators/operator_list.html', {'operators': operators})

@login_required
def operator_detail(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    return render(request, 'operators/operator_detail.html', {'operator': operator})
@login_required
def operator_create(request):
    if request.method == 'POST':
        form = OperatorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('operator_list')
    else:
        form = OperatorForm()
    return render(request, 'operators/operator_form.html', {'form': form})

@login_required
def operator_update(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    if request.method == 'POST':
        form = OperatorForm(request.POST, instance=operator)
        if form.is_valid():
            form.save()
            return redirect('operator_list')
    else:
        form = OperatorForm(instance=operator)
    return render(request, 'operators/operator_form.html', {'form': form})

@login_required
def operator_delete(request, pk):
    operator = get_object_or_404(Operator, pk=pk)
    if request.method == 'POST':
        operator.delete()
        return redirect('operator_list')
    return render(request, 'operators/operator_confirm_delete.html', {'operator': operator})

@login_required
def operator_history(request, operator_id):
    # Get the specific operator
    operator = Operator.objects.get(id=operator_id)

    # Get all hotel interests connected to the operator
    interests = operator.operatorinterest_set.select_related('hotel')

    return render(
        request,
        'operators/operator_history.html',  # Create this template
        {'operator': operator, 'interests': interests}
    )