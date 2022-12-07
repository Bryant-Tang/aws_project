from detect_image import detect_one_label
from flask import Flask, render_template, request


def index():
    return render_template("index.html")


def sayhello(username):
    print(username)
    return render_template("sayhello.html", username=username)


def chat_room():
    return render_template("chatroom.html")


def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['file1']
        result = detect_one_label(file1)
        return result

        return 'ok'
    return '''
    <h1>Upload new File</h1>
    <form method="post" enctype="multipart/form-data">
      <input type="file" name="file1">
      <input type="submit">
    </form>
    '''
