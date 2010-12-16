from Products.Collage.browser.views import BaseView
from collective.js.innerfade.browser.folder_innerfade_view import FolderInnerfadeView

class InnerfadeCollageView(BaseView, FolderInnerfadeView):
    title = u'Innerfade View'
