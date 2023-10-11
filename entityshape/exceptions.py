class LangError(BaseException):
    pass


class EntityIdError(BaseException):
    pass


class EidError(BaseException):
    pass


class ApiError(BaseException):
    pass


class WikibaseEntitySchemaDownloadError(BaseException):
    pass


class WikibasePropertiesDownloadError(BaseException):
    pass


class NoEntitySchemaDataError(BaseException):
    pass


class MissingInformationError(BaseException):
    pass
