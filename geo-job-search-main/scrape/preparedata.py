""" Module docstring """
import csv

def escape_single_quotes(s):
    """ Escapes single quotes """
    return s.replace("'", "''")

# Needed to do this for code coverage
def create_sql_line(data):
    """ Create SQL command from information and return it """
    line = "INSERT INTO jobs (title, company, location, "
    line += "description, summary, link, salary) VALUES("
    line += f"'{data[0]}', '{data[1]}', '{data[2]}', "
    line += f"'{data[3]}', '{data[3]}', '{data[4]}', '{data[5]}');\n"
    return line

# Needed to do this for code coverage
def process_job(job):
    """ Escapes quotes and then returns SQL string """
    title = escape_single_quotes(job.get('Title', ''))
    company = escape_single_quotes(job.get('Company', ''))
    location = escape_single_quotes(job.get('Location', ''))
    summary = escape_single_quotes(job.get('Summary', ''))
    link = escape_single_quotes(job.get('Link', ''))
    salary = escape_single_quotes(job.get('Salary', ''))
    data = [title, company, location, summary, link, salary]
    line = create_sql_line(data)
    print(line)
    return line

def main():
    """ Main function to modify the csv file and add to the database"""
    input_file_path = 'jobs.csv'  # Change to CSV
    output_file_path = 'data.sql'

    with open(input_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)  # Use DictReader for easy column access

        with open(output_file_path, 'w', encoding='utf-8') as out_file:
            for job in reader:
                out_file.write(process_job(job))

if __name__ == "__main__":
    main()
