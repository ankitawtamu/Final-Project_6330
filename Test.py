import unittest
import sqlite3
from sqlalchemy import MetaData
from flask import Flask, jsonify, request, redirect, url_for, render_template
from http import HTTPStatus
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import sqlite3 as sql
from datetime import datetime
from test import bookmarks, db
from Flaskapp import *
from Flaskapp import app
from Flaskapp import bookmarks


con = sqlite3.connect('Barky/bookmarks.db')
cur = con.cursor()


class TestFlaskapp(unittest.TestCase):


  def test_add_bookmark(self):
        tester = app.test_client(self)
        response = tester.get('adddata')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        

    # arrange
        engine = create_engine('sqlite:///./Barky/bookmarks.db', echo = True)
        meta = MetaData()

        bookmarks = Table(
        'bookmarks', meta, 
            Column('id', Integer, primary_key = True), 
            Column('title', String), 
            Column('url', String), 
            Column('notes', String), 
            Column('date_added', String), 
            )

        conn = engine.connect()
           
        cursor = conn.cursor()
        data = bookmarks.insert().values(id = 8, title = 'Flaskr', url = 'www', notes = 'notes', date_added = '11.3.12')
        result = conn.execute(data)
        assert cursor.fetchone()[0] == 1   