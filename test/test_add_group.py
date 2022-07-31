# -*- coding: utf-8 -*-

from model.group import Group
import time


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="ewewr", header="gsgdsfg", footer="sdfgdgfsd"))
    app.session.logout()
    time.sleep(1)


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
    time.sleep(1)