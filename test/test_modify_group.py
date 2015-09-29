__author__ = 'vden'
from model.group import Group
import random


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_id = group.id
    group = Group(name="New group")
    app.group.modify_group_by_id(group_id, group)
    new_groups = db.get_group_list()
    index = 0
    for m in old_groups:
        if m.id == group_id:
            return index
        index = index+1
    old_groups[index] = group
    assert old_groups == new_groups
    if check_ui:
        assert sorted(db.get_group_list(True), key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



