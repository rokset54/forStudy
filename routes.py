"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime
import floydFormHandler

@route('/')
@route('/Hamiltonov_path')
@view('index')
def Hamiltonov_path():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )


@route('/floyd')
@view('floyd')
def floyd():
    """Renders the contact page."""
    graph = [[0, 2, 0, 3, 1, 0, 0, 10],
     [2, 0, 4, 0, 0, 0, 0, 0],
     [0, 4, 0, 0, 0, 0, 0, 3],
     [3, 0, 0, 0, 0, 0, 0, 8],
     [1, 0, 0, 0, 0, 2, 0, 0],
     [0, 0, 0, 0, 2, 0, 3, 0],
     [0, 0, 0, 0, 0, 3, 0, 1],
     [10, 0, 3, 8, 0, 0, 1, 0],]

    return dict(
        title='Floyds algorithm',
        message='here you can calculate the shortest path of your graph using floyds algorithm',
        year=datetime.now().year,
        answer="",
        graph=graph,
        length=len(graph)
    )

@route('/about')
@view('about')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/authors')
@view('authors')
def authors():
        return dict(
        year=datetime.now().year
    )