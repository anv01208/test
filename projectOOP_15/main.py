from users import User, Admin, all_users
from messages import Message

# Создание Users и Admin
era = User("Era")
print("Новый пользователь Era...")
ulan = User("Ulan")
print("Новый пользователь Ulan...")
admin = Admin('Admin')

# Добавление друзей
era.add_friend(ulan)
print("\nera добавил ulan в друзья...")
ulan.add_friend(era)
print("ulan добавил era в друзья...")
print('\n')

# Сообщения
print(Message(era, ulan, "Hi, how are you?"))
print(Message(ulan, era, "Hello, I'm good, you?"))

# Создание постов
post1 = era.add_post("Hello, World!")
post2 = ulan.add_post("Python is the BEST!")

# Добавление комментариев
post1.add_comment(ulan, "Nice post!")
post2.add_comment(era, "Agree!")

# Лайки
post1.add_like()
for _ in range(5):
    post2.add_like()  # 5 likes to the post №2

# All posts
for post in era.posts:
    print(f"\n{era.username}'s post:")
    print(f"Content: {post.content}")
    print(f"Likes: {post.likes}")
    print("Comments:")
    for comment in post.comments:
        print(f"{comment.commenter.username}: {comment.text}")

for post in ulan.posts:
    print(f"\n{ulan.username}'s post:")
    print(f"Content: {post.content}")
    print(f"Likes: {post.likes}")
    print("Comments:")
    for comment in post.comments:
        print(f"{comment.commenter.username}: {comment.text}")

print("------------------------------ADMIN------------------------------")

admin.delete_like(post2)
print('Admin deleted 1 like from 2nd post...')
for post in ulan.posts:
    print(f"\n{ulan.username}'s post:")
    print(f"Content: {post.content}")
    print(f"Likes: {post.likes}   ----->   -1 like")
    print("Comments:")
    for comment in post.comments:
        print(f"{comment.commenter.username}: {comment.text}")


print(f"\nUsers before: {all_users}")
admin.delete_user(ulan)
print('Admin deleted user "Ulan"...')
print(f"Users after: {all_users}")

