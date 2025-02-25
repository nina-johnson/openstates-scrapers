from openstates.scrape import State
from .bills import WVBillScraper
from .events import WVEventScraper


class WestVirginia(State):
    scrapers = {
        "bills": WVBillScraper,
        "events": WVEventScraper,
    }
    legislative_sessions = [
        {
            "_scraped_name": "2011",
            "classification": "primary",
            "identifier": "2011",
            "name": "2011 Regular Session",
            "start_date": "2011-01-12",
            "end_date": "2011-03-18",
        },
        {
            "_scraped_name": "2012",
            "classification": "primary",
            "identifier": "2012",
            "name": "2012 Regular Session",
            "start_date": "2012-01-11",
            "end_date": "2012-03-10",
        },
        {
            "_scraped_name": "2013",
            "classification": "primary",
            "identifier": "2013",
            "name": "2013 Regular Session",
            "start_date": "2013-01-09",
            "end_date": "2013-04-14",
        },
        {
            "_scraped_name": "2014",
            "classification": "primary",
            "identifier": "2014",
            "name": "2014 Regular Session",
            "start_date": "2014-01-08",
            "end_date": "2014-03-10",
        },
        {
            "_scraped_name": "2015",
            "classification": "primary",
            "identifier": "2015",
            "name": "2015 Regular Session",
            "start_date": "2015-01-14",
            "end_date": "2015-03-14",
        },
        {
            "_scraped_name": "2016",
            "classification": "primary",
            "identifier": "2016",
            "name": "2016 Regular Session",
            "start_date": "2016-01-13",
            "end_date": "2016-03-12",
        },
        {
            "_scraped_name": "2016",
            "classification": "special",
            "identifier": "20161S",
            "name": "2016 First Special Session",
            "start_date": "2016-05-16",
            "end_date": "2016-06-14",
        },
        {
            "_scraped_name": "2017",
            "classification": "primary",
            "identifier": "2017",
            "name": "2017 Regular Session",
            "start_date": "2017-02-08",
            "end_date": "2017-04-09",
        },
        {
            "_scraped_name": "2017",
            "classification": "special",
            "identifier": "20171S",
            "name": "2017 First Special Session",
            "start_date": "2017-05-04",
            "end_date": "2017-06-26",
        },
        {
            "_scraped_name": "2017",
            "classification": "special",
            "identifier": "20172S",
            "name": "2017 Second Special Session",
            "start_date": "2017-10-16",
            "end_date": "2017-10-17",
        },
        {
            "_scraped_name": "2018",
            "classification": "primary",
            "identifier": "2018",
            "name": "2018 Regular Session",
            "start_date": "2018-01-10",
            "end_date": "2018-03-10",
        },
        {
            "_scraped_name": "2018",
            "classification": "special",
            "identifier": "20181S",
            "name": "2018 First Special Session",
            "start_date": "2018-05-20",
            "end_date": "2018-05-25",
        },
        {
            "_scraped_name": "2018",
            "classification": "special",
            "identifier": "20182S",
            "name": "2018 Second Special Session",
            "start_date": "2018-08-12",
            "end_date": "2018-10-15",
        },
        {
            "_scraped_name": "2019",
            "classification": "primary",
            "identifier": "2019",
            "name": "2019 Regular Session",
            "start_date": "2019-01-14",
            "end_date": "2019-03-09",
        },
        {
            "_scraped_name": "2019",
            "classification": "special",
            "identifier": "20191S",
            "name": "2019 First Special Session",
            "start_date": "2019-05-20",
            "end_date": "2019-10-01",
        },
        {
            "_scraped_name": "2020",
            "classification": "primary",
            "identifier": "2020",
            "name": "2020 Regular Session",
            "start_date": "2020-01-08",
            "end_date": "2020-03-07",
        },
        {
            "_scraped_name": "2021",
            "classification": "primary",
            "identifier": "2021",
            "name": "2021 Regular Session",
            "start_date": "2021-01-13",
            "end_date": "2021-04-10",
        },
        {
            "_scraped_name": "2021",
            "classification": "special",
            "identifier": "20211S",
            "name": "2021 First Special Session",
            "start_date": "2021-06-07",
            "end_date": "2021-06-11",
        },
        {
            "_scraped_name": "2021",
            "classification": "special",
            "identifier": "20212S",
            "name": "2021 Second Special Session",
            "start_date": "2021-06-24",
            "end_date": "2021-06-25",
        },
        {
            "_scraped_name": "2021",
            "classification": "special",
            "identifier": "20213S",
            "name": "2021 Third Special Session",
            "start_date": "2021-06-24",
            "end_date": "2021-06-25",
            "active": False,
        },
        {
            "_scraped_name": "2022",
            "classification": "special",
            "identifier": "20221S",
            "name": "2022 First Special Session",
            "start_date": "2021-01-10",
            # TODO: update end date
            "end_date": "2021-01-12",
            "active": True,
        },
        {
            "_scraped_name": "2022",
            "classification": "primary",
            "identifier": "2022",
            "name": "2022 Regular",
            "start_date": "2022-01-12",
            "end_date": "2022-06-25",
            "active": True,
        },
    ]
    ignored_scraped_sessions = [
        "2029",
        *(str(each) for each in range(1940, 2011)),
    ]

    def get_session_list(self):
        from utils import url_xpath

        return url_xpath(
            "http://www.legis.state.wv.us/Bill_Status/Bill_Status.cfm",
            '//select[@name="year"]/option/text()',
        )
