from sqlalchemy import MetaData
from flask import Flask, jsonify, request, redirect, url_for, render_template
from http import HTTPStatus
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
import sqlite3 as sql
from datetime import datetime
from test import bookmarks, db


import pytest


from Flaskapp import bookmarks

@pytest.fixture
def test_database_manager_add_bookmark(bookmarks):

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
            data = bookmarks.insert().values(id = 9, title = 'Kapoor', url = 'www', notes = 'notes', date_added = '12.3.34')
            result = conn.execute(data)
            assert cursor.fetchone()[0] == 1   