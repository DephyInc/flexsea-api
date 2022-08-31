import nox


@nox.session
def lint(session):
    session.run("poetry", "run", "black", "rsyncs3")
    session.run("poetry", "run", "pylint", "rsyncs3")
