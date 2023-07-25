class Comment:
    total_comments = 0

    def __init__(self, text):
        self.text = text
        self.votes_qty = 0
        Comment.total_comments += 1

    def comparison(self, other):
        if ((self.text == other.text) & (self.votes_qty == other.votes_qty)):
            return True
        else:
            return False


first_comment = Comment("First comment")
# print(Comment.total_comments)
second_comment = Comment("Second comment")
# print(Comment.total_comments)

# print(first_comment.total_comments)

# first_comment.total_comments = 10
# print(first_comment.__dict__)
# print(Comment.__dict__)
# print(Comment.total_comments)
# print(first_comment.total_comments)

print(first_comment.comparison(second_comment))
