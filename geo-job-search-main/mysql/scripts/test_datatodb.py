import unittest
from unittest.mock import patch, MagicMock
import datatodb

class TestDatatodb(unittest.TestCase):

    @patch('datatodb.mysql.connector.connect')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="SELECT * FROM DUMMY;")
    def test_execute_sql_script(self, mock_open, mock_connect):
        mock_connection = mock_connect.return_value
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        datatodb.execute_sql_script('dummy.sql', mock_connection)
        mock_cursor.execute.assert_called_with("SELECT * FROM DUMMY")  # Adjusted to match the actual command without semicolon
        mock_cursor.close.assert_called()  # Ensure cursor is closed
        mock_connection.commit.assert_called()  # Ensure commit is called

    @patch('datatodb.csv.writer')
    @patch('datatodb.mysql.connector.connect')
    def test_export_to_csv(self, mock_connect, mock_csv_writer):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('row1',), ('row2',)]
        mock_cursor.description = [('column1',), ('column2',)]
        datatodb.export_to_csv(mock_cursor, 'test_export.csv')
        mock_csv_writer().writerow.assert_called()  # Check if writerow was called
        mock_csv_writer().writerows.assert_called_with([('row1',), ('row2',)])  # Check if writerows was called with expected data

if __name__ == '__main__':
    unittest.main()