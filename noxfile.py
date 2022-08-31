import nox


@nox.session
def lint(session):
    session.run("poetry", "run", "black")
    session.run("poetry", "run", "flake8")
