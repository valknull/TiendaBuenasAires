# TiendaBuenasAires
Tienda Buenos Aires Integración de plataforma
# create user oracledb
    create user c##aires identified by aires;
    grant connect, resource to c##aires;
    alter user c##aires default tablespace users quota unlimited on users;

# database connection settings.py
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '127.0.0.1:1521/xe',
        'USER': 'c##aires',
        'PASSWORD': 'aires',
        'TEST': {
            'USER': 'default_test',
            'TBLSPACE': 'default_test_tbls',
            'TBLSPACE_TMP': 'default_test_tbls_tmp',
        },
    },
}