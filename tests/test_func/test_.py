import pytest

def test_connection(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT acft_bnkr_occ_nr FROM adds.acft_bnkr WHERE uuid = '80523d22-5d1a-4a86-b3e4-cfa80d13c8e5'")
    record = cursor.fetchall()
    assert record[0][0] == 0