from website import create_app

app = create_app()

# Only run the webserver if we are running this file. app.run() starts the server
if __name__ == '__main__':
    app.run(debug=True)
