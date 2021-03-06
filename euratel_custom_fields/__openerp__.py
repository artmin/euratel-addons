{
    'name': 'Amamedis Custom Fields',
    'category': 'Tools',
    'summary': 'Custom fields for Amamedis',
    'version': '1.0',
    'description': """
Benutzerdefinierte Felder für Amamedis
Kundenansicht:

* Lastschrift Mandatsreferenz
* BGA
* Vorname
* Filialen
* Änderungen an den Ansichten
        """,
    'author': 'artmin IT-Dienstleistungen',
    'depends': ['sale'],
    'data': [
        'views/partner_view.xml',
        'views/sale_view.xml',
    ],
    'installable': True,
    'auto-install' : False,
}
