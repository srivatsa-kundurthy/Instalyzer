"""
@Author Srivatsa Kundurthy

"""
import instaloader
from time import sleep
import os.path
import os
import shutil
from datetime import datetime


class InstaData:

    def __init__(self, username, password, account):
        global L
        L = instaloader.Instaloader()
        self.username = username
        self.password = password
        self.account = account
        L.login(self.username, self.password)
        print('Login Completed successfuly. \n')

        global now
        now = datetime.now()

        global filename
        filename = self.account + ' followers - ' + str(now.strftime("%b-%d-%Y %H-%M-%S"))

        global loc
        loc = os.getcwd()
        global path
        path = loc + '\\' + self.account
        print('\n', path, '\n')
        check_dir = os.path.isdir(path)

        if check_dir == False:
            os.mkdir(path)
            print(' \n Path generated successfully:', path)
        elif check_dir == True:
            print(' \n Path exists:', path)

        dir_name = self.account + ' ' + str(now.strftime("%b-%d-%Y %H-%M-%S"))
        global job_path
        job_path = path + '\\' + dir_name
        check_dir = os.path.isdir(job_path)
        os.mkdir(job_path)
        print('\n Job path created successfully:', job_path)

    def migrate_files(self):


        file_list = []

        try:
            for root, dirs, files in os.walk(path):
                for file in files:
                    print(os.path.join(root, file))
                    print('yes')
                    file_list.append(file)
                    shutil.move(os.path.join(path, file), job_path)
                    print('moved')
        except (FileNotFoundError, shutil.Error):
            pass

        print(file_list)

    def get_posts(self):

        print('get_posts run on target ' + self.account)
        profile = instaloader.Profile.from_username(L.context, self.account)


        for post in profile.get_posts():
            L.download_post(post, target=self.account)
            post.get_likes()



        self.migrate_files()

    def get_followers(self):

        # Pull instaloader profile object
        print('Fetching followers...')
        profile = instaloader.Profile.from_username(L.context, self.account)
        # dec var username
        username = ''
        # set counter
        count = 0
        # create text tile

        file = open(filename + '.txt', "w+")

        # header for file
        file.write('\n' + self.account + ' followerlist as of ' + str(now.strftime("%b-%d-%Y %H:%M:%S")))

        for follower in profile.get_followers():
            username = username + '\n' + follower.username
            count = count + 1

        print('Completed: ' + str(count) + ' followers')

        file.write(username)

        file.close()

        shutil.move(filename + '.txt', self.account)

        # sleep(2)

        self.migrate_files()

    def get_followees(self):
        print('Fetching followees...')
        profile = instaloader.Profile.from_username(L.context, self.account)
        # dec var username
        username = ''
        # set counter
        count = 0
        # create text tile

        file = open(filename + '.txt', "w+")

        # header for file
        file.write('\n' + self.account + ' followeelist as of ' + str(now.strftime("%b-%d-%Y %H:%M:%S")))

        for followee in profile.get_followees():
            username = username + '\n' + followee.username
            count = count + 1

        print('Completed: ' + str(count) + ' followers')

        file.write(username)

        file.close()

        shutil.move(filename + '.txt', self.account)

        # sleep(2)

        self.migrate_files()

    def get_hashtags(self):
        hashtag = instaloader.Hashtag.from_name(L.context, self.account)

        for post in hashtag.get_posts():
            L.download_post(post, target="#" + self.account)

        self.migrate_files()

    def get_follower_posts(self):
        print('get_follower_posts \n get post metadata of all followers and self \n \n')
        print('WARNING: Please ensure computational capabilities of device before proceeding. \
\n Process will be time-taking. Proceed with caution. DO NOT ATTEMPT ON ACCOUNTS WITH LARGE FOLLOWING \
CTRL + C TO STOP. \n \n')

        sleep(5)

        self.get_followers()

        p_followers = open(path + '\\' + filename + '.txt', 'r')
        followers = p_followers.read().split('\n')
        p_followers.close()

        for i in range(2):
            del followers[0]

        followers.append(self.account)

        # print(followers)

        n = len(followers) - 1

        for i in range(n):
            follower = followers[i]
            print(follower)
            profile = instaloader.Profile.from_username(L.context, follower)
            for post in profile.get_posts():
                L.download_post(post, target=follower)
                post.get_likes()

        for follower in profile.get_followers():
            self.migrate_files()

        print(' \n Follower posts fetched successfully.')








