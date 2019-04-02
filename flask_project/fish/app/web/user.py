from app.web.webblue import web

@web.route('/user')
def user():
    return 'user'