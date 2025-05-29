from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Player
from .forms import PlayerForm
from .MyError import invalid
from .Person import Person,GoalKeeper,FieldPlayer

def insert(request):
    form = PlayerForm()
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            id1 = form.cleaned_data["id1"]
            count = form.cleaned_data["count"]
            player_type = form.cleaned_data["player_type"]
            total_stopping_shots = form.cleaned_data["total_stopping_shots"]
            goal_count = form.cleaned_data["goal_count"]
            if player_type=="GoalKeeper":
               obj1= GoalKeeper(name,id1,count,total_stopping_shots )
               print(obj1)
            else:
                obj2=FieldPlayer(name,id1,count,goal_count)
                print(obj2)
            
            try:
                if Player.objects.filter(id1=id1).exists() or len(str(abs(id1))) < 5:
                    raise invalid("Error: A player with this Player ID already exists or Length not sufficient.")
                return HttpResponseRedirect('display')
            except invalid as e:
                return render(request, "error.html", {"message": e.message})
            form.save()
            return HttpResponse("Successfully inserted Player Details")
    return render(request, "insert.html", {'form': form})

def display(request): 
    players = Player.objects.all()
    display_players = []
    for player in players:
        if player.player_type == "Goalkeeper" and player.count > 0:
            stop_rate = player.total_stopping_shots / player.count
        else:
            stop_rate = 0
       
        display_players.append({
            'player': player,
            'stop_rate': stop_rate,
            'goal_count': player.goal_count
        })

    return render(request, "display.html", {'players': display_players})

def search1(request):
    return render(request, "search1.html")
def search(request):
    player_id = request.GET["id"] # Get the 'id' parameter from URL

    print(f"Searching for player ID: {player_id}")  # Debugging line to check player_id value

    player_id = int(player_id)  # Ensure it's treated as an integer
    print(f"Converted player_id to integer: {player_id}")  # Debugging line
    player = Player.objects.filter(id1=player_id).first()  # Perform the query
    print(f"Found player: {player}")  # Debugging line to check if player is found

    if not player:
        # If no player is found, return your custom error message
        msg = '<h1>No data found with the following requisites</h1>'
        return HttpResponse(msg)  # Send back the message in an HTTP response
    else:
        if player.player_type == "Goalkeeper" and player.count > 0:
            stop_rate = player.total_stopping_shots / player.count
            return render(request, 'display2.html', {'player': player, 'stop_rate': stop_rate})
        else:
            return render(request, 'display2.html', {'player': player})





def bestfield():
    field_players = Player.objects.filter(player_type="FieldPlayer")
    
    if not field_players:
        return None  

    best_fieldplayer = None
    best_goals = 0
    for player in field_players:
        if player.goal_count > best_goals:
            best_goals = player.goal_count
            best_fieldplayer = player

    return best_fieldplayer

def bestgoalkeeper():
    goalkeepers = Player.objects.filter(player_type="Goalkeeper")
    
    if not goalkeepers:
        return None, 0 

    best_goalkeeper = None
    best_stop_rate = 0
    for goalie in goalkeepers:
        if goalie.count > 0:  
            stop_rate = goalie.total_stopping_shots / goalie.count
            if stop_rate > best_stop_rate:
                best_stop_rate = stop_rate
                best_goalkeeper = goalie

    return best_goalkeeper, best_stop_rate  

def bestplayer(request):
    best_goalkeeper, best_stop_rate = bestgoalkeeper()  
    best_fieldplayer = bestfield()  

    return render(request, "display1.html", {
        'goalkeeper': best_goalkeeper,
        'stop_rate': best_stop_rate,
        'fieldplayer': best_fieldplayer
    })

def update(request, t):
    player = Player.objects.filter(id1=t).first()  
    if player:
        if request.method == "POST":
            form = PlayerForm(request.POST, instance=player)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/display')
        else:
            form = PlayerForm(instance=player)
        return render(request, "insert.html", {'form': form})
 
    return HttpResponse('<h1>No player record found with that ID</h1>')

def delete(request,t):
    player=Player.objects.get(id1=t)
    player.delete()
    return HttpResponseRedirect('/display')
    
