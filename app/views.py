from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Game, Review, Genre
from .forms import ReviewForm

def mainpage(request):
    games = Game.objects.all()
    reviews = Review.objects.order_by('-created_at')[:5]
    return render(request, 'reviews/mainpage.html', {'games': games, 'reviews':reviews})

def game_list(request):
    games = Game.objects.all()

    title = request.GET.get("title")
    genre_id = request.GET.get("genres")
    year = request.GET.get("year")

    if title:
        games = games.filter(title__icontains=title)

    if genre_id:
        games = games.filter(genres__id=genre_id)

    if year:
        games = games.filter(release_year=year)

    context = {
        "games": games,
        "genres": Genre.objects.all(),
    }

    return render(request, "games/game_list.html", context)

def game_detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    reviews = Review.objects.filter(game=game)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.game = game
            review.author = request.user
            review.save()
            return redirect('game_detail', game_id=game.id)
    else:
        form = ReviewForm()
    
    return render(request, 'games/game_detail.html', {'game': game, 'reviews': reviews, 'form': form})

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, "reviews/review_detail.html", {"review": review})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'reviews/register.html', {'form': form})
