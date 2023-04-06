from flask import request 
from . import api 
from app.models import Post, User

@api.route('/')
def index():
    return 'Hello this is the API'

@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return [post.to_dict() for post in posts]

@api.route('/posts/<post_id>')
def get_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        return {'error': f'Post with the ID of {post_id} does not exist.'}, 404
    return post_id.to_dict()

# Endpoint to create a new post
@api.route('/posts', methods=["POST"])
def create_post():
    # Check to see that the request body is JSON aka application/json content-type
    if not request.is_json:
        return {'error': 'Your request content-type must be application/json'}, 400
    # Get the data from the request body
    data = request.json
    # Validate the incoming data
    required_fields = ['title', 'body', 'user_id']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            # If the field is not in the request body, add that to missing fields list
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400
    title = data.get('title')
    body = data.get('body')
    image_url = data.get('image_url')
    user_id = data.get('user_id')

    new_post = Post(title=title, body=body, image_url=image_url, user_id=user_id)

    return new_post.to_dict(), 201

@api.route('/users', methods=['GET'])
def get_users():
    users = Post.query.all()
    return [users.to_dict() for user in users]

@api.route('/user/<user_id>', methods={'GET'})
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return {'error': f'User with the ID of {user_id} does not exist.'}, 404
    return user_id.to_dict()

   # Endpoint to create a new post
@api.route('/user', methods=["POST"])
def create_user():
    # Check to see that the request body is JSON aka application/json content-type
    if not request.is_json:
        return {'error': 'Your request content-type must be application/json'}, 400
    # Get the data from the request body
    data = request.json
    # Validate the incoming data
    required_fields = ['user_id', 'first_name', 'last_name', 'email', 'username', 'password', 'date_created', 'posts']
    missing_fields = []
    for field in required_fields:
        if field not in data:
            # If the field is not in the request body, add that to missing fields list
            missing_fields.append(field)
    if missing_fields:
        return {'error': f"{', '.join(missing_fields)} must be in the request body"}, 400
    user_id = data.get('user_id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    date_created = data.get('date_created')
    posts = data.get('posts')

    new_user = User(user_id=user_id, first_name=first_name, last_name=last_name, email=email, username=username, password=password, date_created=date_created, posts=posts)

    return new_user.to_dict(), 201
