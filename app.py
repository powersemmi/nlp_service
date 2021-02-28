import nlp_service

app = nlp_service.create_app()

if __name__ == '__main__':
    app.run(debug=True)