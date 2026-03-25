
from flask import Flask, jsonify, request

app = Flask(__init__)

# Sample data for demonstration
posts = [
    {"id": 1, "title": "First Post", "content": "This is the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the second post."}
]

@app.route('/api/posts', methods=['GET'])
def get_posts():   
  """Retrieves all posts."""
  return jsonify({'post', posts})


@app.route('/api/posts/<int:post_id>', methods=['GET'])
def get_posts():
  post = next((post for post in posts if post['id'] == post_id), None)
  if post:
    return jsonify({'post', post})
  return jsonify({'message': 'Post not found'}), 404


@app.route('api/posts/', methods =['POST'])
def create_post():
  """creates a new post."""
  new_post = request.get_json() # get post from request body
  new_post['id'] = len(posts) + 1
  posts.append(new_post)
  return jsonify({'post': new_post}), 201

@app.route('/api/posts/<int:post_id>', methods =['PUT'])
def update_posts():
    # for p in posts:
    #     if p['id'] == post_id:
    #         post = p
    #         break
    # else:
    #     post = None
  post = next((post for post in posts if post['id'] == post_id), None)
  if not post:
    return jsonify({'message':'Post not found'}), 404 
  updated_post = request.get_json()
  updated_post['id'] = post_id # ensure id remains the same
  posts[post_id - 1 ] = updates_post
  return jsonify({'post':updated_post})

@app.route('/api/posts/<int:post_id>', methods=['PATCH'])
def partial_update_post(post_id):
  """Partially updates a post."""
  post = next((post for post in posts if post['id'] == post_id), None)
  if not post:
    return jsonify({'message': 'Post not found'}), 404
  updates = request.get_json()
  post.update(updates)  # Apply partial updates, update dict method 
  return jsonify({'post': post})

@app.route('/api/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
  """Deletes a post."""
  post = next((post for post in posts if post['id'] == post_id), None)
  if not post:
    return jsonify({'message': 'Post not found'}), 404
  posts.remove(post)
  return jsonify({'message': 'Post deleted'}), 204

if __name__ == '__main__':
  app.run(debug=True)