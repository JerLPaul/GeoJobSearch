""" Pytest tests """
from bs4 import BeautifulSoup
from scraper import get_job_title
from scraper import get_job_location
from scraper import get_job_salary
from scraper import get_job_summary
from scraper import get_company_name
from scraper import get_job_cards
from preparedata import escape_single_quotes
from preparedata import create_sql_line

BAD_TITLE = "No Title Found"
BAD_LOC = "No Location Found"
BAD_COMP = "No Company Found"
BAD_SAL = "No Salary Found"
BAD_SUM = "No Job Summary Found"

INDEED_FILE = "testingFiles/indeedListing"
DUMMY_FILE = "testingFiles/dummyFile"
PAGE_SOURCE = "testingFiles/pageSource"

def test_get_job_title_one():
    """Get job title from Indeed test file"""
    with open(INDEED_FILE, "r", encoding="utf8") as f:
        job_soup = BeautifulSoup(f.read(), "html.parser")
    assert get_job_title(job_soup) != BAD_TITLE

def test_get_job_title_two():
    """ Get (non-existent) job title from dummy test file"""
    with open(DUMMY_FILE, "r", encoding="utf8") as f:
        job_soup = BeautifulSoup(f.read(), "html.parser")
    assert get_job_title(job_soup) == BAD_TITLE

def test_get_job_location_one():
    """ Get job location from Indeed test file"""
    with open(INDEED_FILE, "r", encoding="utf8") as f:
        job_soup = BeautifulSoup(f.read(), "html.parser")
    assert get_job_location(job_soup) != BAD_LOC

def test_get_job_location_two():
    """ Get (non-existent) job location from dummy test file"""
    with open(DUMMY_FILE, "r", encoding="utf8") as f:
        job_soup = BeautifulSoup(f.read(), "html.parser")
    assert get_job_location(job_soup) == BAD_LOC

def test_get_company_name_one():
    """ Get company name from Indeed test file"""
    with open(INDEED_FILE, "r", encoding="utf8") as f:
        job_soup = BeautifulSoup(f.read(), "html.parser")
    assert get_company_name(job_soup) != BAD_COMP

def test_get_company_name_two():
    """ Get (non-existent) company name from dummy test file"""
    with open(DUMMY_FILE, "r", encoding="utf8") as f:
        job_soup = BeautifulSoup(f.read(), "html.parser")
    assert get_company_name(job_soup) == BAD_COMP

def test_get_job_salary_one():
    """ Get job salary from Indeed test file"""
    with open(INDEED_FILE, "r", encoding="utf8") as f:
        job_soup = BeautifulSoup(f.read(), "html.parser")
    assert get_job_salary(job_soup) != BAD_SAL

def test_get_job_salary_two():
    """ Get (non-existent) job salary from dummy test file"""
    with open(DUMMY_FILE, "r", encoding="utf8") as f:
        job_soup = BeautifulSoup(f.read(), "html.parser")
    assert get_job_salary(job_soup) == BAD_SAL

def test_get_job_summary_one():
    """ Get job summary from Indeed test file"""
    with open(INDEED_FILE, "r", encoding="utf8") as f:
        job_soup = BeautifulSoup(f.read(), "html.parser")
    assert get_job_summary(job_soup) != BAD_SUM

def test_get_job_summary_two():
    """ Get (non-existent) job summary from dummy test file"""
    with open(DUMMY_FILE, "r", encoding="utf8") as f:
        job_soup = BeautifulSoup(f.read(), "html.parser")
    assert get_job_summary(job_soup) == BAD_SUM

def test_get_job_cards_one():
    """ Testing job source function """
    with open(PAGE_SOURCE, "r", encoding="utf8") as f:
        soup = get_job_cards(f.read())
    assert len(soup) != 0

def test_get_job_cards_two():
    """ Testing job cards two """
    with open(DUMMY_FILE, "r", encoding="utf8") as f:
        soup = get_job_cards(f.read())
    assert len(soup) == 0

def test_escape_one():
    """ One """
    string = escape_single_quotes("'test'")
    assert string == "''test''"

def test_escape_two():
    """ None """
    string = escape_single_quotes("test")
    assert string == "test"

def test_escape_three():
    """ Three """
    string = escape_single_quotes("'''test'''")
    assert string == "''''''test''''''"

def test_escape_four():
    """ Empty String """
    string = escape_single_quotes("")
    assert string == ""

def test_escape_five():
    """ Test single quote """
    string = escape_single_quotes("'")
    assert string == "''"

def test_create_sql_line_one():
    """ Test creation of sql line """
    list_one = ["Title", "Company", "Location", "Summary", "Link", "Salary"]
    line = create_sql_line(list_one)
    title = "Title"
    company = "Company"
    location = "Location"
    summary = "Summary"
    link = "Link"
    salary = "Salary"
    expected = "INSERT INTO jobs (title, company, location, "
    expected += "description, summary, link, salary) VALUES("
    expected += f"'{title}', '{company}', '{location}', "
    expected += f"'{summary}', '{summary}', '{link}', '{salary}');\n"
    assert line == expected

def test_create_sql_line_two():
    """ Test creation of sql line again"""
    list_one = ["Title", "Company", "Location", "Summary", "Link", "Salary"]
    line = create_sql_line(list_one)
    title = "titl"
    company = "compan"
    location = "locatio"
    summary = "summar"
    link = "lin"
    salary = "salar"
    expected = "insert into jobs (title, company, location, "
    expected += "description, summary, link, salary) values("
    expected += f"'{title}', '{company}', '{location}', "
    expected += f"'{summary}', '{summary}', '{link}', '{salary}');\n"
    assert line != expected

def test_create_sql_line_three():
    """ Test creation of sql line with empty strings"""
    list_one = ["Title", "Company", "Location", "Summary", "Link", "Salary"]
    line = create_sql_line(list_one)
    title = ""
    company = ""
    location = ""
    summary = ""
    link = ""
    salary = ""
    expected = "INSERT INTO jobs (title, company, location, "
    expected += "description, summary, link, salary) VALUES("
    expected += f"'{title}', '{company}', '{location}', "
    expected += f"'{summary}', '{summary}', '{link}', '{salary}');\n"
    assert line != expected
