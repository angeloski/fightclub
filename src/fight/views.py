from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

import tweepy
import json

from .forms import SearchForm
from common.util import validate_name
from .models import User
from .models import Fight

consumer_key = '3QgqCacIZt5BvtjHpN5yqCzEF'
consumer_secret = 'tXsRkwnoQH2totF4MFXDDUso0LbaiqHlOMKv4JoCl1cUYNq2uW'

access_token = '50341384-Te71ZAm42LyXGoxhaYKkgWUpztV9kYwAvWP7I3APy'
access_token_secret = 'qJUWf65lwJJDPQy3xZvXPTHZB7Z53xES1y2MXyJQgd7H1'

def home(request):
    # TODO: make POST-Redirect-GET here to make the URL bookmarkable
    # TODO: use Django's Regex validator
    form = SearchForm()

    template = 'home.html'
    context = {'searchForm': form}
    context.update({'error_message_show':False})
    context.update({'initial_load':True})

    if request.method == 'POST':

        form = SearchForm(request.POST)

        context.update({'error_message_show':False})
        context.update({'initial_load':False})

        oponent1 = request.POST.get('oponent1')
        oponent2 = request.POST.get('oponent2')

        try:
            # Check if the names are valid
            validate_name(r'^@([A-Za-z0-9_]+)$', oponent1)
            validate_name(r'^@([A-Za-z0-9_]+)$', oponent2)
        except ValidationError:
            # Return and print error message if the names are not valid
            print('Please enter valid Twitter names.')
            context.update({'error_message':'Please enter valid Twitter names.'})
            context.update({'error_message_show':True})
            return render(request, template, context)
        else:
            try:
                # Check if the given user names exist
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)

                api = tweepy.API(auth)

                user1 = api.get_user(oponent1)
                user2 = api.get_user(oponent2)
            except tweepy.TweepError:
                # Return message if at least one of the users does not exist
                context.update({'error_message':'At least one of the Twitter users does not exist. Please enter existing users.'})
                context.update({'error_message_show':True})
                return render(request, template, context)
            else:
                # Both users exist, so compare their parameters
                if user1.followers_count > user2.followers_count:
                    result_message = str(oponent1) + ' is the winner! ' + str(user1.followers_count) + ' vs ' + str(user2.followers_count)
                else:
                    result_message = str(oponent2) + ' is the winner! ' + str(user1.followers_count) + ' vs ' + str(user2.followers_count)
                
                context.update({'user1':user1})
                context.update({'user2':user2})
                context.update({'result_message':result_message})

                chart_data = [
                              {
                                'key': "Followers",
                                'color': "#51A351",
                                'values':
                                  [      
                                    { 'x' : str(oponent1), 'y' : user1.followers_count },
                                    { 'x' : str(oponent2), 'y' : user2.followers_count }   
                                  ]
                              },
                              {
                                'key': "Following",
                                'color': "#BD362F",
                                'values':
                                  [      
                                    { 'x' : str(oponent1), 'y' : user1.friends_count },
                                    { 'x' : str(oponent2), 'y' : user2.friends_count }
                                  ]
                              }
                            ]

                chart_data = json.dumps(chart_data)
                context.update({'chart_data':chart_data})

                return render(request, template, context)
                # # Save fight to database
                # if form.is_valid():

                #     # Check if user has already been entered in the DB. If not, add it
                #     save_it = form.save(commit=False)
                #     save_it.save()

                #     oponent1 = form.cleaned_data['oponent1']
                #     oponent2 = form.cleaned_data['oponent2']

                #     user1 = User()
                #     user2 = User()

                #     user1.save()

                #     fight_instance = Fight()
                #     fight.save()

                    # Add the current fight
        
    else:
        pass


    return render(request, template, context)
