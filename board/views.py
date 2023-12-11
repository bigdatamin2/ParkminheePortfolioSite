from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Board
from .forms import BoardUpdateForm


class BoardUpdateView(generic.UpdateView):
  model = Board
  form_class = BoardUpdateForm
  template_name = 'board/board_update.html'
  success_url = reverse_lazy('board:list')
class BoardDeleteView(generic.DeleteView):
  model = Board
  success_url = reverse_lazy('board:list')
  template_name = 'board/board_delete.html'


def index(request):
  board_list = Board.objects.order_by('-create_date')
  context = {'board_list': board_list}
  return render(request, 'board/board_list.html', context)
def detail(request, board_id):
  board = Board.objects.get(id=board_id)
  context = {'board': board}
  return render(request, 'board/board_detail.html', context)

class BoardCreateView(generic.CreateView):
  model = Board
  fields = ['subject', 'content', 'create_date']
  success_url = reverse_lazy('board:list')
  template_name_suffix = '_create'
