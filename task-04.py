

class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        indent = "  " * level
        print(f"{indent}{self.author}: {self.text}")

        for reply in self.replies:
            reply.display(level + 1)


root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")
reply3 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)
reply1.add_reply(reply3)
reply2.remove_reply()

print(root_comment.display())
