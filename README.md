Introduction
------------
This module will automate a bunch of Google Play console actions:
* Publish/Update an Android APK/App Bundle programmatically (dynamically), from an Android project, faster and without Android Studio, to the Google Play Store
* Clear an App screenshots from a certain category, even by language, in an app listing in the Google Play Console
* Clear an app's logo or feature graphic by language in an app listing in the Google Play Console
* Add any images (screenShots, TV Banner, Logo, Feature Graphic and more) to an existing Android app in the Google Play Console.

## Installation

Install via pip:
```python
pip install os_android_play_console_automation
```

# Prerequisites

<B> Google Play Console API isn't open automatically. You should enable it from your Google Play Console account.</b>

To do so, log in to your Google Play Console account and:

1. At the left pane, navigate to <b>Settings -> API Access -> Agree to link your project</b>
2. At the API access page, under <b>"OAuth clients"</b> click on <b>"View in Google Cloud Console"</b>
3. Under OAuth 2.0 Client IDs click on your client id (usually "Google Play Android Developer")
4. At the top, click on "DOWNLOAD JSON" and save the file in a secure location on your computer
5. <b> IMPORTANT: change the JSON file name to be client_secrets.json </b> so Google's algorithm could read it


## Usage

After you've downloaded the ```client_secrets.json``` file, you can use this tool to automate actions.
## Publish an APK

```python
from os_android_play_console_automation import publisher

publisher.publish_apk(package_name='com.my.package',  # the app's package name
                      apk_file_path='path/to/apk.apk',  # the path to the released apk file
                      client_secrets_path='path/to/client_secret.json',  # the client_secret.json file you made in the previous section 
                      publish_percents=0.95,  # 95% published publish_percents
                      version_code=2  # the apk version code
                      )   
```

## Publish an App Bundle

```python
from os_android_play_console_automation import publisher

publisher.publish_app_bundle(package_name='com.my.package',  # the app's package name
                             app_bundle_path='path/to/app_bundle.aab',  # the path to the released .aab file
                             client_secrets_path='path/to/client_secret.json',  # the client_secret.json file you made in the previous section 
                             publish_percents=0.95,  # 95% published publish_percents
                             version_code=2  # the apk version code
                             )   
```


## Update APK/App Bundle

```python
from os_android_play_console_automation import publisher

publisher.update_version(package_name='com.my.package',
                         client_secrets_path='path/to/client_secret.json',
                         publish_percents=0.95,  # 95% published publish_percents
                         version_code=2)  # the apk version code
```

# Clearing and uploading image types

```ImageType``` defines the type of images group you wish to alter. For example, ```ImageType.ICON``` will target a change in your app's logo.

You can see all of the ```ImageType``` [here](os_android_play_console_automation/types/ImageType.py).

## Clear Images

You can clear a bunch of images by request. 

For example, the next command will clear all the phone screenshots in the english language.

```python
from os_android_play_console_automation import publisher
from os_android_play_console_automation.types.ImageType import ImageType

publisher.clear_images(client_secrets_path='path/to/client_secret.json',  # your client secrets,
                       package_name='com.my.package',  # the identifier of the app in the store
                       image_type=ImageType.PHONE_SCREENSHOTS,  # the type of image here (try ImageType.ICON) 
                       language_initials='en-US')  # can be any initials you want (the en-US is the default)
```

## Upload Images

You can add images (one by one) by request. 

For example, the next command will add all the phone screenshots in the english language.

```python
from os_android_play_console_automation import publisher
from os_android_play_console_automation.types.ImageType import ImageType

screenshot_lst = ['path/to/img/1.png', 'path/to/img/2.png']
for ss in screenshot_lst:
    publisher.push_image(client_secrets_path='path/to/client_secret.json',  # your client secrets
                         package_name='com.my.package',  # the identifier of the app in the store
                         image_type=ImageType.PHONE_SCREENSHOTS,  # the type of image here (try ImageType.ICON)
                         path_to_image=ss,
                         language_initials='en-US')  # can be any initials you want (the en-US is the default)
```



## Links
If you all about automation, why use Android Studio?:  
* [os_android_apk_builder-py](https://github.com/osfunapps/os_android_apk_builder-py) will create an Android apk/app bundle programmatically (dynamically), from an Android project, faster and without Android Studio    
* More Android and iOS automation tools can be found in [my profile](https://github.com/osfunapps) 

## Licence
MIT