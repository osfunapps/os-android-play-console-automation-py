import enum


class ImageType(enum.Enum):
    PHONE_SCREENSHOTS = 'phoneScreenshots'
    SEVEN_INCH_SCREENSHOTS = 'sevenInchScreenshots'
    TEN_INCH_SCREENSHOTS = 'tenInchScreenshots'
    TV_SCREENSHOTS = 'tvScreenshots'
    WEAR_SCREENSHOTS = 'wearScreenshots'
    ICON = 'icon'
    FEATURE_GRAPHIC = 'featureGraphic'
    TV_BANNER = 'tvBanner'
