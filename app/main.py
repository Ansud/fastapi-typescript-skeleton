from application import Application

if __name__ == "__main__":
    app = Application()
    app.run_server(host="0.0.0.0", port=80, debug=False)
