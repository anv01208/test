from posts import Post
all_users = []


class User:

    def __init__(self, username):
        self.username = username
        self.posts = []
        self.friends = []
        all_users.append(self)

    def add_post(self, content):
        post = Post(self, content)
        self.posts.append(post)
        return post

    def add_friend(self, friend):
        self.friends.append(friend)

    def __repr__(self):
        return f"username = {self.username}"


class Admin(User):

    def __init__(self, username):
        super().__init__(username)

    def delete_user(self, user):
        all_users.remove(user)

    def delete_like(self, post):
        post.likes = post.likes - 1

    def __repr__(self):
        return f"admin_username = {self.username}"



