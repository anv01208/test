from comments import Comment


class Post:

    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.comments = []
        self.likes = 0

    def add_comment(self, commenter, comment):
        comment = Comment(commenter, comment)
        self.comments.append(comment)

    def add_like(self):
        self.likes = self.likes + 1
