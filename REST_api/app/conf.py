### Settings necessary to use the app in the console
### Note that enrivonment settings override module settings.
module_config = {
	'DATETIME_FORMAT': '%Y-%m-%d-%H:%M:%S:%f',
	'LOGLEVEL': 'DEBUG'
}


### Settings shared between environments
shared_config = {
	
	'CSRF_ENABLED': True,
	'SECRET_KEY': 'you-will-never-guess'
}

def config_production(flapp):
	flapp.config.update(shared_config)
	flapp.config.update(
			DEBUG = False,
			PROPAGATE_EXCEPTIONS = False,
			HOST = 'http://107.170.251.142',
			PORT = '80',
			SQLALCHEMY_DATABASE_URI = "postgresql://halfdan:halfdan@localhost/tekrice_prod",
			LOGLEVEL = 'WARNING'
		)

def config_development(flapp):
	flapp.config.update(shared_config)
	flapp.config.update(
			DEBUG = True,
			PROPAGATE_EXCEPTIONS = True,
			HOST = 'http://120.0.0.1',
			PORT = '8080',
			SQLALCHEMY_DATABASE_URI = "postgresql://halfdan:halfdan@localhost/tekrice_dev",
			LOGLEVEL = 'DEBUG'
		)

def config_test_env(flapp):
	flapp.config.update(shared_config)
	flapp.config.update(
			DEBUG = False,
			PROPAGATE_EXCEPTIONS = False,
			HOST = 'http://120.0.0.1',
			PORT = '8080',
			SQLALCHEMY_DATABASE_URI = "postgresql://halfdan:halfdan@localhost/tekrice_test",
			LOGLEVEL = 'DEBUG'
		)
