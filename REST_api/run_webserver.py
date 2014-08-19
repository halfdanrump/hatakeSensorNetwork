import argparse
from app import flapp, socketio, conf
import os

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument('--env', choices = ('test', 'dev', 'prod'), default = 'dev')
	args = parser.parse_args()

	


	if args.env == 'test':
		print 'TEST ENVIRONMENT NOT IMPLEMENTED YET. QUITTING!'
		os._exit(1)
	elif args.env == 'dev':
		conf.config_development(flapp)
	elif args.env == 'production':
		conf.config_production(flapp)
		
	socketio.run(flapp, port = 8080)