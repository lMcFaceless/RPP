import random
import string

import cherrypy
from peewee import *

connection = SqliteDatabase('db.sqlite3')

cursor = connection.cursor()
cursor.execute("INSERT INTO lab_dish (id, title) VALUES (2, 'lasagna');")


# cursor.execute("SELECT name FROM lab_seller")
#
# results = cursor.fetchall()
# print(type(results))

# resultString = ""
# for i in results:
#     print(i)
#     resultString += i[0] + " "


class ModelBase(Model):
    class Meta:
        database = connection


class ShowTables(object):
    @cherrypy.expose
    def index(self):
        return """<html>
          <head></head>
          <body>
            <form method="get" action="showSellers">
              <button type="submit">Показать продавцов</button>
            </form>
            <form method="get" action="showClients">
              <button type="submit">Показать клиентов</button>
            </form>
            <form method="get" action="showDishes">
              <button type="submit">Показать блюда</button>
            </form>
            <form method="get" action="showProducts">
              <button type="submit">Показать продукты</button>
            </form>
            <form method="get" action="showOrders">
              <button type="submit">Показать заказы</button>
            </form>
            <form method="get" action="addProduct">
            <input type="hidden" value="" name="newProduct" />
              <select name = "dishId" value = 0 hidden = "hidden"><option>0</option></select>
              <button type="submit">Добавить продукт</button>
            </form>
            <form method="get" action="updateProductPage">
              <button type="submit">Изменить продукт</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def showSellers(self):
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM lab_seller")

        results = cursor.fetchall()
        print(type(results))
        resultString = ""
        for i in results:
            print(i)
            resultString += i[0] + " "
        return resultString

    @cherrypy.expose
    def showClients(self):
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM lab_client")

        results = cursor.fetchall()
        print(type(results))
        resultString = ""
        for i in results:
            print(i)
            resultString += i[0] + " "
        return resultString

    @cherrypy.expose
    def showDishes(self):
        cursor = connection.cursor()
        cursor.execute("SELECT title FROM lab_dish")

        results = cursor.fetchall()
        print(type(results))
        resultString = ""
        for i in results:
            print(i)
            resultString += i[0] + " "
        return resultString

    @cherrypy.expose
    def showProducts(self):
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM lab_product")

        results = cursor.fetchall()
        print(type(results))
        resultString = ""
        for i in results:
            print(i)
            resultString += i[0] + " "
        return resultString

    @cherrypy.expose
    def showOrders(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM lab_order")
        idResults = cursor.fetchall()
        resultString = ""
        for i in idResults:
            resultString += str(i[0]) + " "
        return resultString

    @cherrypy.expose
    def addProduct(self, dishId, newProduct):
        cursor = connection.cursor()
        lastId = cursor.execute("SELECT MAX (id) FROM lab_product")
        maxId = 0
        for i in lastId:
            maxId = i[0]
        if newProduct != "":
            cursor.execute(f"INSERT INTO lab_product (id, name, dish_id) VALUES({maxId + 1}, \'{newProduct}\', {dishId});")
            cursor.fetchall

        cursor.execute("SELECT id FROM lab_dish")
        idResults = cursor.fetchall()
        optionString = ""
        for i in idResults:
            print(i)
            optionString = optionString + f"<option>{i[0]}</option>"


        return """<html>
          <head></head>
          <body>
            <form method="get" action="addProduct">
                <select name = dishId>
                """ + optionString + """
                </select>
                <input type="text" name="newProduct" />
                <button type="submit">Добавить</button>
            </form>
            <form method="get" action="index">
                <button type="submit">Назад</button>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def updateProductPage(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM lab_dish")
        idResults = cursor.fetchall()
        optionString = ""
        for i in idResults:
            print(i)
            optionString = optionString + f"<option>{i[0]}</option>"

        cursor.execute("SELECT id FROM lab_product")
        idResults = cursor.fetchall()
        productString = ""
        for i in idResults:
            productString = productString + f"<option>{i[0]}</option>"

        return """<html>
          <head></head>
          <body>
          <form method="post" action="updateProduct">
                <select name = "productId">
                """ + productString + """
                </select>
                <input type="text" name="newProductName" />
                <select name = "dishId">
                    """ + optionString + """
                </select>
                <button type="submit">Изменить</button>
          </form>
          </body>
        </html>"""

    @cherrypy.expose
    def updateProduct(self, productId, newProductName, dishId):
        cursor = connection.cursor()
        cursor.execute(f"UPDATE lab_product SET name = '{newProductName}', dish_id = {dishId} WHERE id = {productId};")
        return """<html>
          <head></head>
          <body>
          Успешно изменено!
          </body>
        </html>"""






cherrypy.tree.mount(ShowTables())
cherrypy.engine.start()
cherrypy.engine.block()
connection.close()
