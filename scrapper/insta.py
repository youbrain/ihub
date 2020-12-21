import requests
import json


cookies = {
    "ig_did": "58971998-1837-4A06-B2DA-2DBEAB6B2250",
    "mid": "XrujiAALAAHHAKk-gpcHvE3x4TMV",
    "ds_user_id": "5961078248",
    "csrftoken": "mmc2td6kSwrZZzNMsu0F8fLCntQCxqLL",
    "sessionid": "5961078248%3AOLUa6tDvgbHjJz%3A15",
}


class InstaParser:
    def __init__(self, cookies):
        self.session = requests.session()
        self.cookies = cookies

    def get_profil_id(self, username):
        r = self.session.get(
            'https://www.instagram.com/' + username + '/', cookies=self.cookies)
        return r.text.split('profilePage_')[1].split('"')[0]

    def get_tagged_posts(self, profil_id):
        r = self.session.get(
            'https://www.instagram.com/graphql/query/' +
            '?query_hash=31fe64d9463cbbe58319dced405c6206&variables={"id":' +
            profil_id + ',"first":9999}',
            cookies=self.cookies
        )

        r_json = json.loads(r.text)
        posts = r_json['data']['user']['edge_user_to_photos_of_you']['edges']
        return posts


if __name__ == '__main__':
    parser = InstaParser(cookies)
    hub_id = parser.get_profil_id('ihub_khm')
    posts = parser.get_tagged_posts(hub_id)

    print(
'https://www.instagram.com/p/' + posts[0]['node']['shortcode'],      # link
posts[0]['node']['taken_at_timestamp'], # published time
posts[0]['node']['owner']['username'], # owner username
posts[0]['node']['edge_media_to_caption']['edges'][0]['node']['text'], # description
posts[0]['node']['display_url'], # photo link
posts[0]['node']['edge_media_to_comment']['count'], # cooments count
posts[0]['node']['edge_liked_by']['count'], # likes count
    )
