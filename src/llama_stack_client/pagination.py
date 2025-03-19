# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncDatasetsIterrows", "AsyncDatasetsIterrows"]

_T = TypeVar("_T")


class SyncDatasetsIterrows(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    next_index: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_index = self.next_index
        if not next_index:
            return None

        return PageInfo(params={"start_index": next_index})


class AsyncDatasetsIterrows(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    next_index: Optional[int] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_index = self.next_index
        if not next_index:
            return None

        return PageInfo(params={"start_index": next_index})
