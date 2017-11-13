import tornado.ioloop
import tornado.web
import mysql_connection
import json

class UserHandler(tornado.web.RequestHandler):
    def get(self):
        user_list = []
        conn = mysql_connection.create_mysql_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM user")
        # print all the first cell of all the rows
        for row in cur.fetchall():
            user_item = {}
            user_item["id"] = row[0]
            user_item["username"] = row[1]
            user_item["password"] = row[2]
            user_item["status"]=row[3]
            user_list.append(user_item)
        conn.close()
        self.write(json.dumps(user_list))

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/users", UserHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()