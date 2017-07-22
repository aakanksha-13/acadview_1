import  requests, urllib
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import matplotlib.pyplot as plt

#Token Owner : aakankshat01
#Sandbox Users : _amethyst00,anisha_lamichhane,bhavana.singh.10,legendwait4itdary

ACCESS_TOKEN='5729772464.38e704c.08c4dd98fe6644f0957b911ef4fe88f8'

BASE_URL='https://api.instagram.com/v1/'

'''
Function declaration to get own info
'''


def self_info():
    url=BASE_URL + "users/self/?access_token=%s"%ACCESS_TOKEN
    r=requests.get(url).json()

    if r['meta']['code'] == 200:

            if len(r['data']):
                print 'Username: %s' % (r['data']['username'])
                print 'No. of followers: %s' % (r['data']['counts']['followed_by'])
                print 'No. of people you are following: %s' % (r['data']['counts']['follows'])
                print 'No. of posts: %s' % (r['data']['counts']['media'])
            else:
                print 'User donot exist!'
    else:
            print 'Status code other than 200 received!'



'''
Function declaration to get the ID of a user by username
'''

def get_user_id(insta_username):
    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') % (insta_username, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)

    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()


'''
Function declaration to get the user info by username
'''
def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print 'Username: %s' % (user_info['data']['username'])
            print 'No. of followers: %s' % (user_info['data']['counts']['followed_by'])
            print 'No. of people you are following: %s' % (user_info['data']['counts']['follows'])
            print 'No. of posts: %s' % (user_info['data']['counts']['media'])
        else:
            print 'There is no data for this user!'
    else:
        print 'Status code other than 200 received!'

'''
Function declaration to get your recent post
'''

