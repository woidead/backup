# from googletrans import Translator
# translator = Translator()
# def text_transltor(text = 'hello friend', src = 'en', dest = 'ru'):
#     try:
#         translation = translator.translate(text = text, src = src, dest = dest )
#         print(translation.text)
#         return translation.text

#     except Exception as ex:
#         return ex

# text_transltor(text = 'Hello', src = 'en', dest = 'fr')



# def lang_detect(text):
#     langdetect = translator.detect(text)
#     print(f"код языка: {langdetect.lang}") 

# lang_detect('이 문장은 한글로 쓰여졌습니다')

# def synh_trans(text, dest):
#     translations = translator.translate([text], dest=dest)
#     for translation in translations:
#         print(translation.origin, ' -> ', translation.text)
# synh_trans('сегодня хорошая погода', 'en')

# # def main():
# #     print(text_transltor(text = 'Hello', src = 'en', dest = 'ru'))

# # if __name__ == '__main__':
# #     main()
text = {'content_type': 'text', 'id': 199, 'message_id': 199, 'from_user': 
    {'id': 2016079139, 'is_bot': False, 'first_name': 'woidead', 'username': 'woidead', 'last_name': None, 'language_code': 'ru', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None, 'is_premium': None, 'added_to_attachment_menu': None}
    , 'date': 1670760763,
    'chat': {'id': 2016079139, 'type': 'private', 'title': None, 'username': 'woidead', 'first_name': 'woidead', 'last_name': None, 'photo': None, 'bio': None, 'join_to_send_messages': None, 'join_by_request': None, 'has_private_forwards': None, 'has_restricted_voice_and_video_messages': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'message_auto_delete_time': None, 'has_protected_content': None, 'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None},
    'sender_chat': None, 'forward_from': None, 'forward_from_chat': None, 'forward_from_message_id': None, 'forward_signature': None, 'forward_sender_name': None, 'forward_date': None, 'is_automatic_forward': None, 'reply_to_message': None, 'via_bot': None, 'edit_date': None, 'has_protected_content': None, 'media_group_id': None, 'author_signature': None, 'text': 'hello', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_member': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': None, 
    'json': {'message_id': 199, 'from': {'id': 2016079139, 'is_bot': False, 'first_name': 'woidead', 'username': 'woidead', 'language_code': 'ru'}, 
    'chat': {'id': 2016079139, 'first_name': 'woidead', 'username': 'woidead', 'type': 'private'}, 
    'date': 1670760763, 'text': 'hello'}}
# text = text.replace('/trans ', '') 
print(text['json']['text'])