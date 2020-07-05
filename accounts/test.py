from bigbluebutton_api_python import BigBlueButton
import uuid

big = BigBlueButton("http://192.168.1.98/bigbluebutton/", "xhMB9RAMaqwcEn1UHDthqn9ZTEMzY20SftMsgf4fhI")
guid = uuid.uuid1()
my_dict = {'moderatorPW': 'pw', 'attendeePW': '123',
           # 'muteOnStart': 'true', 'welcome': 'Hello World!!!',
           # 'isBreakout': 'true', 'freeJoin': 'true',
           # 'bannerText': 'Welcome to banner', 'allowModsToUnmuteUsers': 'true',
           }


def create_room():
    try:
        creation_room = big.create_meeting(guid, params=my_dict)
        return creation_room, guid
    except Exception as error:
        print(error)

creation_room = create_room()
print(creation_room[0]["xml"], creation_room[1])
# print(big.get_meeting_info(guid))
# data = big.is_meeting_running(guid)
# print(big.get_join_meeting_url(meeting_id=guid, full_name="hazimal", password="pw"))
# print(big.get_join_meeting_url(meeting_id=guid, full_name="user", password="123"))
# print(data["xml"]["running"])
# print(big.get_meetings())
