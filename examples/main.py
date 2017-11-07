
import sys
import os

def main():
    from googlemaps.android.factories import install
    install()

    #: Called to start your app
    from enamlnative.android.app import AndroidApplication
    app = AndroidApplication()
    #app.debug = True #: Uncomment to debug the bridge
    #app.dev = 'server' #: Uncomment to enable reloading
    app.reload_view = reload_view
    app.deferred_call(load_view, app)
    app.start()


def load_view(app):
    #: Create and show the enaml view
    import enaml
    with enaml.imports():
        from view import ContentView
        app.view = ContentView()
    app.show_view()


def reload_view(app):
    #: This is called when an app reload is requested in dev mode
    import enaml
    with enaml.imports():
        import view
        reload(view)
        app.view = view.ContentView()
    app.show_view()

