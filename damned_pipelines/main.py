# imports

from modules.module import *


def main():
    DF_PULLS = get_pulls(BASE_URL, KEY, OWNER, REPO, PULLS, SEARCH, STATE, USERNAME, API_TOKEN, field_list1)
    DF_STATUS = df_status(DF_PULLS, BASE_URL, KEY, OWNER, REPO, COMMITS, USERNAME, API_TOKEN, field_list2)

    DF_CSV = create_csv(DF_STATUS, field_sort1, field_name1)

    print('starting...')


if __name__ == '__main__':
    main()

    print('ending...')
