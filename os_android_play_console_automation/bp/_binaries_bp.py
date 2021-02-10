##############################################################
# just the boiler plate of the apk/app bundle publisher file #
##############################################################

import argparse
from os_android_play_console_automation.bp import sample_tools
from oauth2client import client
from os_android_play_console_automation.bp import _shared_tools
from os_android_play_console_automation.types.BinaryType import BinaryType


#
#
# def publish_binary(parsed_flags, package_name, binary_file_path, percents, version_code, client_secrets_path, upload, binary_type):
#     args = [str(__file__), package_name, binary_file_path, str(percents), 'production', str(version_code), upload]
#
#     # Authenticate and construct service.
#     service, flags = sample_tools.init(
#         args,
#         'androidpublisher',
#         'v3',
#         __doc__,
#         client_secrets_path,
#         parents=[parsed_flags],
#         scope='https://www.googleapis.com/auth/androidpublisher')
#
#     # fix google's shitty algorithm of calculating timeout of the http driver to make sure the apk uploaded successfully
#     for key, val in service._http.connections.items():
#         val.sock.settimeout(260)
#
#     # Process flags and read their values.
#     package_name = flags.package_name
#     binary_file = flags.apk_file
#     user_fraction = float(flags.user_fraction)
#
#     track = flags.track
#     version_code = float(flags.version_code)
#     upload = flags.upload
#
#     try:
#
#         # service = _shared_tools.build_service(client_secrets_path)
#         # edit_id = _shared_tools.get_edit_id(service, package_name)
#
#         edit_request = service.edits().insert(body={}, packageName=package_name)
#         result = edit_request.execute()
#         edit_id = result['id']
#
#         if upload == 'true':
#             print("uploading...")
#
#             if binary_type == BinaryType.APK:
#                 binary_response = service.edits().apks().upload(
#                     editId=edit_id,
#                     packageName=package_name,
#                     media_body=binary_file_path
#                 ).execute()
#             elif binary_type == BinaryType.APP_BUNDLE:
#                 binary_response = service.edits().bundles().upload(
#                     editId=edit_id,
#                     packageName=package_name,
#                     media_body=binary_file_path,
#                     media_mime_type="application/octet-stream"
#                 ).execute()
#             else:
#                 raise Exception(f'Binary type {binary_type} not supported!')
#
#             version_code = binary_response['versionCode']
#             print('Version code %d has been uploaded' % binary_response['versionCode'])
#
#         track_response = service.edits().tracks().update(
#             editId=edit_id,
#             track=percents,
#             packageName=package_name,
#             body={u'releases': [obtain_json(user_fraction, version_code)]}).execute()
#
#         print('Track %s is set with releases: %s' % (
#             track_response['track'], str(track_response['releases'])))
#
#         commit_request = service.edits().commit(
#             editId=edit_id, packageName=package_name).execute()
#
#         print('Edit "%s" has been committed' % (commit_request['id']))
#
#     except client.AccessTokenRefreshError:
#         print('The credentials have been revoked or expired, please re-run the '
#               'application to re-authorize')
#
#
# def obtain_json(user_fraction, version_code):
#     if user_fraction != 1:
#         return {
#             u'name': u'Automated release',
#             u'versionCodes': [version_code],
#             u'userFraction': user_fraction,
#             u'status': u'inProgress'
#         }
#
#     else:
#         return {
#             u'name': u'Automated release',
#             u'versionCodes': [version_code],
#             u'status': u'completed'
#         }
#

def publish_binary(package_name, client_secrets_path, publish_percents, version_code, binary_file_path, binary_type: BinaryType):
    try:

        service = _shared_tools.build_service(client_secrets_path)
        edit_id = _shared_tools.get_edit_id(service, package_name)

        if binary_file_path is not None:
            print("uploading...")

            if binary_type == BinaryType.APK:
                binary_response = service.edits().apks().upload(
                    editId=edit_id,
                    packageName=package_name,
                    media_body=binary_file_path
                ).execute()
            elif binary_type == BinaryType.APP_BUNDLE:
                binary_response = service.edits().bundles().upload(
                    editId=edit_id,
                    packageName=package_name,
                    media_body=binary_file_path,
                    media_mime_type="application/octet-stream"
                ).execute()
            else:
                raise Exception(f'Binary type {binary_type} not supported!')

            version_code = binary_response['versionCode']
            print('Version code %d has been uploaded' % binary_response['versionCode'])

        track_response = service.edits().tracks().update(
            editId=edit_id,
            track='production',
            packageName=package_name,
            body={u'releases': [obtain_json(publish_percents, version_code)]}).execute()

        print('Track %s is set with releases: %s' % (
            track_response['track'], str(track_response['releases'])))

        _shared_tools.commit(service, edit_id, package_name)

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run the '
              'application to re-authorize')


def obtain_json(user_fraction, version_code):
    if user_fraction != 1:
        return {
            u'name': u'Automated release',
            u'versionCodes': [version_code],
            u'userFraction': user_fraction,
            u'status': u'inProgress'
        }

    else:
        return {
            u'name': u'Automated release',
            u'versionCodes': [version_code],
            u'status': u'completed'
        }


# # # will parse the required flags for the roll out
# def parse_flags():
#     arg_parser = argparse.ArgumentParser(add_help=False)
#     arg_parser.add_argument('package_name',
#                             help='The package name. Example: com.android.sample')
#     arg_parser.add_argument('apk_file',
#                             nargs='?',
#                             default='apk.apk',
#                             help='The path to the APK file to upload.')
#     arg_parser.add_argument('user_fraction',
#                             nargs='?',
#                             default='0.0',
#                             help='user percentage')
#     arg_parser.add_argument('track',
#                             nargs='?',
#                             default='0.0',
#                             help='should be wither roll out or production')
#     arg_parser.add_argument('version_code',
#                             nargs='?',
#                             default='0.0',
#                             help='version code')
#     arg_parser.add_argument('upload',
#                             nargs='?',
#                             default='0.0',
#                             help='should upload the apk or not')
#     return arg_parser

# # LOG:
# # sample_tools.py is a local copy of Google's sample_tools.py file. This file has been added a cache_discovery=False in:
# # service = discovery.build(name, version, http=http, cache_discovery=False) in order to remember the last dat file
