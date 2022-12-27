"""Module providing os."""
import os
from ebaysdk.trading import Connection as Trading
from src.ebay.exceptions import (
    TokenNotDefined,
    AppIdNotDefined,
    CertIdNotDefined,
    DevIdNotDefined,
)


class EbayData:
    """Gather eBay data from"""

    def __init__(self):

        # Raise a custom exception if TOKEN is not defined
        try:
            self.token = os.environ["TOKEN"]
        except KeyError as err:
            raise TokenNotDefined from err

        # Raise a custom exception if APP_ID is not defined
        try:
            self.app_id = os.environ["APP_ID"]
        except KeyError as err:
            raise AppIdNotDefined from err

        # Raise a custom exception if CERT_ID is not defined
        try:
            self.cert_id = os.environ["CERT_ID"]
        except KeyError as err:
            raise CertIdNotDefined from err

        # Raise a custom exception if DEV_ID is not defined
        try:
            self.dev_id = os.environ["DEV_ID"]
        except KeyError as err:
            raise DevIdNotDefined from err

        self.api = Trading(
            appid=self.app_id,
            devid=self.dev_id,
            certid=self.cert_id,
            token=self.token,
            config_file=None,
        )
        self.list_auhtorize = ["ActiveList", "UnsoldList"]

    def get_user(self):
        """Get currently authenticated user"""
        user = self.api.execute("GetUser")
        return user.dict().get("User")

    def get_items_ids(self, item_type):
        """Get all item from authenticated user with item_type"""
        all_items_ids = []

        if item_type not in self.list_auhtorize:
            raise ValueError("item_type must be ActiveList or UnsoldList")

        total_page_response = self.api.execute(
            "GetMyeBaySelling",
            {
                item_type: "True",
                "OutputSelector": "PaginationResult",
            },
        )

        total = total_page_response.dict().get(item_type).get("PaginationResult")

        for i in range(1, int(total.get("TotalNumberOfPages")) + 1):
            item_ids_response = self.api.execute(
                "GetMyeBaySelling",
                {
                    item_type: {
                        "Sort": "StartTime",
                        "Pagination": {"PageNumber": str(i)},
                    },
                    "OutputSelector": "ItemID",
                },
            ).dict()

            item_ids = map(
                lambda item: item.get("ItemID"),
                item_ids_response.get(item_type).get("ItemArray").get("Item"),
            )

            all_items_ids += list(item_ids)

        return all_items_ids

    def get_item_by_id(self, item_id):
        """Get item info with item_id"""
        item = self.api.execute(
            "GetItem",
            {"ItemID": str(item_id), "DetailLevel": "ReturnAll"},
        )

        return item.dict().get("Item")


if __name__ == "__main__":
    ebay_data = EbayData()
    print(ebay_data.token)
