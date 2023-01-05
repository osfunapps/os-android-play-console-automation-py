import os_android_play_console_automation.bp._binaries_bp as _binaries_bp
from os_android_play_console_automation.bp import _images_bp
from os_android_play_console_automation.types.ImageType import ImageType
from os_android_play_console_automation.types.BinaryType import BinaryType


############################################################################################
# This module aim to automate the most common Google Play Developer actions.               #
#                                                                                          #
# To run, make sure you have the client-secrets.json file. If you don't have it,           #
# read in the GitHub repo on how to acquire it:                                            #
# [link]https://github.com/osfunapps/os-android-google-play-publisher-py#Prerequisites #
############################################################################################

def update_version(package_name, client_secrets_path, publish_percents, version_code):
    """
    Will update a released version

    Args:
        package_name: Your app's package name
        client_secrets_path: The path to your Google's client secrets json (read on how to obtain at 'os_android_apk_google_play_publisher <https://github.com/osfunapps/os-android_apk-google-play-publisher-py#Prerequisites>')
        publish_percents: Roll out percents are -> 0.1 to 10%, 0.85 to 85% etc...
        version_code: The version code of the binary (APK/App Bundle)
    """
    _binaries_bp.publish_binary(package_name, client_secrets_path, publish_percents, version_code, None, None)


def publish_apk(package_name, apk_file_path, client_secrets_path, publish_percents, version_code):
    """
    Will publish a new apk to the Google's Play Store (you HAVE to have a published app in the Google's Play Store already)

    Args:
        package_name: your app's package name
        apk_file_path: the path to your apk file.
        client_secrets_path: the path to your Google's client secrets json (read on how to obtain at 'os_android_apk_google_play_publisher <https://github.com/osfunapps/os_android_apk_google_play_publisher>')
        publish_percents: roll out publish_percents are -> 0.1 to 10%, 0.85 to 85% etc...
        version_code: the version code of the current apk
    """

    if apk_file_path is None:
        raise Exception("Error: apk_file_path is None! If you want to update an already published APK file, call 'update_version()' instead")
    else:
        _binaries_bp.publish_binary(package_name, client_secrets_path, publish_percents, version_code, apk_file_path, BinaryType.APK)


def publish_app_bundle(package_name, app_bundle_path, client_secrets_path, publish_percents, version_code):
    """
    Will publish a new App Bundle to the Google's Play Store (you HAVE to have a published app in the Google's Play Store already)

    Args:
        package_name: your app's package name
        app_bundle_path: the path to your App Bundle file.
        client_secrets_path: the path to your Google's client secrets json (read on how to obtain at 'os_android_apk_google_play_publisher <https://github.com/osfunapps/os_android_apk_google_play_publisher>')
        publish_percents: roll out publish_percents are -> 0.1 to 10%, 0.85 to 85% etc...
        version_code: the version code of the current App Bundle
    """

    if app_bundle_path is None:
        raise Exception("Error: apk_file_path is None! If you want to update an already published APK file, call 'update_version()' instead")
    else:
        _binaries_bp.publish_binary(package_name, client_secrets_path, publish_percents, version_code, app_bundle_path, BinaryType.APP_BUNDLE)


def clear_images(client_secrets_path, package_name, image_type: ImageType, language_initials='en-US'):
    """
    Will clear images of a certain type from a certain app in a certain langauge

    Args:
      client_secrets_path: the path to your Google's client secrets json (read on how to obtain at 'os_android_apk_google_play_publisher <https://github.com/osfunapps/os_android_apk_google_play_publisher>')
      package_name: your app's package name
      image_type: the type of the image
      language_initials: the language in which you want to change the images
  """
    _images_bp.clear_images(client_secrets_path, package_name, image_type, language_initials)


def push_images(client_secrets_path, package_name, image_type: ImageType, img_list, language_initials='en-US', initials_as_google_translate=False):
    """
    Will add a bunch of images of a certain type to a certain app in a certain langauge

    Args:
      client_secrets_path: the path to your Google's client secrets json (read on how to obtain at 'os_android_apk_google_play_publisher <https://github.com/osfunapps/os_android_apk_google_play_publisher>')
      package_name: your app's package name
      image_type: the type of the images
      language_initials: the language in which you want to change the images
      img_list: the list of paths to the images
      initials_as_google_translate: if the initials are represented by the google translate api, select true. This will turn them to Google Play ones
  """
    _images_bp.push_images(client_secrets_path, package_name, image_type, img_list, language_initials, initials_as_google_translate)


# a common executor
def _build_binary_and_run(package_name, client_secrets_path, percents, version_code, binary_file_path, binary_type):
    parsed_flags = _binaries_bp.parse_flags()

    upload = 'false'
    if binary_file_path is not None:
        upload = 'true'

    _binaries_bp.publish_binary(parsed_flags, package_name, binary_file_path, percents, version_code, client_secrets_path, upload, binary_type)
