import pytest


@pytest.fixture
def owner(accounts):
    return accounts[0]


@pytest.fixture
def contract(owner, project):
    with project.config_manager.using_project(project.tests_folder):
        return project.DSNoteTest.deploy(sender=owner)
