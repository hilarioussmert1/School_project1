from django.shortcuts import render, get_object_or_404
from .models import Team, Club, News, Statistic
from .utils import binary_search_by_team_name, quick_sort_teams


# View for rendering the home page
def home(request):
    return render(request, 'core/home.html')


# View for rendering the leagues page
def leagues(request):
    return render(request, 'core/leagues.html')


# View for displaying the details of a specific club based on its slug
def club_detail(request, slug):
    # Retrieve the club object or return 404 if not found
    club = get_object_or_404(Club, slug=slug)
    return render(request, 'core/club_detail.html', {'club': club})


# View for displaying all clubs and teams in a dropdown (e.g., selection UI)
def clubs_dropdown(request):
    clubs = Club.objects.all()
    teams = Team.objects.all()  # Optional: used if teams are shown alongside clubs
    return render(request, 'core/clubs.html', {'clubs': clubs, 'teams': teams})


# View for listing all news items, ordered by newest first
def news_list(request):
    news = News.objects.all().order_by('-date')
    return render(request, 'core/news.html', {'news': news})


# View for displaying details of a single news item
def news_detail(request, news_id):
    # Retrieve the news object by ID or return 404 if not found
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'core/news_detail.html', {'news': news_item})


# View for displaying team statistics, with optional search and sorting
def statistics(request):
    # Retrieve all statistics with related team data (optimized with select_related)
    stats = list(Statistic.objects.select_related('team').all())

    # Read search and sort query parameters from the request
    search_query = request.GET.get('search', '').strip()
    sort_order = request.GET.get('sort', 'desc')

    # Search for a specific team by name using binary search (exact match)
    if search_query:
        # Sort alphabetically for binary search (case-insensitive)
        stats.sort(key=lambda s: str(s.team).lower() if s.team else '')
        result = binary_search_by_team_name(stats, search_query)
        stats = [result] if result else []

    # ⚡ Sort teams by their calculated points using quick sort
    reverse = (sort_order == 'desc')  # Default is descending order
    sorted_stats = quick_sort_teams(stats, reverse=reverse)

    # Render the statistics page with sorted and filtered data
    return render(request, 'core/statistics.html', {
        'teams': sorted_stats,
        'search_query': search_query,
        'sort_order': sort_order,
    })
# def games(request):
#     return render(request, 'core/games.html')
#
# def video(request):
#     return render(request, 'core/video.html')
#
# def schedule(request):
#     return render(request, 'core/schedule.html')
#
