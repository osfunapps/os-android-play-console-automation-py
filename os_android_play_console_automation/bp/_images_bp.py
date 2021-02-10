##############################################################
# just the boiler plate of the images handling actions       #
##############################################################

import argparse
from os_android_play_console_automation.bp import _shared_tools
from os_android_play_console_automation.types.ImageType import ImageType

from oauth2client import client


# will clear all of the images in the server
def clear_images(client_secrets_path, package_name, image_type: ImageType, language_initials):
    try:
        service = _shared_tools.build_service(client_secrets_path)
        edit_id = _shared_tools.get_edit_id(service, package_name)

        service.edits().images().deleteall(
            packageName=package_name,
            editId=edit_id,
            language=language_initials,
            imageType=image_type.value,
        ).execute()
        print(f'All of the {image_type.value} removed for package name "{package_name}" with the language "{language_initials}"')

        _shared_tools.commit(service, edit_id, package_name)

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run the '
              'application to re-authorize')


# will push an image to the server
def push_image(client_secrets_path, package_name, image_type: ImageType, path_to_image, language_initials='en-US'):
    try:
        service = _shared_tools.build_service(client_secrets_path)
        edit_id = _shared_tools.get_edit_id(service, package_name)

        service.edits().images().upload(
            packageName=package_name,
            editId=edit_id,
            language=language_initials,
            imageType=image_type.value,
            media_body=path_to_image
        ).execute()
        print(f'Image for {image_type.value} added for package name "{package_name}" with the language "{language_initials}"')

        _shared_tools.commit(service, edit_id, package_name)

    except client.AccessTokenRefreshError:
        print('The credentials have been revoked or expired, please re-run the '
              'application to re-authorize')