def get_own_post():
    request_url=(BASE_URL + 'users/self/media/recent/?access_token=%s') %(ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    own_media = requests.get(request_url).json()
    if own_media['meta']['code']==200:
        if len(own_media['data']):
            image_name=own_media['data'][0]['id'] + '.jpeg'
            image_url=own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print 'Your image has been downloaded!!!!'
        else:
            print 'Post does not exists!!'
    else:
        print 'Status code other than 200 received!'

'''
Function declaration to get user  recent post by username
'''
def get_user_post(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print 'User doesnot exist!!'
        exit()
    request_url=(BASE_URL + 'users/%s/media/recent/?access_token=%s') %(user_id,ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media=requests.get(request_url).json()
    if user_media['meta']['code']==200:
        if len(user_media['data']):
            image_name=user_media['data'][0]['id'] + '.jpeg'
            image_url=user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url,image_name)
            print 'Your image has been downloaded!!!!'
        else:
            print 'Post does not exists!!'
    else:
        print 'Status code other than 200 received!'


'''
Function declaration to get the ID of the recent post of a user by username
'''

def get_post_id(insta_username):
    user_id=get_user_id(insta_username)
    if user_id==None:
        print 'User doesnot exist!!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print 'There is no recent post!!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()

'''
Function declaration to like the recent post of a user
'''

def like_a_post(insta_username):
    media_id=get_post_id(insta_username)
    request_url=(BASE_URL + 'media/%s/likes') %(media_id)
    payload ={"access_token": ACCESS_TOKEN}
    print 'POST request url : %s' %(request_url)
    post_like =requests.post(request_url,payload).json()
    if post_like['meta']['code']==200:
        print 'Post liked!!!'
    else:
        print 'Unable to like post!!!'


'''
Function declaration to comment on the recent post of a user
'''
def post_comment(insta_username):
    media_id=get_post_id(insta_username)
    comment_msg = raw_input('Enter comment:')
    payload = {"access_token": ACCESS_TOKEN ,"text": comment_msg }
    request_url = (BASE_URL + 'media/%s/comments') % (media_id)
    print 'POST request url : %s' % (request_url)

    post_comment = requests.post(request_url, payload).json()

    if post_comment['meta']['code'] == 200:
        print 'Comment posted successfully!!'
    else:
        print 'Status code other than 200 received!'
        exit()


'''
Function declaration to get the list of user the  like the recent post of a user
'''

def no_of_user_likes(insta_username):
    media_id =get_post_id(insta_username)
    request_url =(BASE_URL + 'media/%s/likes?access_token=%s') %(media_id,ACCESS_TOKEN)
    print 'GET request url : %s' %(request_url)

    user_like =requests.get(request_url).json()

    if user_like['meta']['code']==200:
        if user_like['data']:
            print "Following users likes recent post :"
            for x in range(0,len(user_like['data'])):
                print  user_like['data'][x]['username']
        else:
            print 'No likes on post!!'
    else:
        print 'Status code other than 200 received!'
        exit()

'''
Function declaration to get the ID of  recent post like by  user own
'''
def recent_like_by_user(insta_username):
   # user_id=get_user_id(insta_username)
    request_url=(BASE_URL +'users/self/media/liked?access_token=%s') %(ACCESS_TOKEN)
    recent_like=requests.get(request_url).json()

    if recent_like['meta']['code']==200:
        if recent_like['data']:
            print ('ID of liked reccent media=%s')%(recent_like['data'][0]['id'])
        else:
            print 'No media recent liked'
    else:
        print 'Status code other than 200 received!'
        exit()


'''
Function declaration to search post with minimum like
'''
def post_with_min_like(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            min = user_media['data'][0]['likes']['count']
            for i in range(len(user_media['data'])):
                if min > user_media['data'][i]['likes']['count']:
                    min = user_media['data'][i]['likes']['count']
                    pos= i
            print "Likes on post : %d"  %user_media['data'][pos]['likes']['count']
            print "Image URL :" + user_media['data'][pos]['images']['standard_resolution']['url']
            print "Post ID : " + user_media['data'][pos]['id'] + "\n"
        else:
            print 'There is no post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()


'''
Function declaration to search post with a particular caption input by user
'''
def get_post_by_caption(word,insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    flag = False
    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            for i in range(len(user_media['data'])):
                caption_text = user_media['data'][i]['caption']['text']
                if word in caption_text:
                    print "Caption on the post : " + user_media['data'][i]['caption']['text']
                    print "Image URL :" + user_media['data'][i]['images']['standard_resolution']['url']
                    print "Post ID : " + user_media['data'][i]['id'] +"\n"
                    flag = True
            if(flag == False):
                print "No caption related post found"
        else:
            print 'There is no required post of the user!'
            exit()
    else:
        print 'Status code other than 200 received!'
        exit()


'''
Function declaration to choose post in creative way!!!
1- WITH MINIMUM NUMBER LIKES
2- CAPTION WITH A PARTICULAR TEXT
'''
def try_creative_ways(insta_username):
    print "Choose a way for getting a post of a user:"
    print "1- with minimum number likes"
    print "2-whose caption has a particular text"
    print "3- exit"
    while True:
        choice= raw_input("Enter your choice:")
        choice=int(choice)
        if choice==1:
            post_with_min_like(insta_username)
        elif choice == 2:
            word = raw_input("Enter a particular text to be searched in caption")
            get_post_by_caption(word,insta_username)
        elif choice == 3:
            break
        else:
            print "Invalid Choice"


'''
Function declaration to list comments on recent post of user
'''
def list_of_comment(insta_username):
    media_id=get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments?access_token=%s') % (media_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)

    list_of_comment = requests.get(request_url).json()

    if list_of_comment['meta']['code'] == 200:
        if list_of_comment['data']:
            print 'List of comments:%s'

            for i in range(0, len(list_of_comment['data'])):

                print  (list_of_comment['data'][i]['text'])
        else:
            print 'No comments on post!!'
    else:
        print 'Status code other than 200 received!'
        exit()


'''
Function declaration to delete negative comment from post(not slang words /Incomplete words)
'''
def delete_negative_comment(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's a naive implementation of how to delete the negative comments :)
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (media_id, comment_id, ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    print 'Positive comment : %s\n' % (comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'

'''
Function declaration to plot piechart of positive and negative comments
'''
def plot_piechart(insta_username):
    media_id = get_post_id(insta_username)
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Here's  implementation of how to delete the negative comments
             for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    neg=p_neg;
                else
                    pos=p_pos;

        # defining labels
        activities = ['positive', 'negative']

        # portion covered by each label
        slices = ['pos','neg']

        # color for each label
        colors = ['r', 'm']

        # plotting the pie chart
        plt.pie(slices, labels=activities, colors=colors,
                startangle=90, shadow=True, explode=(0, 0.1),
                radius=1.2, autopct='%1.1f%%')

        # plotting legend
        plt.legend()

        # showing the plot
        plt.show()
    else:
        print 'Status code other than 200 received!'





'''
************************************************ MAIN M E N U **********************************************
'''
def start_bot():
    while True:
        print '\n'
        print 'Hey! Welcome to instaBot!'
        print 'Here are your menu options:'
        print "a.Get your own details\n"
        print "b.Get ID of user by username\n"
        print "c.Get details of a user by username\n"
        print "d.Get your own recent post\n"
        print "e.Get the recent post of a user by username\n"
        print "f.Get ID of recent post by username\n"
        print "g.Like the recent post of a user\n"
        print "h.Make a comment on the recent post of a user\n"
        print "i.Get a list of people who have liked the recent post of a user\n"
        print "j.Get the ID of recent post like by self\n"
        print "k.Get the post in creative way by username\n"
        print "l.Get a list of comments on the recent post of a user\n"
        print "m.Delete negative comments from the recent post of a user\n"
        print "n.Plot the piechart based on positive and negative comment\n"
        print "o.Exit"

            choice = raw_input("Enter you choice: ")
            if choice == "a":
                self_info()
            elif choice =="b":
                insta_username = raw_input("Enter the username of the user: ")
                get_user_id(insta_username)
            elif choice == "c":
                insta_username = raw_input("Enter the username of the user: ")
                get_user_info(insta_username)
            elif choice == "d":
                get_own_post()
            elif choice == "e":
                insta_username = raw_input("Enter the username of the user: ")
                get_user_post(insta_username)
            elif choice =="f":
                insta_username = raw_input("Enter the username of the user: ")
                get_post_id(insta_username)
            elif choice =="g":
                insta_username = raw_input("Enter the username of the user: ")
                like_a_post(insta_username)
            elif choice =="h":
                insta_username = raw_input("Enter the username of the user: ")
                post_comment(insta_username)
            elif choice =="i":
                insta_username = raw_input("Enter the username of the user: ")
                no_of_user_likes(insta_username)
            elif choice =="j":
                insta_username = raw_input("Enter the username of the user: ")
                recent_like_by_user(insta_username)
            elif choice =="k":
                insta_username = raw_input("Enter the username of the user: ")
                try_creative_ways(insta_username)
            elif choice =="l":
                insta_username = raw_input("Enter the username of the user: ")
                list_of_comment(insta_username)
            elif choice =="m":
                insta_username = raw_input("Enter the username of the user: ")
                delete_negative_comment(insta_username)
            elif choice =="n":
                insta_username = raw_input("Enter the username of the user: ")
                plot_piechart(insta_username)
            else:
                print "wrong choice"
       


'''
CALLING THE START_BOT() TO GET THE MENU AND PERFORM OPERATION BASED ON USER'S CHOICE
'''
start_bot()