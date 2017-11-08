# coding: utf-8

"""
    data.world API

    data.world is designed for data and the people who work with data.  From professional projects to open data, data.world helps you host and share your data, collaborate with your team, and capture context and conclusions as you work.   Using this API users are able to easily access data and manage their data projects regardless of language or tool of preference.  Check out our [documentation](https://dwapi.apidocs.io) for tips on how to get started, tutorials and to interact with the API right within your browser.

    OpenAPI spec version: 0.9.0
    Contact: help@data.world
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FileSourceSummaryResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'url': 'str',
        'sync_status': 'str',
        'sync_summary': 'str',
        'last_sync_start': 'str',
        'last_sync_success': 'str',
        'last_sync_failure': 'str'
    }

    attribute_map = {
        'url': 'url',
        'sync_status': 'syncStatus',
        'sync_summary': 'syncSummary',
        'last_sync_start': 'lastSyncStart',
        'last_sync_success': 'lastSyncSuccess',
        'last_sync_failure': 'lastSyncFailure'
    }

    def __init__(self, url=None, sync_status=None, sync_summary=None, last_sync_start=None, last_sync_success=None, last_sync_failure=None):
        """
        FileSourceSummaryResponse - a model defined in Swagger
        """

        self._url = None
        self._sync_status = None
        self._sync_summary = None
        self._last_sync_start = None
        self._last_sync_success = None
        self._last_sync_failure = None

        self.url = url
        self.sync_status = sync_status
        if sync_summary is not None:
          self.sync_summary = sync_summary
        if last_sync_start is not None:
          self.last_sync_start = last_sync_start
        if last_sync_success is not None:
          self.last_sync_success = last_sync_success
        if last_sync_failure is not None:
          self.last_sync_failure = last_sync_failure

    @property
    def url(self):
        """
        Gets the url of this FileSourceSummaryResponse.
        Source URL of file. Must be an http or https URL.

        :return: The url of this FileSourceSummaryResponse.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this FileSourceSummaryResponse.
        Source URL of file. Must be an http or https URL.

        :param url: The url of this FileSourceSummaryResponse.
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")
        if url is not None and len(url) > 4096:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `4096`")
        if url is not None and len(url) < 1:
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")
        if url is not None and not re.search('^https?.*', url):
            raise ValueError("Invalid value for `url`, must be a follow pattern or equal to `/^https?.*/`")

        self._url = url

    @property
    def sync_status(self):
        """
        Gets the sync_status of this FileSourceSummaryResponse.
        Synchronization status of the file.  This status can be checked periodically after changes are made to the dataset to determine the status of asynchronous syncronization.  * `NEW`: Just created. Not yet synchronized. * `INPROGRESS`: Currently being synchronized. * `LOADED`: Successfully synchronized. * `SYSTEMERROR`: Error state due to synchronization failure.

        :return: The sync_status of this FileSourceSummaryResponse.
        :rtype: str
        """
        return self._sync_status

    @sync_status.setter
    def sync_status(self, sync_status):
        """
        Sets the sync_status of this FileSourceSummaryResponse.
        Synchronization status of the file.  This status can be checked periodically after changes are made to the dataset to determine the status of asynchronous syncronization.  * `NEW`: Just created. Not yet synchronized. * `INPROGRESS`: Currently being synchronized. * `LOADED`: Successfully synchronized. * `SYSTEMERROR`: Error state due to synchronization failure.

        :param sync_status: The sync_status of this FileSourceSummaryResponse.
        :type: str
        """
        if sync_status is None:
            raise ValueError("Invalid value for `sync_status`, must not be `None`")
        allowed_values = ["NEW", "INPROGRESS", "OK", "SYSTEMERROR"]
        if sync_status not in allowed_values:
            raise ValueError(
                "Invalid value for `sync_status` ({0}), must be one of {1}"
                .format(sync_status, allowed_values)
            )

        self._sync_status = sync_status

    @property
    def sync_summary(self):
        """
        Gets the sync_summary of this FileSourceSummaryResponse.
        Human-readable message detailing status of last failed sync.

        :return: The sync_summary of this FileSourceSummaryResponse.
        :rtype: str
        """
        return self._sync_summary

    @sync_summary.setter
    def sync_summary(self, sync_summary):
        """
        Sets the sync_summary of this FileSourceSummaryResponse.
        Human-readable message detailing status of last failed sync.

        :param sync_summary: The sync_summary of this FileSourceSummaryResponse.
        :type: str
        """

        self._sync_summary = sync_summary

    @property
    def last_sync_start(self):
        """
        Gets the last_sync_start of this FileSourceSummaryResponse.
        Date and time when synchronization last started.

        :return: The last_sync_start of this FileSourceSummaryResponse.
        :rtype: str
        """
        return self._last_sync_start

    @last_sync_start.setter
    def last_sync_start(self, last_sync_start):
        """
        Sets the last_sync_start of this FileSourceSummaryResponse.
        Date and time when synchronization last started.

        :param last_sync_start: The last_sync_start of this FileSourceSummaryResponse.
        :type: str
        """

        self._last_sync_start = last_sync_start

    @property
    def last_sync_success(self):
        """
        Gets the last_sync_success of this FileSourceSummaryResponse.
        Date and time when synchronization last finished successfully.

        :return: The last_sync_success of this FileSourceSummaryResponse.
        :rtype: str
        """
        return self._last_sync_success

    @last_sync_success.setter
    def last_sync_success(self, last_sync_success):
        """
        Sets the last_sync_success of this FileSourceSummaryResponse.
        Date and time when synchronization last finished successfully.

        :param last_sync_success: The last_sync_success of this FileSourceSummaryResponse.
        :type: str
        """

        self._last_sync_success = last_sync_success

    @property
    def last_sync_failure(self):
        """
        Gets the last_sync_failure of this FileSourceSummaryResponse.
        Date and time when synchronization last failed.

        :return: The last_sync_failure of this FileSourceSummaryResponse.
        :rtype: str
        """
        return self._last_sync_failure

    @last_sync_failure.setter
    def last_sync_failure(self, last_sync_failure):
        """
        Sets the last_sync_failure of this FileSourceSummaryResponse.
        Date and time when synchronization last failed.

        :param last_sync_failure: The last_sync_failure of this FileSourceSummaryResponse.
        :type: str
        """

        self._last_sync_failure = last_sync_failure

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, FileSourceSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
