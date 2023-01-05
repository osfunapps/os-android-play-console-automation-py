from distutils.core import setup

setup(
    name='os_android_play_console_automation',
    packages=['os_android_play_console_automation',
              'os_android_play_console_automation.types',
              'os_android_play_console_automation.bp'],
    version='1.03',
    license='MIT',
    description='This module will automate a bunch of Google Play actions like publish apk/app bundle and image handling',  # Give a short description about your library
    author='Oz Shabat',
    author_email='admin@os-apps.com',
    url='https://github.com/osfunapps/os-android-play-console-automation-py',  # Provide either the link to your github or to your website
    keywords=['python', 'osfunapps', 'apk', 'google_play', 'play_console', 'app_bundle', 'android', 'automation', 'release', 'publish', 'assemble-release', 'create', 'google-play', 'screenshots', 'logo', 'feature_graphic'],  # Keywords that define your package best
    install_requires=['google-api-python-client', 'oauth2client'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
    ],
)
