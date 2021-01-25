# imports

from modules import module as mod

# GIT INFO

API_TOKEN = 'd3739fbed22921d17f5b0b493aa45360ad319896'
USERNAME = 'marinafdezban'
BASE_URL = 'https://api.github.com/'
KEY = 'repos/'
OWNER = 'ta-data-mad/'
REPO = 'dataptmad1120/'
SEARCH = 'search/issues?q=repo:' + OWNER + REPO + '+type:pr+state:{}'
PULLS = 'pulls?page={}&per_page=100&state={}'
COMMITS = 'pulls/{}/commits'
STATE = 'open'


print('starting...')

def main():
    DF_PULLS = mod.get_pulls(BASE_URL, KEY, OWNER, REPO, PULLS, SEARCH, STATE, USERNAME, API_TOKEN, field_list1)
    DF_STATUS = mod.df_status(DF_PULLS, BASE_URL, KEY, OWNER, REPO, COMMITS, USERNAME, API_TOKEN, field_list2)

    DF_CSV = mod.create_csv(DF_STATUS, field_sort1, field_name1)

    print('ending...')


if __name__ == '__main__':
    main()

 
