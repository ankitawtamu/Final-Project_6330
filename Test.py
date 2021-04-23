from re import X
import unittest
import sqlite3
from unittest import result, mock
from app import *
from flask.templating import render_template
from app import app
from app import *
from event import Event_handler
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from flask import Flask, jsonify, request, redirect, url_for, render_template


con = sqlite3.connect('complaints.db')
cur = con.cursor()

# x=cur.execute("select COUNT(*) from complain where store_name='walmart'")

# print(x.fetchone())

# con.close()


class Testapp(unittest.TestCase):

    #Test route for home page 
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Customer Service', response.data)


    #Test route for dashboard page 
    def test_dashboard(self):
        tester = app.test_client(self)
        response = tester.get('/dashboard')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Customer profile', response.data)

    #      #Test route for service page 
    def test_service(self):
        tester = app.test_client(self)
        response = tester.get('/service')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertIn(b'Type of Service', response.data)


    #   #Test route for complaint page 
    def test_complaint(self):
         tester = app.test_client(self)
         response = tester.get('/complaint')
         statuscode = response.status_code
         self.assertEqual(statuscode, 200)
         self.assertIn(b'Lodge a compliant', response.data)


    # # Testing delete page route
    def test_delete(self):
         tester = app.test_client(self)
         response = tester.get('/delete')
         statuscode = response.status_code
         self.assertEqual(statuscode, 200)
         self.assertIn(b'Delete', response.data)

        # Testing update page route
    def test_update(self):
         tester = app.test_client(self)
         response = tester.get('/update')
         statuscode = response.status_code
         self.assertEqual(statuscode, 200)
         self.assertIn(b'Update', response.data)

    def test_select(self):
        cur.execute("select * from complain where id = 4")
        out = cur.fetchone()
        assert out == (4, 'Ankita Singh', 'Phone not working', 'walmart', '2021-04-17T22:01:41.700439')

    def test_order(self):
        cur.execute("select * from complain ORDER BY description")
        out = cur.fetchone()
        assert out == (2, 'Flower Sen', 'Chicken not fresh', 'walmart', '2021-04-17T21:57:49.414989')

    def test_order_DESC(self):
        cur.execute("select * from complain ORDER BY name DESC" )
        out = cur.fetchone()
        assert out == (7, 'Tim Wex','Issues with apparel', 'walmart', '2021-04-19T17:52:20.306933')

    def test_count(self):
        cur.execute("select COUNT(*) from complain")
        out = cur.fetchone()
        assert out == (7,)

    def test_columncount(self):
        cur.execute("select COUNT(*) from complain where store_name='walmart'")
        out = cur.fetchone()
        assert out == (3,)  

# Testing add complaint function by using mocking method
    @mock.patch('app.addcomplaint')
    def test_addcomplaint(self, test_mock):
        test_mock = addcomplaint
        assert test_mock is addcomplaint

    # Testing update complaint function by using mocking method
    @mock.patch('app.updatecomplaint')
    def test_updatecomplaint(self, test_mock):
        test_mock = updatecomplaint
        assert test_mock is updatecomplaint

    # Testing delete complaint function by using mocking method
    @mock.patch('app.deletecomplaint')
    def test_deletecomplaint(self, test_mock):
        test_mock = deletecomplaint
        assert test_mock is deletecomplaint

    # Testing event handler function by using mocking method
    @mock.patch('app.Event_handler')
    def test_Event_handler(self, test_mock):
        test_mock = Event_handler
        assert test_mock is Event_handler




if __name__ == "__main__":
    unittest.main()