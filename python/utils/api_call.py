import requests
import py_utils as pu

def mm_api_login():
	"""log into the mediamath API"""
	creds=pu.load_credentials()['mediamath_api']
	payload={'user':creds['username'],'password':creds['password'],'api_key':creds['key']}
	MM_LOGIN_URL='https://api.mediamath.com/api/v2.0/login'
	s = requests.session()
	s.post(MM_LOGIN_URL, data=payload)
	
	return s


