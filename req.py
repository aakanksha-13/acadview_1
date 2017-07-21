import  requests

ACCESS_TOKEN='5729772464.38e704c.08c4dd98fe6644f0957b911ef4fe88f8'
BASE_URL='https://api.instagram.com/v1/'

def self_info():
    url=BASE_URL + "users/self/?access_token=%s"%ACCESS_TOKEN
    r=requests.get(url).json()
    if r['meta']['code']==200:
        return r['data']
    else:
        return"Entered wrong details"

#print self_info();
def get_user_id(instagram_username):
    url = BASE_URL + "users/search?q=%s &access_token=%s"%(instagram_username,ACCESS_TOKEN)
    users = requests.get(url).json()['data']#[0]['id']
    if users['meta']['code'] == 200:
        if len(users['data']):
            return users['data']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()

print get_user_id("aakanksht01")
def get_user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()
    request_url = (BASE_URL + 'users/%s?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
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

print get_user_id("aakanksht01")



