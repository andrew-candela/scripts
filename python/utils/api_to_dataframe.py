import pandas as pd 
import py_utils as pu
import StringIO as stio


#hit the MM api and make a data frame:
def api_performance(start_date='2016-07-20',end_date='2016-07-21')
	ORGANIZATION_ID=100062

	URL='https://api.mediamath.com/reporting/v1/std/performance/'
	dims=['exchange_id','advertiser_id','advertiser_name','campaign_id','campaign_name','strategy_id','strategy_name','exchange_name','creative_name','creative_id','creative_size']
	mets=['clicks','impressions','post_click_conversions','post_view_conversions','media_cost','total_spend','total_ad_cost']

	params = {}
	params['dimensions'] = ','.join(dims)
	params['metrics'] = ','.join(mets)
	params['start_date'] = start_date
	params['end_date'] = end_date
	params['time_rollup']='by_day'
	params['filter'] = 'organization_id={}'.format(ORGANIZATION_ID)

	s=pu.mm_api_login()
	r=s.get(URL,params=params)
	if r.status_code == 200:
		data=stio.StringIO(r.content)
		df = pd.read_csv(data,sep=',')
		return df
	else:
		raise ValueError('looks like you got a bad response from the API')
