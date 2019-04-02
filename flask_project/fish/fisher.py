from app import create_app
#print('1->'+str(id(app)))
app = create_app()
if __name__ == "__main__":
    #print('2->' + str(id(app)))
    app.run(host=app.config['HOST'],port=app.config['PORT'],debug=app.config['DEBUG'])


