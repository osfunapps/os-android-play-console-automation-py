from os_android_play_console_automation.bp import sample_tools

PLAY_INITIALS_BANK = ['en-GB', 'af', 'am', 'ar', 'hy-AM', 'az-AZ', 'bn-BD', 'eu-ES', 'be', 'bg', 'my-MM', 'ca', 'zh-HK', 'zh-CN', 'zh-TW', 'hr', 'cs-CZ', 'da-DK', 'nl-NL', 'en-AU', 'en-IN', 'en-SG',
                      'en-ZA', 'en-CA', 'en-US', 'et', 'fil', 'fi-FI', 'fr-FR', 'fr-CA', 'gl-ES', 'ka-GE', 'de-DE', 'el-GR', 'hi-IN', 'hu-HU', 'is-IS', 'id', 'it-IT', 'ja-JP', 'kn-IN', 'km-KH',
                      'ko-KR', 'ky-KG', 'lo-LA', 'lv', 'lt', 'mk-MK', 'ms', 'ml-IN', 'mr-IN', 'mn-MN', 'ne-NP', 'no-NO', 'fa', 'pl-PL', 'pt-BR',
                      'pt-PT', 'ro', 'ro', 'ru-RU', 'sr', 'si-LK', 'sk', 'sl', 'es-419', 'es-ES', 'es-US', 'sw', 'sv-SE', 'ta-IN', 'te-IN', 'th', 'tr-TR', 'uk', 'vi', 'zu']


# will build the service
def build_service(client_secrets_path):
    args = [str(__file__)]

    # Authenticate and construct service.
    service, flags = sample_tools.init(
        args,
        'androidpublisher',
        'v3',
        __doc__,
        client_secrets_path,
        parents=[],
        scope='https://www.googleapis.com/auth/androidpublisher')

    # fix google's shitty algorithm of calculating timeout of the http driver to make sure the apk uploaded successfully
    service._http.timeout = 300
    return service


# will get the edit id from the execute
def get_edit_id(service, package_name):
    edit_request = service.edits().insert(body={}, packageName=package_name)
    result = edit_request.execute()
    return result['id']


# will commit the request to Edit's api
def commit(service, edit_id, package_name):
    commit_request = service.edits().commit(editId=edit_id, packageName=package_name).execute()
    print('Edit "%s" has been committed' % (commit_request['id']))

# will turn a google translate language initials to Google Play translation initials
def google_translate_to_google_play_initials(translate_initials):
    if translate_initials == 'pt':
        print(f'Notice: Got the initials "pt". By default returning pt-brazil')
        return 'pt-BR'
    elif translate_initials == 'es':
        return 'es-ES'
    elif translate_initials == 'ur':
        return 'ur'
    elif translate_initials == 'kk':
        return 'kk'
    elif translate_initials == 'tl':
        return 'fil'
    elif translate_initials == 'he':
        return 'iw'
    elif translate_initials == 'in':
        return 'id'
    elif translate_initials == 'ur':
        return 'uk'
    play_initials = next((play_lang for play_lang in PLAY_INITIALS_BANK if play_lang.startswith(translate_initials)), None)
    return play_initials
