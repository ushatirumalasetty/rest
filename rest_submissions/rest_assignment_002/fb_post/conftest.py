import pytest

from fb_post.models import User, Post, Reaction, Comment

@pytest.fixture
def user():
    user_obj = User.objects.create(name="ammu")
    return user_obj

@pytest.fixture
def user2():
    User.objects.create(name="ammu")
    user_obj2 = User.objects.create(name="ammudu")
    return user_obj2

@pytest.fixture
def user3():
    User.objects.create(name="ammu")
    User.objects.create(name="ammudu")
    user_obj3 = User.objects.create(name="usha")
    return user_obj3

@pytest.fixture
def user4():
    User.objects.create(name="ammu")
    User.objects.create(name="ammudu")
    User.objects.create(name="usha")
    user_obj4 = User.objects.create(name="usha tirumalasetty")
    return user_obj4

@pytest.fixture
def post():
    post_obj1 = Post.objects.create(posted_by_id=1, content="ammu is a very good girl")
    return post_obj1

@pytest.fixture
def post2():
    Post.objects.create(posted_by_id=1, content="ammu is a very good girl")
    post_obj2 = Post.objects.create(posted_by_id=2, content="ammudu is a very good girl")
    return post_obj2

@pytest.fixture
def post3():
    Post.objects.create(posted_by_id=1, content="ammu is a very good girl")
    Post.objects.create(posted_by_id=2, content="ammudu is a very good girl")
    post_obj3 = Post.objects.create(posted_by_id=3, content="usha is a very good girl")
    return post_obj3

@pytest.fixture
def comment():
    comment_obj = Comment.objects.create(commented_by_id=1, post_id=1, content="yes ofcourse!!!")
    return comment_obj

@pytest.fixture
def reply_comment():
    reply_comment_obj = Comment.objects.create(commented_by_id=2, post_id=1, content="yes ofcourse!!!", parent_comment_id=1)
    return reply_comment_obj

@pytest.fixture
def reaction():
    reaction_obj = Reaction.objects.create(post_id=1, reaction="WOW", reacted_by_id=1)
    return reaction_obj

@pytest.fixture
def reaction2():
    Reaction.objects.create(post_id=1, reaction="WOW", reacted_by_id=1)
    reaction_obj2 = Reaction.objects.create(post_id=2, reaction="SAD", reacted_by_id=2)
    return reaction_obj2

@pytest.fixture
def reaction3():
    Reaction.objects.create(post_id=1, reaction="WOW", reacted_by_id=1)
    Reaction.objects.create(post_id=2, reaction="SAD", reacted_by_id=2)
    reaction_obj3 = Reaction.objects.create(post_id=3, reaction="WOW", reacted_by_id=3)
    return reaction_obj3

@pytest.fixture
def reaction4():
    Reaction.objects.create(post_id=1, reaction="WOW", reacted_by_id=1)
    Reaction.objects.create(post_id=2, reaction="SAD", reacted_by_id=2)
    Reaction.objects.create(post_id=3, reaction="WOW", reacted_by_id=3)
    reaction_obj4 = Reaction.objects.create(post_id=3, reaction="SAD", reacted_by_id=4)
    return reaction_obj4

@pytest.fixture
def reaction_to_comment():
    reaction_obj = Reaction.objects.create(comment_id=1, reaction="WOW", reacted_by_id=1)
    return reaction_obj


@pytest.fixture
def reaction5():
    reaction_obj = Reaction.objects.create(post_id=3, reaction="SAD", reacted_by_id=4)
    return reaction_obj